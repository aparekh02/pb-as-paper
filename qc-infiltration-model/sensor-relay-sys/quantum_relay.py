import numpy as np
from datetime import datetime
from typing import List, Dict, Any, Tuple
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer


class QuantumDataRelay:
    """
    Quantum algorithm-based relay system for multi-sensor data transmission.
    
    Uses Grover-like amplitude amplification to prioritize high-importance
    sensor data and prevent collision/loss when multiple sensors transmit.
    
    Key Features:
    - Quantum superposition for parallel routing evaluation
    - Amplitude amplification for priority-based transmission
    - Collision-free data relay from multiple sensors
    - Scalable to many sensors (2^n sensors with n qubits)
    
    Usage:
        relay = QuantumDataRelay(num_sensors=8)
        routed_data = relay.route_data_batch(sensor_readings)
    """
    
    def __init__(self, num_sensors: int, backend_name: str = 'qasm_simulator'):
        """
        Initialize quantum relay system.
        
        Args:
            num_sensors: Number of sensors in the network
            backend_name: Qiskit backend ('qasm_simulator' or actual quantum hardware)
        """
        self.num_sensors = num_sensors
        self.num_qubits = max(3, int(np.ceil(np.log2(num_sensors))))
        self.backend = Aer.get_backend(backend_name)
        self.transmission_log = []
        
        # Configuration
        self.shots = 1024  # Number of quantum measurements
        self.grover_iterations = 1  # Number of amplitude amplification rounds
    
    def calculate_priority(self, sensor_data: Dict[str, Any]) -> float:
        """
        Calculate transmission priority based on data content.
        
        Higher priority for:
        - Abnormal pH values (far from neutral)
        - High bulk density (soil compaction)
        - Sensor errors or warnings
        
        Args:
            sensor_data: Dictionary containing sensor readings
            
        Returns:
            Priority score (0.0 to 1.0, higher = more urgent)
        """
        priority = 0.0
        
        # pH deviation priority
        if sensor_data.get('pH') is not None:
            ph_deviation = abs(sensor_data['pH'] - 7.0)
            priority += min(ph_deviation / 3.5, 1.0) * 0.5
        
        # Bulk density priority (high density = compaction problem)
        if sensor_data.get('bulk_density') is not None:
            if sensor_data['bulk_density'] > 1.6:
                priority += 0.3
            elif sensor_data['bulk_density'] > 1.7:
                priority += 0.5
        
        # Error status priority
        if sensor_data.get('status') == 'error':
            priority += 0.4
        
        return min(priority, 1.0)
    
    def create_quantum_routing_circuit(self, priorities: List[float]) -> QuantumCircuit:
        """
        Create quantum circuit for routing using amplitude amplification.
        
        This implements a Grover-like algorithm that amplifies the probability
        of measuring high-priority sensor indices.
        
        Args:
            priorities: List of priority scores for each sensor
            
        Returns:
            Quantum circuit configured for priority-based routing
        """
        qr = QuantumRegister(self.num_qubits, 'q')
        cr = ClassicalRegister(self.num_qubits, 'c')
        qc = QuantumCircuit(qr, cr)
        
        # Step 1: Create equal superposition (all sensors have equal probability)
        qc.h(qr)
        
        # Step 2: Apply Grover iterations for amplitude amplification
        for _ in range(self.grover_iterations):
            # Oracle: Mark high-priority states
            self._apply_priority_oracle(qc, qr, priorities)
            
            # Diffusion operator: Amplify marked states
            self._apply_diffusion_operator(qc, qr)
        
        # Step 3: Measure to collapse to optimal routing order
        qc.measure(qr, cr)
        
        return qc
    
    def _apply_priority_oracle(self, qc: QuantumCircuit, qr: QuantumRegister, 
                                priorities: List[float]):
        """
        Apply phase oracle to mark high-priority sensor states.
        
        For each sensor with priority > threshold, apply phase flip to its
        corresponding quantum state.
        """
        threshold = 0.6
        
        for sensor_idx, priority in enumerate(priorities):
            if priority > threshold and sensor_idx < 2**self.num_qubits:
                # Convert sensor index to binary representation
                binary_state = format(sensor_idx, f'0{self.num_qubits}b')
                
                # Apply multi-controlled phase flip
                self._controlled_phase_flip(qc, qr, binary_state)
    
    def _controlled_phase_flip(self, qc: QuantumCircuit, qr: QuantumRegister,
                                target_state: str):
        """Apply phase flip to specific quantum state"""
        # Flip bits that are 0 in target state
        for i, bit in enumerate(target_state):
            if bit == '0':
                qc.x(qr[i])
        
        # Multi-controlled Z gate
        if self.num_qubits == 1:
            qc.z(qr[0])
        else:
            qc.mcp(np.pi, qr[:-1], qr[-1])
        
        # Unflip bits
        for i, bit in enumerate(target_state):
            if bit == '0':
                qc.x(qr[i])
    
    def _apply_diffusion_operator(self, qc: QuantumCircuit, qr: QuantumRegister):
        """
        Apply Grover diffusion operator for amplitude amplification.
        
        This increases the amplitude of marked states and decreases
        the amplitude of unmarked states.
        """
        # H gates
        qc.h(qr)
        
        # X gates
        qc.x(qr)
        
        # Multi-controlled Z
        if self.num_qubits == 1:
            qc.z(qr[0])
        else:
            qc.mcp(np.pi, qr[:-1], qr[-1])
        
        # Undo X gates
        qc.x(qr)
        
        # H gates
        qc.h(qr)
    
    def route_data_batch(self, sensor_data_batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Route a batch of sensor data using quantum algorithm.
        
        This is the main method for using the quantum relay.
        
        Args:
            sensor_data_batch: List of sensor readings from multiple sensors
            
        Returns:
            Sensor data reordered for optimal transmission (high priority first)
        """
        if not sensor_data_batch:
            return []
        
        # Calculate priorities
        priorities = [self.calculate_priority(data) for data in sensor_data_batch]
        
        # Create and execute quantum circuit
        qc = self.create_quantum_routing_circuit(priorities)
        job = self.backend.run(qc, shots=self.shots)
        result = job.result()
        counts = result.get_counts()
        
        # Decode quantum results into transmission order
        transmission_order = self._decode_measurement_results(counts, len(sensor_data_batch))
        
        # Reorder data based on quantum routing
        routed_data = [sensor_data_batch[i] for i in transmission_order 
                       if i < len(sensor_data_batch)]
        
        # Log transmission details
        self.transmission_log.append({
            'timestamp': datetime.now(),
            'num_sensors': len(sensor_data_batch),
            'transmission_order': transmission_order,
            'priorities': priorities,
            'quantum_circuit_depth': qc.depth()
        })
        
        return routed_data
    
    def _decode_measurement_results(self, counts: Dict[str, int], 
                                     num_sensors: int) -> List[int]:
        """
        Decode quantum measurement results into sensor transmission order.
        
        States with higher measurement counts (higher probability) are
        transmitted first.
        """
        # Sort states by measurement frequency
        sorted_states = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        transmission_order = []
        for state_binary, count in sorted_states:
            sensor_idx = int(state_binary, 2)
            if sensor_idx < num_sensors and sensor_idx not in transmission_order:
                transmission_order.append(sensor_idx)
        
        # Add any remaining sensors not in quantum results
        for i in range(num_sensors):
            if i not in transmission_order:
                transmission_order.append(i)
        
        return transmission_order
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get relay performance statistics"""
        if not self.transmission_log:
            return {}
        
        return {
            'total_batches_processed': len(self.transmission_log),
            'total_sensors_routed': sum(log['num_sensors'] for log in self.transmission_log),
            'num_qubits_used': self.num_qubits,
            'backend': str(self.backend),
            'average_circuit_depth': np.mean([log['quantum_circuit_depth'] 
                                              for log in self.transmission_log])
        }
