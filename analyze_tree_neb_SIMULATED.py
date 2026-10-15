import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy.stats import pearsonr

# Set seaborn theme for publication quality
sns.set_theme(style='whitegrid', palette='colorblind', font='DejaVu Sans')

# Ensure working directories exist
os.makedirs('/workspace/scratch', exist_ok=True)

# Set random seed for reproducible snRNA-seq simulation
np.random.seed(42)

print("Starting Tree-NEB snRNA-seq simulation and processing pipeline...")

# 1. Simulate Single-Nuclei Dataset
n_cells_per_cohort = 800
cohorts = ['15-Year (Juvenile)', '200-Year (Mature)', '600+ Year (Centenarian)']
cell_types = [
    'Central Cambial Stem Cells (WOX4+)',
    'Developing Secondary Xylem (VND6/7+)',
    'Developing Secondary Phloem (APL+)',
    'Mitotic Checkpoint Primed Cells (TPX2+/CDC20.1+)'
]

cell_type_proportions = [0.25, 0.40, 0.25, 0.10]

# Primary Genes of Interest in the Meristem Longevity Niche
genes = [
    'GbWOX4', 'GbPXY', 'GbWUS', 'GbCLV3', 'GbAHK4', 'GbLOG',
    'GbKu70', 'GbKu80', 'GbATG8', 'GbNBR1', 'GbTPX2', 'GbCDC20.1',
    'GbCYC1BAT', 'GbSTM', 'GbAIL1', 'gbi-miR156_target', 'gbi-miR172_target'
]

data_list = []
cell_id = 0

for cohort_idx, cohort in enumerate(cohorts):
    # Age factor: 0 for 15y, 1 for 200y, 2 for 600+y
    age_factor = cohort_idx / 2.0
    
    for ct_idx, ct in enumerate(cell_types):
        n_cells = int(n_cells_per_cohort * cell_type_proportions[ct_idx])
        
        for i in range(n_cells):
            cell_id += 1
            # Pseudotime simulation (0.0 to 1.0 along differentiation trajectory)
            if 'Stem' in ct:
                pseudotime = np.random.beta(1.5, 5.0)
            elif 'Xylem' in ct:
                pseudotime = np.random.beta(4.0, 2.0)
            elif 'Phloem' in ct:
                pseudotime = np.random.beta(3.5, 2.5)
            else: # Mitotic Primed
                pseudotime = np.random.beta(2.0, 3.0)
                
            # Base expression profiles by cell type
            expr = {}
            # Stem cell markers
            expr['GbWOX4'] = np.random.negative_binomial(15, 0.3) if 'Stem' in ct else np.random.negative_binomial(2, 0.5)
            expr['GbPXY'] = np.random.negative_binomial(12, 0.3) if 'Stem' in ct else np.random.negative_binomial(3, 0.5)
            expr['GbWUS'] = np.random.negative_binomial(8, 0.4) if 'Stem' in ct else np.random.negative_binomial(1, 0.7)
            expr['GbCLV3'] = np.random.negative_binomial(6, 0.5) if 'Stem' in ct else np.random.negative_binomial(1, 0.8)
            expr['GbAHK4'] = np.random.negative_binomial(10, 0.4) if ('Stem' in ct or 'Mitotic' in ct) else np.random.negative_binomial(2, 0.6)
            expr['GbLOG'] = np.random.negative_binomial(7, 0.4) if 'Stem' in ct else np.random.negative_binomial(2, 0.6)
            
            # DNA Repair & Quality Control (Maintained high in centenarians!)
            # In centenarians, GbKu70, GbKu80, GbATG8 remain resilient
            repair_boost = 1.15 if cohort_idx == 2 else (1.0 if cohort_idx == 0 else 1.05)
            expr['GbKu70'] = np.random.negative_binomial(int(14 * repair_boost), 0.35)
            expr['GbKu80'] = np.random.negative_binomial(int(12 * repair_boost), 0.35)
            expr['GbATG8'] = np.random.negative_binomial(int(16 * repair_boost), 0.3)
            expr['GbNBR1'] = np.random.negative_binomial(int(10 * repair_boost), 0.4)
            
            # Mitotic Checkpoint Priming
            expr['GbTPX2'] = np.random.negative_binomial(18, 0.25) if 'Mitotic' in ct else np.random.negative_binomial(4, 0.5)
            expr['GbCDC20.1'] = np.random.negative_binomial(15, 0.3) if 'Mitotic' in ct else np.random.negative_binomial(3, 0.5)
            expr['GbCYC1BAT'] = np.random.negative_binomial(14, 0.3) if 'Mitotic' in ct else np.random.negative_binomial(3, 0.5)
            expr['GbSTM'] = np.random.negative_binomial(12, 0.35) if ('Stem' in ct or 'Mitotic' in ct) else np.random.negative_binomial(2, 0.6)
            
            # Heterochronic Axis
            # GbAIL1 remains high in centenarian stem files (Heterochronic Shielding)
            ail1_base = 12 if 'Stem' in ct else 4
            if cohort_idx == 2 and 'Stem' in ct:
                ail1_base = 14 # Shielded!
            expr['GbAIL1'] = np.random.negative_binomial(int(ail1_base), 0.35)
            expr['gbi-miR156_target'] = np.random.negative_binomial(int(10 * (1 - 0.2 * age_factor)), 0.4)
            expr['gbi-miR172_target'] = np.random.negative_binomial(int(5 * (1 + 0.3 * age_factor)), 0.5)
            
            # Somatic Mutation Accumulation (SNVs per cell division cycle)
            # Central Zone stem cells divide rarely -> low mutation rate
            # Centenarian cambium accumulates very low SNV/cycle due to Ku70/80 fidelity
            div_rate = 0.1 if 'Stem' in ct else 1.0
            snv_count = np.random.poisson((20 + cohort_idx * 15) * div_rate)
            
            cell_data = {
                'Cell_ID': f'Cell_{cell_id:04d}',
                'Cohort': cohort,
                'Cohort_Age_Years': 15 if cohort_idx==0 else (200 if cohort_idx==1 else 600),
                'Cell_Type': ct,
                'Pseudotime': pseudotime,
                'Somatic_SNV_Count': snv_count
            }
            cell_data.update(expr)
            data_list.append(cell_data)

df = pd.DataFrame(data_list)
print(f"Dataset generated: {df.shape[0]} single nuclei across {len(genes)} key target genes.")

# Normalize Log1p Expression
expr_cols = genes
df_log = df[expr_cols].apply(lambda x: np.log1p(x))
df_log.columns = [f'{c}_log1p' for c in expr_cols]
df_full = pd.concat([df, df_log], axis=1)

# Save Raw & Processed Counts Table
csv_out_path = '/workspace/scratch/tree_neb_snrna_counts_summary.csv'
df_full.to_csv(csv_out_path, index=False)
print(f"Saved count matrix summary to {csv_out_path}")

# 2. Dimensionality Reduction (PCA & t-SNE)
pca = PCA(n_components=10, random_state=42)
pca_res = pca.fit_transform(df_log)
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
tsne_res = tsne.fit_transform(pca_res)

df_full['tSNE1'] = tsne_res[:, 0]
df_full['tSNE2'] = tsne_res[:, 1]

# 3. Create High-Resolution Multi-Panel Visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle('Tree-NEB single-nuclei RNA-Seq Analysis across Ginkgo biloba Age Cohorts', fontsize=16, fontweight='bold', y=0.98)

# Panel A: t-SNE by Cell Type
sns.scatterplot(
    data=df_full, x='tSNE1', y='tSNE2', hue='Cell_Type',
    style='Cohort', palette='Set1', alpha=0.8, s=40, ax=axes[0, 0]
)
axes[0, 0].set_title('A. Cambial Cell Type Clusters in Dimension-Reduced Space', fontsize=12, fontweight='bold')
axes[0, 0].legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=8)

# Panel B: GbKu70 & GbATG8 Quality Control Expression across Age Cohorts
df_melt = df_full.melt(
    id_vars=['Cohort', 'Cell_Type'], 
    value_vars=['GbKu70_log1p', 'GbATG8_log1p', 'GbWOX4_log1p', 'GbTPX2_log1p'],
    var_name='Gene', value_name='Log1p_Expression'
)
df_melt['Gene'] = df_melt['Gene'].str.replace('_log1p', '')

sns.boxplot(
    data=df_melt, x='Gene', y='Log1p_Expression', hue='Cohort',
    palette='Blues', ax=axes[0, 1]
)
axes[0, 1].set_title('B. Key Longevity & Stem-Cell Marker Expression Across Age Cohorts', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Log1p Normalized Expression')
axes[0, 1].legend(title='Age Cohort', fontsize=8)

# Panel C: Heterochronic Axis Trajectory (GbAIL1 & miR156 vs miR172)
sns.violinplot(
    data=df_full[df_full['Cell_Type'].str.contains('Stem')],
    x='Cohort', y='GbAIL1_log1p', palette='Greens', ax=axes[1, 0]
)
axes[1, 0].set_title('C. Heterochronic Shielding: GbAIL1 Expression in Central Cambium Stem Files', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('GbAIL1 Log1p Expression in Cambium Stem Cells')

# Panel D: Somatic Mutation Rate Accumulation by Cell Type & Cohort
sns.barplot(
    data=df_full, x='Cell_Type', y='Somatic_SNV_Count', hue='Cohort',
    palette='Oranges', ax=axes[1, 1], ci=95, capsize=0.1
)
axes[1, 1].set_title('D. Somatic Mutation Burden (SNVs) by Cell Type Across Multi-Century Lifespans', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Mean Somatic SNV Count per Cell')
axes[1, 1].set_xticklabels(
    ['Stem Cells', 'Xylem Deriv.', 'Phloem Deriv.', 'Mitotic Primed'], rotation=15
)
axes[1, 1].legend(title='Age Cohort', fontsize=8)

sns.despine()
plt.tight_layout(rect=[0, 0, 1, 0.96])

plot_out_path = '/workspace/scratch/tree_neb_snrna_analysis.png'
plt.savefig(plot_out_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved analysis plot to {plot_out_path}")

# 4. Summary Statistics Matrix
summary_stats = df_full.groupby(['Cohort', 'Cell_Type'])[[
    'GbWOX4', 'GbKu70', 'GbATG8', 'GbTPX2', 'GbAIL1', 'Somatic_SNV_Count'
]].mean().reset_index()

summary_csv_path = '/workspace/scratch/tree_neb_cohort_summary_metrics.csv'
summary_stats.to_csv(summary_csv_path, index=False)
print(f"Saved cohort summary metrics to {summary_csv_path}")

print("Pipeline execution completed successfully.")
