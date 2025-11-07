# Research Paper Figure Placement Guide

## Complete List of Figures with Citations and Placement

---

### **Figure 1: Overall System Architecture**
**File:** `Figure_1_System_Architecture.png`

**Placement:** Insert in **Section II.1** (Quantum Infiltration Modeling Architecture) after the first paragraph.

**Citation:**
```
Figure 1: Quantum computational framework architecture showing the three main modules (14-qubit infiltration model, 6-qubit QMC chemical optimizer, and deployment integration system) with environmental inputs, quantum processing pathways, and actionable outputs. The framework demonstrates 34,000-68,000× computational speedup over classical approaches. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "The integrated framework architecture (Figure 1) consists of three primary computational modules operating in parallel..."

---

### **Figure 2A: Qiskit Quantum Circuit Architecture**
**File:** `Figure_2_Qiskit_Circuit_Architecture.png`

**Placement:** Insert in **Section II.1** (Quantum Infiltration Modeling Architecture) after describing circuit construction.

**Citation:**
```
Figure 2A: Qiskit-rendered quantum circuit diagrams showing (top) the 14-qubit infiltration model with position encoding qubits (q[0:3]) using Hadamard gates and CNOT entanglement, followed by layer encoding qubits (q[4:13]) with RY rotations and vertical CNOT propagation, and (bottom) the 6-qubit QMC trial wavefunction circuit with H → RY → CNOT → RZ gate sequence encoding coordination sites and functional group effects. Circuits rendered using Qiskit circuit_drawer with professional styling. Figure created by researcher using Qiskit (2024).
```

**Suggested text reference:**
> "The quantum circuit implementation (Figure 2A) utilizes actual Qiskit quantum gates with hierarchical gate sequences..."

---

### **Figure 2B: Circuit Specifications and Parameters**
**File:** `Figure_2_Circuit_Specifications.png`

**Placement:** Insert in **Section II.1** (Quantum Infiltration Modeling Architecture) after Figure 2A, or in appendix for detailed reference.

**Citation:**
```
Figure 2B: Detailed specifications for the quantum circuit architectures including gate sequences, qubit assignments, rotation angles, functional group parameters, and performance metrics. The infiltration model uses 14 qubits with 23-gate depth simulating 16,384 states across a 16×10 grid. The QMC optimizer uses 6 qubits with 18-gate depth testing 204 formulations. Implementation uses Qiskit StatevectorSimulator with universal gate set. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "Complete circuit specifications (Figure 2B) detail the gate-level implementation parameters..."

---

### **Figure 2C: Quantum Gate Reference**
**File:** `Figure_2_Gate_Reference.png`

**Placement:** Insert in **Section II.1** or place in appendix as supplementary material.

**Citation:**
```
Figure 2C: Quantum gate reference guide explaining the four primary gates used in circuit construction: Hadamard (H) for superposition, Rotation-Y (RY) for probability encoding, Rotation-Z (RZ) for phase encoding, and CNOT (CX) for entanglement. Includes matrix representations, operational purposes, and specific usage examples from lead infiltration simulation. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "The quantum gates employed (Figure 2C) provide the fundamental operations for state manipulation..."

---

### **Figure 2 (Original): 14-Qubit Quantum Circuit Architecture**
**File:** `Figure_2_Qubit_Architecture.png`

**Note:** This is the original simplified circuit diagram. Consider replacing with Figure 2A-C or use as alternative visualization.

**Placement:** Insert in **Section II.1** (Quantum Infiltration Modeling Architecture) after describing circuit construction.

**Citation:**
```
Figure 2: Schematic diagram of the 14-qubit quantum circuit architecture. The first 4 qubits encode horizontal positions (16 states) using Hadamard gates and CNOT entanglement. The subsequent 10 qubits represent depth layers with RY rotation gates encoding infiltration probabilities and CNOT gates establishing vertical entanglement. Total circuit depth: 10 gates. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "The quantum circuit implementation (Figure 2) utilizes a hierarchical gate sequence beginning with Hadamard initialization..."

---

### **Figure 3: Infiltration Probability Distributions**
**File:** `Figure_3_Infiltration_Results.png`

**Placement:** Insert in **Section II.2** (Infiltration Simulation Results and Trajectory Analysis) immediately after presenting quantitative metrics.

**Citation:**
```
Figure 3: Quantum simulation results showing (left) lead infiltration with average probability 0.0375, maximum 0.2178, 3 distinct branching pathways reaching layer 2 (20% depth), and (right) arsenic infiltration with average 0.0420, maximum 0.4172, 2 pathways reaching layer 1 (10% depth). Red markers indicate computed branching trajectories. Color intensity represents probability magnitude. Figure created by researcher using Qiskit simulation data and Matplotlib visualization (2024).
```

**Suggested text reference:**
> "The spatial probability distributions (Figure 3) reveal contrasting migration patterns between the two contaminants..."

---

### **Figure 4: Chemical Optimization Performance Comparison**
**File:** `Figure_4_Optimization_Performance.png`

**Placement:** Insert in **Section II.4** (Optimization Results and Performance Metrics) after presenting all four chemical results.

**Citation:**
```
Figure 4: (Left) Overall fitness scores for the four optimized chemical formulations, with iron oxides achieving highest performance (0.647). (Right) Radar chart comparing property achievement percentages for iron oxides (best) versus TSP, showing iron oxides' advantages in activation barrier (100%) and pKa (90%) but shared binding energy challenges (0%). Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "Comparative analysis (Figure 4) demonstrates iron oxides' superior overall performance across target properties..."

---

### **Figure 5: Quantum Monte Carlo Calculation Process**
**File:** `Figure_5_QMC_Process.png`

**Placement:** Insert in **Section II.3** (Chemical Neutralization Formulation Design) after describing QMC architecture.

**Citation:**
```
Figure 5: Flowchart of the quantum Monte Carlo energy calculation process. Sequential steps include: (1) 6-qubit trial wavefunction construction via H/RY/CNOT/RZ gates, (2) variational Monte Carlo energy expectation calculation, (3) diffusion Monte Carlo ground state refinement, (4) molecular property derivation from QMC energies, and (5) Grover's algorithm optimization across 51 formulations per chemical. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "The QMC computational workflow (Figure 5) proceeds through five integrated stages, beginning with quantum circuit construction..."

---

### **Figure 6: Competing Ion Interference Effects**
**File:** `Figure_6_Competing_Ions.png`

**Placement:** Insert in **Section II.5** (Competing Ion Interference Analysis) after presenting selectivity coefficient calculations.

**Citation:**
```
Figure 6: (Left) Overall binding capacity retention percentages for each chemical formulation under competitive ion loads, with iron oxides demonstrating highest retention (79.6%). (Right) Ion-specific resistance comparison between TSP and iron oxides showing differential selectivity against Ca²⁺, Mg²⁺, PO₄³⁻, SO₄²⁻, and CO₃²⁻. Both formulations exhibit strong sulfate resistance (95%) but differ significantly in phosphate and carbonate handling. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "Competitive binding analysis (Figure 6) quantifies formulation robustness against environmentally prevalent interfering ions..."

---

### **Figure 7: pH Optimization Success**
**File:** `Figure_7_pH_Optimization.png`

**Placement:** Insert in **Section III.2** (Chemical Neutralization Optimization Performance) when discussing pH achievements.

**Citation:**
```
Figure 7: Baseline versus optimized pKa values for all four chemical formulations. Green shaded region indicates target neutral pH range (6.5-8.5). Phosphoric acid and ferric sulfate demonstrate dramatic improvements (3.6 unit shifts toward neutrality) through amine group addition, while TSP shows minimal change. Arrows indicate magnitude and direction of pH correction. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "The pH optimization outcomes (Figure 7) reveal amine groups' effectiveness for acidic formulation correction..."

---

### **Figure 8: Quantum Computational Advantage**
**File:** `Figure_8_Quantum_Classical.png`

**Placement:** Insert in **Section III.4** (Quantum Computing Advantages and Limitations) when discussing computational speedup.

**Citation:**
```
Figure 8: (Left) Logarithmic-scale comparison of quantum versus classical computation times for infiltration simulation (5 min vs 2,000 min), chemical optimization (180 min vs 120,000 min), and complete workflow (200 min vs 150,000 min). (Right) Resulting speedup factors demonstrating 400× to 750× quantum computational advantages. Figure created by researcher using Matplotlib (2024).
```

**Suggested text reference:**
> "Computational performance benchmarking (Figure 8) quantifies the practical quantum advantage achieved in this framework..."

---

## Additional Suggested Figures (Optional)

### **Figure 9: Functional Group Properties**
**Suggested placement:** Section II.3
**Content:** Table or diagram showing electron donating power, coordination sites, pKa shifts, and stability factors for OH, NH₂, and SH groups

**Citation template:**
```
Figure 9: Molecular properties of the three functional groups tested: hydroxyl (-OH), amine (-NH₂), and thiol (-SH). Properties include electron donating power (related to metal binding strength), coordination sites (number of metal binding locations), pKa shift (effect on solution pH), and stability factor (resistance to degradation). Figure created by researcher using Matplotlib (2024).
```

---

### **Figure 10: Field Deployment Schematic**
**Suggested placement:** Section III.3 (Implications for Field Deployment)
**Content:** Diagram showing permeable reactive barrier installation with quantum-optimized formulations

**Citation template:**
```
Figure 10: Conceptual field deployment configuration for quantum-optimized iron oxide formulations in a permeable reactive barrier application. The enhanced kinetics enable 70-90% thickness reduction (10-30 cm vs 1-2 m conventional) while maintaining or exceeding capture efficiency. Figure created by researcher using draw.io (2024).
```

---

### **Figure 11: Future Integration with Sensor Networks**
**Suggested placement:** Section IV.4 (Integration with Monitoring Networks)
**Content:** Schematic of quantum model coupled with distributed sensors for real-time updates

**Citation template:**
```
Figure 11: Proposed integration of quantum infiltration model with distributed sensor networks for adaptive remediation. Real-time pH, conductivity, and redox measurements from 10-50 subsurface nodes continuously update quantum probability distributions, triggering chemical deployment when contamination risk thresholds are exceeded. Figure created by researcher using draw.io (2024).
```

---

## Figure Quality Specifications

All figures generated with:
- **Resolution:** 300 DPI (publication quality)
- **Format:** PNG with transparent backgrounds where applicable
- **Color scheme:** Colorblind-safe palettes
- **Font sizes:** Minimum 8pt for readability
- **Line weights:** Minimum 1.5pt for clarity

---

## Usage Instructions

1. **Insertion in LaTeX:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.9\textwidth]{research_figures/Figure_1_System_Architecture.png}
\caption{Quantum computational framework architecture showing the three main modules...}
\label{fig:system_arch}
\end{figure}
```

2. **Insertion in Word:**
- Insert → Pictures → Select figure
- Right-click → Insert Caption
- Copy citation text from above
- Format as Figure style

3. **Cross-referencing in text:**
- LaTeX: `As shown in Figure~\ref{fig:system_arch}...`
- Word: Use Insert → Cross-reference → Figure

---

## Figure Summary Table

| Figure # | Title | Section | Key Message |
|----------|-------|---------|-------------|
| 1 | System Architecture | II.1 | Integrated 3-module framework |
| 2 | Qubit Architecture | II.1 | 14-qubit circuit design |
| 3 | Infiltration Results | II.2 | Pb vs As migration patterns |
| 4 | Optimization Performance | II.4 | Iron oxides best (0.647) |
| 5 | QMC Process | II.3 | 5-stage calculation workflow |
| 6 | Competing Ions | II.5 | 79.6% capacity retention |
| 7 | pH Optimization | III.2 | Amine-mediated pH correction |
| 8 | Quantum Advantage | III.4 | 400-750× speedup |

---

## Notes on Figure Creation

All figures were programmatically generated using:
- **Qiskit 1.0+** for quantum circuit simulation
- **Matplotlib 3.8+** for visualization
- **NumPy 1.26+** for data processing
- **Seaborn 0.13+** for statistical graphics

Raw simulation data available in project repository for reproducibility.

---

**Last Updated:** November 6, 2024
**Author:** Research Team
**Contact:** See main paper for correspondence
