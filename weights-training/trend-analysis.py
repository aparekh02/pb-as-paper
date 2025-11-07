"""
Trend Analysis: Linear Regression for pH and Bulk Density vs Heavy Metals
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

# Load the dataset
data = pd.read_csv('soil_contamination_data.csv')

print("Performing linear regression analysis...\n")

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 12)

# Perform linear regression for each relationship
# 1. pH vs Lead
slope_pH_Pb, intercept_pH_Pb, r_pH_Pb, p_pH_Pb, se_pH_Pb = linregress(
    data['pH'], data['Lead_Pb_mg_kg']
)

# 2. pH vs Arsenic
slope_pH_As, intercept_pH_As, r_pH_As, p_pH_As, se_pH_As = linregress(
    data['pH'], data['Arsenic_As_mg_kg']
)

# 3. Bulk Density vs Lead
slope_BD_Pb, intercept_BD_Pb, r_BD_Pb, p_BD_Pb, se_BD_Pb = linregress(
    data['Bulk_Density_g_cm3'], data['Lead_Pb_mg_kg']
)

# 4. Bulk Density vs Arsenic
slope_BD_As, intercept_BD_As, r_BD_As, p_BD_As, se_BD_As = linregress(
    data['Bulk_Density_g_cm3'], data['Arsenic_As_mg_kg']
)

# Create figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: pH vs Lead
ax1 = axes[0, 0]
ax1.scatter(data['pH'], data['Lead_Pb_mg_kg'], alpha=0.6, s=50, color='#e74c3c')
x_pH = np.linspace(data['pH'].min(), data['pH'].max(), 100)
y_pH_Pb = slope_pH_Pb * x_pH + intercept_pH_Pb
ax1.plot(x_pH, y_pH_Pb, 'r-', linewidth=2, label=f'Slope = {slope_pH_Pb:.2f}')
ax1.set_xlabel('pH', fontsize=12, fontweight='bold')
ax1.set_ylabel('Lead (Pb) Concentration (mg/kg)', fontsize=12, fontweight='bold')
ax1.set_title('pH vs Lead (Pb)', fontsize=14, fontweight='bold')
ax1.legend(loc='best', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.text(0.05, 0.95, f'R² = {r_pH_Pb**2:.3f}\np-value = {p_pH_Pb:.4f}', 
         transform=ax1.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 2: pH vs Arsenic
ax2 = axes[0, 1]
ax2.scatter(data['pH'], data['Arsenic_As_mg_kg'], alpha=0.6, s=50, color='#3498db')
y_pH_As = slope_pH_As * x_pH + intercept_pH_As
ax2.plot(x_pH, y_pH_As, 'b-', linewidth=2, label=f'Slope = {slope_pH_As:.2f}')
ax2.set_xlabel('pH', fontsize=12, fontweight='bold')
ax2.set_ylabel('Arsenic (As) Concentration (mg/kg)', fontsize=12, fontweight='bold')
ax2.set_title('pH vs Arsenic (As)', fontsize=14, fontweight='bold')
ax2.legend(loc='best', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.text(0.05, 0.95, f'R² = {r_pH_As**2:.3f}\np-value = {p_pH_As:.4f}', 
         transform=ax2.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 3: Bulk Density vs Lead
ax3 = axes[1, 0]
ax3.scatter(data['Bulk_Density_g_cm3'], data['Lead_Pb_mg_kg'], alpha=0.6, s=50, color='#e67e22')
x_BD = np.linspace(data['Bulk_Density_g_cm3'].min(), data['Bulk_Density_g_cm3'].max(), 100)
y_BD_Pb = slope_BD_Pb * x_BD + intercept_BD_Pb
ax3.plot(x_BD, y_BD_Pb, color='#d35400', linewidth=2, label=f'Slope = {slope_BD_Pb:.2f}')
ax3.set_xlabel('Soil Bulk Density (g/cm³)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Lead (Pb) Concentration (mg/kg)', fontsize=12, fontweight='bold')
ax3.set_title('Bulk Density vs Lead (Pb)', fontsize=14, fontweight='bold')
ax3.legend(loc='best', fontsize=11)
ax3.grid(True, alpha=0.3)
ax3.text(0.05, 0.95, f'R² = {r_BD_Pb**2:.3f}\np-value = {p_BD_Pb:.4f}', 
         transform=ax3.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 4: Bulk Density vs Arsenic
ax4 = axes[1, 1]
ax4.scatter(data['Bulk_Density_g_cm3'], data['Arsenic_As_mg_kg'], alpha=0.6, s=50, color='#2ecc71')
y_BD_As = slope_BD_As * x_BD + intercept_BD_As
ax4.plot(x_BD, y_BD_As, color='#27ae60', linewidth=2, label=f'Slope = {slope_BD_As:.2f}')
ax4.set_xlabel('Soil Bulk Density (g/cm³)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Arsenic (As) Concentration (mg/kg)', fontsize=12, fontweight='bold')
ax4.set_title('Bulk Density vs Arsenic (As)', fontsize=14, fontweight='bold')
ax4.legend(loc='best', fontsize=11)
ax4.grid(True, alpha=0.3)
ax4.text(0.05, 0.95, f'R² = {r_BD_As**2:.3f}\np-value = {p_BD_As:.4f}', 
         transform=ax4.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('soil_trend_analysis.png', dpi=300, bbox_inches='tight')
print("Trend analysis plot saved as 'soil_trend_analysis.png'\n")

# Print detailed results
print("="*80)
print("TREND ANALYSIS RESULTS - LINEAR REGRESSION")
print("="*80)

print("\n1. pH vs LEAD (Pb)")
print("-" * 50)
print(f"   Slope: {slope_pH_Pb:.4f} mg/kg per pH unit")
print(f"   Intercept: {intercept_pH_Pb:.4f}")
print(f"   R² (coefficient of determination): {r_pH_Pb**2:.4f}")
print(f"   Correlation coefficient (r): {r_pH_Pb:.4f}")
print(f"   p-value: {p_pH_Pb:.6f}")
print(f"   Standard error: {se_pH_Pb:.4f}")

print("\n2. pH vs ARSENIC (As)")
print("-" * 50)
print(f"   Slope: {slope_pH_As:.4f} mg/kg per pH unit")
print(f"   Intercept: {intercept_pH_As:.4f}")
print(f"   R² (coefficient of determination): {r_pH_As**2:.4f}")
print(f"   Correlation coefficient (r): {r_pH_As:.4f}")
print(f"   p-value: {p_pH_As:.6f}")
print(f"   Standard error: {se_pH_As:.4f}")

print("\n3. BULK DENSITY vs LEAD (Pb)")
print("-" * 50)
print(f"   Slope: {slope_BD_Pb:.4f} mg/kg per g/cm³")
print(f"   Intercept: {intercept_BD_Pb:.4f}")
print(f"   R² (coefficient of determination): {r_BD_Pb**2:.4f}")
print(f"   Correlation coefficient (r): {r_BD_Pb:.4f}")
print(f"   p-value: {p_BD_Pb:.6f}")
print(f"   Standard error: {se_BD_Pb:.4f}")

print("\n4. BULK DENSITY vs ARSENIC (As)")
print("-" * 50)
print(f"   Slope: {slope_BD_As:.4f} mg/kg per g/cm³")
print(f"   Intercept: {intercept_BD_As:.4f}")
print(f"   R² (coefficient of determination): {r_BD_As**2:.4f}")
print(f"   Correlation coefficient (r): {r_BD_As:.4f}")
print(f"   p-value: {p_BD_As:.6f}")
print(f"   Standard error: {se_BD_As:.4f}")

print("\n" + "="*80)