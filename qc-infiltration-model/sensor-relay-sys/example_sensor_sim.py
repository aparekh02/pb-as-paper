import numpy as np
import time
from datetime import datetime
from typing import List, Dict, Any


class SimulatedSoilSensor:
    """
    Simulated version of SoilSensor for testing.
    Mimics the behavior of the real sensor class.
    """
    
    def __init__(self, sensor_id: str, location: str):
        self.sensor_id = sensor_id
        self.location = location
        self.is_active = True
        
        # Simulate sensor characteristics
        self.base_ph = np.random.uniform(6.0, 7.5)
        self.base_density = np.random.uniform(1.2, 1.5)
        self.noise_level = 0.1
    
    def read_sensors(self) -> Dict[str, Any]:
        """Simulate sensor readings"""
        if not self.is_active:
            return None
        
        # Add some random variation and occasional anomalies
        ph = self.base_ph + np.random.normal(0, self.noise_level)
        density = self.base_density + np.random.normal(0, 0.05)
        
        # Occasional anomaly simulation
        if np.random.random() < 0.1:
            ph += np.random.choice([-2, 2])  # pH spike
        if np.random.random() < 0.05:
            density += 0.3  # Compaction event
        
        return {
            'sensor_id': self.sensor_id,
            'location': self.location,
            'pH': round(np.clip(ph, 4.5, 8.5), 2),
            'bulk_density': round(np.clip(density, 1.0, 1.9), 3),
            'timestamp': datetime.now(),
            'status': 'ok'
        }


class CentralHub:
    """Central processing hub for real-time soil modeling"""
    
    def __init__(self, num_sensors: int):
        from quantum_relay import QuantumDataRelay
        
        self.quantum_relay = QuantumDataRelay(num_sensors)
        self.all_readings = []
        self.spatial_model = {}
    
    def process_sensor_batch(self, sensor_batch: List[Dict[str, Any]]):
        """Process batch of sensor data via quantum relay"""
        # Route data using quantum algorithm
        routed_data = self.quantum_relay.route_data_batch(sensor_batch)
        
        # Store all readings
        self.all_readings.extend(routed_data)
        
        # Update spatial model
        for reading in routed_data:
            self.spatial_model[reading['location']] = {
                'pH': reading['pH'],
                'bulk_density': reading['bulk_density'],
                'last_update': reading['timestamp']
            }
        
        return routed_data
    
    def get_field_statistics(self) -> Dict[str, Any]:
        """Calculate field-wide statistics"""
        if not self.all_readings:
            return {}
        
        ph_values = [r['pH'] for r in self.all_readings if r['pH'] is not None]
        density_values = [r['bulk_density'] for r in self.all_readings 
                         if r['bulk_density'] is not None]
        
        return {
            'avg_ph': np.mean(ph_values),
            'std_ph': np.std(ph_values),
            'min_ph': np.min(ph_values),
            'max_ph': np.max(ph_values),
            'avg_density': np.mean(density_values),
            'std_density': np.std(density_values),
            'total_readings': len(self.all_readings)
        }


def run_simulation():
    """
    Main simulation demonstrating the complete system.
    Shows quantum relay in action with multiple sensors.
    """
    print("=" * 80)
    print("QUANTUM SOIL MONITORING SYSTEM - SIMULATION")
    print("=" * 80)
    print()
    
    # Initialize simulated sensors
    sensors = [
        SimulatedSoilSensor('S001', 'North_Field_A'),
        SimulatedSoilSensor('S002', 'North_Field_B'),
        SimulatedSoilSensor('S003', 'East_Field_A'),
        SimulatedSoilSensor('S004', 'East_Field_B'),
        SimulatedSoilSensor('S005', 'South_Field_A'),
        SimulatedSoilSensor('S006', 'South_Field_B'),
        SimulatedSoilSensor('S007', 'West_Field_A'),
        SimulatedSoilSensor('S008', 'West_Field_B'),
    ]
    
    print(f"✓ Initialized {len(sensors)} soil sensors")
    for sensor in sensors:
        print(f"  • {sensor.sensor_id} @ {sensor.location}")
    print()
    
    # Initialize central hub with quantum relay
    hub = CentralHub(num_sensors=len(sensors))
    print("✓ Central hub initialized")
    print(f"✓ Quantum relay: {hub.quantum_relay.num_qubits} qubits, "
          f"{2**hub.quantum_relay.num_qubits} quantum states")
    print()
    
    # Run multiple collection cycles
    print("=" * 80)
    print("STARTING DATA COLLECTION")
    print("=" * 80)
    print()
    
    num_cycles = 5
    for cycle in range(1, num_cycles + 1):
        print(f"\n{'─' * 80}")
        print(f"CYCLE {cycle}/{num_cycles}")
        print(f"{'─' * 80}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
        print()
        
        # Collect readings from all sensors simultaneously
        sensor_batch = []
        print("📡 Collecting from all sensors...")
        for sensor in sensors:
            reading = sensor.read_sensors()
            sensor_batch.append(reading)
            priority = hub.quantum_relay.calculate_priority(reading)
            status = "⚠️ HIGH" if priority > 0.6 else "✓ normal"
            print(f"  {sensor.sensor_id}: pH={reading['pH']:.2f}, "
                  f"Density={reading['bulk_density']:.3f} g/cm³ "
                  f"[Priority: {priority:.3f} {status}]")
        print()
        
        # Process through quantum relay
        print("🔮 Applying quantum routing algorithm...")
        routed_data = hub.process_sensor_batch(sensor_batch)
        
        # Show quantum routing results
        print("   Quantum transmission order:")
        for i, data in enumerate(routed_data[:5], 1):
            print(f"   {i}. {data['sensor_id']} (pH={data['pH']:.2f}, "
                  f"Density={data['bulk_density']:.3f})")
        if len(routed_data) > 5:
            print(f"   ... and {len(routed_data) - 5} more")
        print()
        
        # Show current field statistics
        stats = hub.get_field_statistics()
        print("📊 Field Statistics:")
        print(f"   pH: {stats['avg_ph']:.2f} ± {stats['std_ph']:.2f} "
              f"(range: {stats['min_ph']:.2f} - {stats['max_ph']:.2f})")
        print(f"   Bulk Density: {stats['avg_density']:.3f} ± {stats['std_density']:.3f} g/cm³")
        print(f"   Total readings: {stats['total_readings']}")
        
        time.sleep(1)
    
    # Final quantum relay statistics
    print("\n" + "=" * 80)
    print("QUANTUM RELAY PERFORMANCE")
    print("=" * 80)
    
    quantum_stats = hub.quantum_relay.get_statistics()
    print("Relay Statistics:")
    print(f"   Total batches processed: {quantum_stats['total_batches_processed']}")
    print(f"   Total sensors routed: {quantum_stats['total_sensors_routed']}")
    print(f"   Qubits utilized: {quantum_stats['num_qubits_used']}")
    print(f"   Average circuit depth: {quantum_stats['average_circuit_depth']:.1f}")
    print(f"   Backend: {quantum_stats['backend']}")
    print()
    
    print("=" * 80)
    print("SIMULATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    run_simulation()
