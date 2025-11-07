# Research Paper Figures - Quick Reference

## 📁 Folder Contents

This folder contains **8 publication-quality figures** (300 DPI PNG) for the research paper on quantum computational modeling of lead-arsenic groundwater infiltration.

---

## 🎯 Quick Figure List

| # | Filename | Use In | Shows |
|---|----------|--------|-------|
| **1** | `Figure_1_System_Architecture.png` | Section II.1 | Overall 3-module framework architecture |
| **2A** | `Figure_2_Qiskit_Circuit_Architecture.png` | Section II.1 | Qiskit-rendered 14-qubit + 6-qubit circuits |
| **2B** | `Figure_2_Circuit_Specifications.png` | Section II.1 | Detailed circuit parameters and specifications |
| **2C** | `Figure_2_Gate_Reference.png` | Section II.1/Appendix | Quantum gate explanations with matrices |
| **2** | `Figure_2_Qubit_Architecture.png` | Section II.1 | Original simplified circuit diagram |
| **3** | `Figure_3_Infiltration_Results.png` | Section II.2 | Lead vs Arsenic probability heatmaps with branching paths |
| **4** | `Figure_4_Optimization_Performance.png` | Section II.4 | Chemical fitness scores + property radar chart |
| **5** | `Figure_5_QMC_Process.png` | Section II.3 | QMC calculation flowchart (5 stages) |
| **6** | `Figure_6_Competing_Ions.png` | Section II.5 | Capacity retention + ion-specific resistance |
| **7** | `Figure_7_pH_Optimization.png` | Section III.2 | Baseline vs optimized pKa values |
| **8** | `Figure_8_Quantum_Classical.png` | Section III.4 | Computational time comparison + speedup factors |

---

## 📋 Standard Citation Format

**Template:**
```
Figure [#]: [Brief description]. [Details about what is shown].
Figure created by researcher using [Matplotlib/Qiskit/draw.io] (2024).
```

**Example (Figure 1):**
```
Figure 1: Quantum computational framework architecture showing the three main
modules (14-qubit infiltration model, 6-qubit QMC chemical optimizer, and
deployment integration system) with environmental inputs, quantum processing
pathways, and actionable outputs. The framework demonstrates 34,000-68,000×
computational speedup over classical approaches. Figure created by researcher
using Matplotlib (2024).
```

---

## 🔍 Figure Highlights

### **Figure 1** - System Architecture
- **Size:** 14×10 inches (533 KB)
- **Key elements:** 3 main modules, input/output boxes, quantum advantage callout
- **Best for:** Introducing overall framework in Section II

### **Figure 2A** - Qiskit Circuit Architecture (NEW - RECOMMENDED)
- **Size:** 16×12 inches
- **Key elements:** Actual Qiskit-rendered circuits, professional gate visualization, both 14-qubit and 6-qubit circuits
- **Best for:** Technical explanation with publication-quality circuit diagrams
- **Advantage:** Uses industry-standard Qiskit circuit drawer for authenticity

### **Figure 2B** - Circuit Specifications (NEW)
- **Size:** 14×10 inches
- **Key elements:** Detailed gate sequences, qubit assignments, rotation angles, performance metrics
- **Best for:** Comprehensive technical reference or appendix material

### **Figure 2C** - Gate Reference (NEW)
- **Size:** 12×8 inches
- **Key elements:** Gate matrices, operational descriptions, example calculations
- **Best for:** Educational supplement or appendix for readers unfamiliar with quantum gates

### **Figure 2** - Qubit Architecture (Original)
- **Size:** 12×8 inches (213 KB)
- **Key elements:** 14 qubit lines, H/RY/CNOT gates, circuit depth annotation
- **Best for:** Simplified circuit overview (consider replacing with 2A-C)

### **Figure 3** - Infiltration Results ⭐
- **Size:** 14×6 inches (403 KB)
- **Key elements:** Side-by-side heatmaps, branching paths overlaid, quantitative metrics
- **Best for:** Showing actual simulation results with visual impact
- **Highlights:** 3 Pb branches vs 2 As branches, depth differences

### **Figure 4** - Optimization Performance
- **Size:** 14×6 inches (460 KB)
- **Key elements:** Fitness bar chart, 6-property radar plot
- **Best for:** Demonstrating iron oxides' superiority (0.647 fitness)

### **Figure 5** - QMC Process
- **Size:** 12×10 inches (286 KB)
- **Key elements:** 5-step flowchart with equations, color-coded boxes
- **Best for:** Explaining computational methodology

### **Figure 6** - Competing Ions
- **Size:** 14×6 inches (186 KB)
- **Key elements:** Capacity retention bars, ion-specific resistance comparison
- **Best for:** Showing real-world performance under ion competition

### **Figure 7** - pH Optimization ⭐
- **Size:** 12×7 inches (189 KB)
- **Key elements:** Before/after bars, target range shading, improvement arrows
- **Best for:** Demonstrating pH correction success (3.6 unit shifts)
- **Highlights:** Visual proof of amine effectiveness

### **Figure 8** - Quantum Advantage
- **Size:** 14×6 inches (207 KB)
- **Key elements:** Log-scale time comparison, speedup factors
- **Best for:** Justifying quantum computational approach

---

## 💡 Usage Tips

### **For LaTeX Users:**
1. Copy all PNG files to your LaTeX project's `figures/` folder
2. Use this template:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{figures/Figure_1_System_Architecture.png}
    \caption{[Insert citation from FIGURE_PLACEMENT_GUIDE.md]}
    \label{fig:system_architecture}
\end{figure}
```

### **For Microsoft Word Users:**
1. Insert → Pictures → Select figure
2. Right-click → Size and Position → Set width to 6.5 inches (for single column) or 6.5-7 inches (for full width)
3. Right-click → Insert Caption → Copy citation from guide
4. Format caption as "Figure [#]:" in bold, rest in regular text

### **For Google Docs Users:**
1. Insert → Image → Upload from computer
2. Resize to fit page width
3. Insert caption below using Insert → Drawing → Text box
4. Copy citation from `FIGURE_PLACEMENT_GUIDE.md`

---

## 📊 Figure Statistics

- **Total figures:** 8
- **Total file size:** ~2.5 MB
- **Average resolution:** 300 DPI
- **Format:** PNG (publication quality)
- **Color mode:** RGB
- **Estimated print size:** 6-14 inches width

---

## 🔧 Regeneration Instructions

If you need to modify or regenerate any figures:

1. Edit the script: `generate_research_figures.py`
2. Run: `python generate_research_figures.py`
3. Figures will be overwritten in this folder

**Dependencies:**
- matplotlib >= 3.8.0
- numpy >= 1.26.0
- seaborn >= 0.13.0

---

## 📖 Complete Documentation

See **`FIGURE_PLACEMENT_GUIDE.md`** for:
- Detailed placement instructions for each figure
- Complete citation text for all figures
- Cross-referencing examples
- LaTeX/Word insertion code
- Figure summary table
- Optional additional figures suggestions

---

## ✅ Quality Checklist

Before submission, verify:
- [ ] All 8 figures present in submission folder
- [ ] Figures numbered sequentially (1-8)
- [ ] Citations match figure content
- [ ] Resolution is 300 DPI or higher
- [ ] Text in figures is readable when printed
- [ ] Color schemes are colorblind-accessible
- [ ] File sizes are reasonable (<1 MB each)
- [ ] Figures referenced in main text

---

## 📞 Support

For questions about:
- **Figure content:** See simulation code in `../quantum_solution_optimizer.py` and `../qc-infiltration-model/quantum_infiltration_sim.py`
- **Figure placement:** See `FIGURE_PLACEMENT_GUIDE.md`
- **Figure regeneration:** See `../generate_research_figures.py`

---

**Generated:** November 6, 2024
**Format:** PNG, 300 DPI, RGB
**Software:** Matplotlib 3.8+ / Python 3.11+
**License:** Research use only
