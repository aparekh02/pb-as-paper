"""
Quantum Simulation of Heavy Metal Infiltration Through Soil Layers

Uses quantum circuits to model particle movement through soil based on:
- Runoff (surface layer)
- Soil type influence
- pH influence on Lead (Pb)
- pH influence on Arsenic (As)

Grid: 16 horizontal x 10 vertical boxes
Qubits: 14 total (4 for surface position encoding, 10 for depth layers)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import math
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector


# Import equations from feature-eq.py
def soiltypehmi(x):
    """y = -exp(-x) + 1"""
    return -math.exp(-x) + 1

def runoffhmi(x):
    """y = exp(-256*10/x)"""
    return math.exp(-256 * 10 / x)

def pHPbhmi(x):
    """y = 100/(1+exp(x-3))"""
    return 100 / (1 + math.exp(x - 3))

def pHAshmi(x):
    """y = (1/1000)(x*5)/(1+x*5)"""
    return (1/1000) * (x * 5) / (1 + x * 5)


class QuantumInfiltrationSimulator:
    """Simulates heavy metal infiltration using quantum circuits."""

    def __init__(self):
        self.width = 16  # Horizontal positions
        self.depth = 10  # Vertical layers
        self.num_position_qubits = 4  # 2^4 = 16 positions
        self.num_layer_qubits = 10  # 10 depth layers
        self.total_qubits = self.num_position_qubits + self.num_layer_qubits

        # Calculate probabilities at t=0
        self.time = 0

        # Surface layer probability (runoff)
        self.p_runoff = runoffhmi(self.time) if self.time > 0 else 1.0

        # Lead (Pb) layer probabilities
        self.soil_type_val = soiltypehmi(10)
        self.ph_pb_val = pHPbhmi(4)
        pb_combined = 0.0878 * self.soil_type_val + 0.9122 * self.ph_pb_val
        # Normalize to [0, 1] range - divide by 100 since pH functions return 0-100 scale
        self.p_pb_layer = min(1.0, pb_combined / 100.0)

        # Arsenic (As) layer probabilities
        self.ph_as_val = pHAshmi(4)
        as_combined = 0.1148 * self.soil_type_val + 0.8852 * self.ph_as_val
        # Already in [0, 1] range but ensure it's clamped
        self.p_as_layer = min(1.0, as_combined)

        print("="*60)
        print("QUANTUM INFILTRATION SIMULATOR")
        print("="*60)
        print(f"\nGrid: {self.width} horizontal x {self.depth} vertical")
        print(f"Qubits: {self.total_qubits} total")
        print(f"  - Position encoding: {self.num_position_qubits} qubits (16 states)")
        print(f"  - Depth layers: {self.num_layer_qubits} qubits")

        print(f"\n--- Probability Calculations (t={self.time}) ---")
        print(f"Surface (Runoff): {self.p_runoff:.6f}")
        print(f"\nLead (Pb) Layer:")
        print(f"  Soil Type HMI: {self.soil_type_val:.6f}")
        print(f"  pH Pb HMI: {self.ph_pb_val:.6f}")
        print(f"  Combined (0.0878*soil + 0.9122*pH): {self.p_pb_layer:.6f}")
        print(f"\nArsenic (As) Layer:")
        print(f"  Soil Type HMI: {self.soil_type_val:.6f}")
        print(f"  pH As HMI: {self.ph_as_val:.6f}")
        print(f"  Combined (0.1148*soil + 0.8852*pH): {self.p_as_layer:.6f}")

    def probability_to_angle(self, prob):
        """Convert probability of |1> to rotation angle for quantum gate."""
        # For RY gate: |0> -> cos(θ/2)|0> + sin(θ/2)|1>
        # P(|1>) = sin²(θ/2) = prob
        # θ/2 = arcsin(sqrt(prob))
        # θ = 2 * arcsin(sqrt(prob))

        # Clamp probability between 0 and 1
        prob = max(0, min(1, prob))
        theta = 2 * np.arcsin(np.sqrt(prob))
        return theta

    def create_pb_circuit(self):
        """Create quantum circuit for Lead (Pb) infiltration."""
        # Create quantum and classical registers
        qr = QuantumRegister(self.total_qubits, 'q')
        cr = ClassicalRegister(self.total_qubits, 'c')
        qc = QuantumCircuit(qr, cr)

        # Layer 0: Surface (position encoding with entanglement)
        # Put all 4 position qubits in superposition
        for i in range(self.num_position_qubits):
            qc.h(qr[i])

        # Entangle position qubits to create 16 correlated states
        for i in range(self.num_position_qubits - 1):
            qc.cx(qr[i], qr[i+1])

        # Apply runoff probability to surface layer
        theta_runoff = self.probability_to_angle(self.p_runoff)
        qc.ry(theta_runoff, qr[4])  # First depth layer

        # Layers 1-9: Pb infiltration layers
        theta_pb = self.probability_to_angle(self.p_pb_layer)
        for layer in range(1, self.num_layer_qubits):
            qubit_idx = self.num_position_qubits + layer
            qc.ry(theta_pb, qr[qubit_idx])
            # Entangle with previous layer
            qc.cx(qr[qubit_idx - 1], qr[qubit_idx])

        return qc, qr, cr

    def create_as_circuit(self):
        """Create quantum circuit for Arsenic (As) infiltration."""
        qr = QuantumRegister(self.total_qubits, 'q')
        cr = ClassicalRegister(self.total_qubits, 'c')
        qc = QuantumCircuit(qr, cr)

        # Layer 0: Surface (position encoding)
        for i in range(self.num_position_qubits):
            qc.h(qr[i])

        # Entangle position qubits
        for i in range(self.num_position_qubits - 1):
            qc.cx(qr[i], qr[i+1])

        # Apply runoff probability
        theta_runoff = self.probability_to_angle(self.p_runoff)
        qc.ry(theta_runoff, qr[4])

        # Layers 1-9: As infiltration layers
        theta_as = self.probability_to_angle(self.p_as_layer)
        for layer in range(1, self.num_layer_qubits):
            qubit_idx = self.num_position_qubits + layer
            qc.ry(theta_as, qr[qubit_idx])
            qc.cx(qr[qubit_idx - 1], qr[qubit_idx])

        return qc, qr, cr

    def simulate_infiltration(self, circuit, metal_name):
        """Simulate particle infiltration and return probability map."""
        print(f"\n{'='*60}")
        print(f"SIMULATING {metal_name} INFILTRATION")
        print(f"{'='*60}")

        # Get statevector
        simulator = AerSimulator(method='statevector')
        circuit_copy = circuit.copy()
        circuit_copy.save_statevector()

        result = simulator.run(circuit_copy).result()
        statevector = result.get_statevector()

        # Extract probabilities for each layer at each horizontal position
        probability_map = np.zeros((self.depth, self.width))

        # For each basis state
        for state_idx, amplitude in enumerate(statevector):
            prob = abs(amplitude) ** 2

            if prob < 1e-10:  # Skip negligible probabilities
                continue

            # Decode state: first 4 bits are position, next 10 are layers
            state_binary = format(state_idx, f'0{self.total_qubits}b')

            # Position (first 4 qubits)
            position_bits = state_binary[:self.num_position_qubits]
            position = int(position_bits, 2)

            # Layer states (next 10 qubits)
            layer_bits = state_binary[self.num_position_qubits:]

            # Accumulate probability for each layer where qubit is |1>
            for layer_idx, bit in enumerate(layer_bits):
                if bit == '1':
                    probability_map[layer_idx, position] += prob

        return probability_map

    def generate_branching_tree(self, probability_map, start_position, metal_name, min_prob=0.001):
        """
        Generate ALL possible branching paths (tree structure).
        Each position can branch to bottom-right and bottom-left.
        """
        print(f"\nGenerating branching tree for {metal_name}...")
        print(f"Starting position: {start_position}")

        # Check surface probability - for visualization, we'll show infiltration if prob > 0.01
        if probability_map[0, start_position] < 0.01:
            print(f"Surface probability too low at position {start_position} ({probability_map[0, start_position]:.4f}) - no significant infiltration")
            return []

        print(f"Surface probability: {probability_map[0, start_position]:.4f} - generating branching tree...")

        # Store all branches: list of paths
        all_branches = []

        # Recursive function to explore all paths
        def explore_branch(current_layer, current_pos, current_path, current_prob):
            # Add current position to path
            path_with_current = current_path + [(current_layer, current_pos)]

            # If we've reached max depth or probability too low, stop
            if current_layer >= self.depth - 1 or current_prob < min_prob:
                all_branches.append((path_with_current, current_prob))
                return

            # Try both directions: right and left
            directions = []

            # Bottom-right
            right_pos = current_pos + 1
            if right_pos < self.width:
                prob_right = probability_map[current_layer + 1, right_pos]
                if prob_right > min_prob:
                    directions.append(('right', right_pos, prob_right))

            # Bottom-left
            left_pos = current_pos - 1
            if left_pos >= 0:
                prob_left = probability_map[current_layer + 1, left_pos]
                if prob_left > min_prob:
                    directions.append(('left', left_pos, prob_left))

            # If no valid moves, this branch ends
            if not directions:
                all_branches.append((path_with_current, current_prob))
                return

            # Explore each direction (creates branching)
            for direction, next_pos, prob in directions:
                new_prob = current_prob * prob
                explore_branch(current_layer + 1, next_pos, path_with_current, new_prob)

        # Start exploration
        initial_prob = probability_map[0, start_position]
        explore_branch(0, start_position, [], initial_prob)

        print(f"Generated {len(all_branches)} total branches")
        return all_branches

    def visualize_infiltration(self, pb_map, as_map, pb_branches, as_branches):
        """Create gradient visualization with branching tree overlay."""
        fig, axes = plt.subplots(1, 2, figsize=(16, 10))

        # Darker colormap with better contrast
        colors = ['#000033', '#000080', '#0000FF', '#4169E1', '#1E90FF',
                  '#00BFFF', '#87CEEB', '#ADD8E6', '#F0F8FF', '#FFFFFF']
        n_bins = 100
        cmap = LinearSegmentedColormap.from_list('infiltration', colors, N=n_bins)

        # Lead (Pb) visualization - ADAPTIVE SCALING
        ax1 = axes[0]
        # Use adaptive range based on actual data
        pb_min = pb_map.min()
        pb_max = pb_map.max()
        pb_range = pb_max - pb_min
        # Set vmax to actual max to make gradient adaptive
        vmin_pb = max(0, pb_min - 0.1 * pb_range)
        vmax_pb = pb_max + 0.05 * pb_range

        im1 = ax1.imshow(pb_map, cmap=cmap, aspect='auto',
                        interpolation='nearest', vmin=vmin_pb, vmax=vmax_pb)
        ax1.set_title('Lead (Pb) Infiltration - Branching Tree\n' +
                     f'Weights: Soil Type (8.78%) + pH (91.22%)\n' +
                     f'Adaptive Range: [{pb_min:.4f}, {pb_max:.4f}]',
                     fontsize=12, fontweight='bold')
        ax1.set_xlabel('Horizontal Position', fontsize=11)
        ax1.set_ylabel('Depth Layer', fontsize=11)
        ax1.set_xticks(range(0, self.width, 2))
        ax1.set_yticks(range(self.depth))
        cbar1 = plt.colorbar(im1, ax=ax1, label='Probability of |1>')
        cbar1.ax.tick_params(labelsize=9)

        # Overlay ALL branches as a tree - BRIGHTER COLORS
        if pb_branches:
            for path, prob in pb_branches:
                if len(path) > 1:
                    path_layers = [p[0] for p in path]
                    path_positions = [p[1] for p in path]
                    # Line thickness based on probability - INCREASED
                    alpha = min(0.95, prob * 5)
                    linewidth = max(2.0, prob * 10)
                    ax1.plot(path_positions, path_layers, '-',
                            color='#FFD700', linewidth=linewidth, alpha=alpha)
            # Add markers at branch points - BRIGHTER
            for path, prob in pb_branches:
                if len(path) > 0:
                    path_layers = [p[0] for p in path]
                    path_positions = [p[1] for p in path]
                    ax1.plot(path_positions, path_layers, 'o',
                            color='#FF4500', markersize=6, alpha=0.9)
            ax1.text(0.02, 0.98, f'{len(pb_branches)} branches',
                    transform=ax1.transAxes, fontsize=11, fontweight='bold',
                    verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9))

        # Arsenic (As) visualization - ADAPTIVE SCALING
        ax2 = axes[1]
        # Use adaptive range based on actual data
        as_min = as_map.min()
        as_max = as_map.max()
        as_range = as_max - as_min
        vmin_as = max(0, as_min - 0.1 * as_range)
        vmax_as = as_max + 0.05 * as_range

        im2 = ax2.imshow(as_map, cmap=cmap, aspect='auto',
                        interpolation='nearest', vmin=vmin_as, vmax=vmax_as)
        ax2.set_title('Arsenic (As) Infiltration - Branching Tree\n' +
                     f'Weights: Soil Type (11.48%) + pH (88.52%)\n' +
                     f'Adaptive Range: [{as_min:.4f}, {as_max:.4f}]',
                     fontsize=12, fontweight='bold')
        ax2.set_xlabel('Horizontal Position', fontsize=11)
        ax2.set_ylabel('Depth Layer', fontsize=11)
        ax2.set_xticks(range(0, self.width, 2))
        ax2.set_yticks(range(self.depth))
        cbar2 = plt.colorbar(im2, ax=ax2, label='Probability of |1>')
        cbar2.ax.tick_params(labelsize=9)

        # Overlay ALL branches as a tree - BRIGHTER COLORS
        if as_branches:
            for path, prob in as_branches:
                if len(path) > 1:
                    path_layers = [p[0] for p in path]
                    path_positions = [p[1] for p in path]
                    # Line thickness based on probability - INCREASED
                    alpha = min(0.95, prob * 5)
                    linewidth = max(2.0, prob * 10)
                    ax2.plot(path_positions, path_layers, '-',
                            color='#FFD700', linewidth=linewidth, alpha=alpha)
            # Add markers at branch points - BRIGHTER
            for path, prob in as_branches:
                if len(path) > 0:
                    path_layers = [p[0] for p in path]
                    path_positions = [p[1] for p in path]
                    ax2.plot(path_positions, path_layers, 'o',
                            color='#FF4500', markersize=6, alpha=0.9)
            ax2.text(0.02, 0.98, f'{len(as_branches)} branches',
                    transform=ax2.transAxes, fontsize=11, fontweight='bold',
                    verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9))

        plt.suptitle('Quantum Simulation: Branching Infiltration Paths',
                    fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig('results/quantum_infiltration_sim.png', dpi=300, bbox_inches='tight')
        print("\nSaved: results/quantum_infiltration_sim.png")
        plt.close()

    def run_simulation(self, start_position=8):
        """Run complete simulation."""
        # Create circuits
        print("\nCreating quantum circuits...")
        pb_circuit, pb_qr, pb_cr = self.create_pb_circuit()
        as_circuit, as_qr, as_cr = self.create_as_circuit()

        print(f"Pb circuit: {pb_circuit.num_qubits} qubits, {pb_circuit.depth()} depth")
        print(f"As circuit: {as_circuit.num_qubits} qubits, {as_circuit.depth()} depth")

        # Simulate infiltration
        pb_map = self.simulate_infiltration(pb_circuit, "Lead (Pb)")
        as_map = self.simulate_infiltration(as_circuit, "Arsenic (As)")

        # Generate branching trees (all possible paths)
        pb_branches = self.generate_branching_tree(pb_map, start_position, "Lead")
        as_branches = self.generate_branching_tree(as_map, start_position, "Arsenic")

        # Visualize
        print("\nGenerating visualization...")
        self.visualize_infiltration(pb_map, as_map, pb_branches, as_branches)

        # Summary statistics
        print("\n" + "="*60)
        print("SIMULATION SUMMARY")
        print("="*60)

        print(f"\nLead (Pb):")
        print(f"  Average infiltration probability: {np.mean(pb_map):.4f}")
        print(f"  Max infiltration probability: {np.max(pb_map):.4f}")
        print(f"  Number of branches: {len(pb_branches)}")
        if pb_branches:
            max_depth = max(len(path) for path, _ in pb_branches)
            print(f"  Deepest penetration: Layer {max_depth-1}/{self.depth}")

        print(f"\nArsenic (As):")
        print(f"  Average infiltration probability: {np.mean(as_map):.4f}")
        print(f"  Max infiltration probability: {np.max(as_map):.4f}")
        print(f"  Number of branches: {len(as_branches)}")
        if as_branches:
            max_depth = max(len(path) for path, _ in as_branches)
            print(f"  Deepest penetration: Layer {max_depth-1}/{self.depth}")

        print("\n" + "="*60)
        print("SIMULATION COMPLETE")
        print("="*60)


if __name__ == '__main__':
    # Set random seed for reproducibility
    np.random.seed(42)

    # Create and run simulator
    sim = QuantumInfiltrationSimulator()

    # Find position with highest surface probability in the middle region for better branching
    pb_circuit, _, _ = sim.create_pb_circuit()
    pb_map = sim.simulate_infiltration(pb_circuit, "Lead (Pb)")

    # Look for best position in middle region (positions 6-10) to allow branching both ways
    middle_positions = range(6, 11)
    middle_probs = [pb_map[0, pos] for pos in middle_positions]
    best_middle_idx = np.argmax(middle_probs)
    best_pos = middle_positions[best_middle_idx]

    print(f"\nBest starting position: {best_pos} (probability: {pb_map[0, best_pos]:.4f})")
    print(f"Surface probability distribution: min={pb_map[0, :].min():.4f}, max={pb_map[0, :].max():.4f}")

    sim.run_simulation(start_position=best_pos)
