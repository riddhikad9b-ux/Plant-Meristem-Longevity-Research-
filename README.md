# Plant Meristem Longevity – Research Lab v1, v2 & v3

An end-to-end computational biotechnology pipeline designed to evaluate meristematic stem-cell resilience, genomic stability, and longevity pathways in perennial species like *Ginkgo biloba*.

## 🚀 Project Overview

This repository contains a modular Google Colab notebook framework divided into progressive research phases:

- **Research Lab v1:** Literature evidence matrix tracking, structured Pandas data integration, distribution visualizations, CSV exports, and automated synthesis reporting.
- **Research Lab v2:** Advanced bioinformatics processing via Biopython (FASTA parsing, transcription/translation, Open Reading Frame scanning, restriction enzyme mapping), Random Forest machine learning classification for gene resilience markers, and an interactive IPywidgets research dashboard.
- **Research Lab v3:** Structural bioinformatics pipeline utilizing Biopython (`Bio.PDB`) to fetch PDB structures (such as `1LCD`), extract $C_\alpha$ backbone coordinate metrics, compute pairwise Euclidean distance matrices, and render publication-ready heatmaps using NumPy, Matplotlib, and Seaborn.

## 🛠️ Tech Stack & Libraries
- **Data Science:** Python, Pandas, NumPy, Matplotlib, Seaborn
- **Bioinformatics:** Biopython (`SeqIO`, `SeqUtils`, `Restriction`, `Bio.PDB`)
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Interactive UI:** IPywidgets

## 📊 Key Modules & Pipeline Stages
1. **Evidence Matrix Construction:** Multi-factor literature cataloging spanning abiotic stress signaling, tree longevity, and telomere maintenance.
2. **Sequence Processing:** Automated parsing of genomic sequences, GC-content evaluation, and translation analysis.
3. **Predictive Modeling:** Supervised classification model trained on genomic features to predict stress-responsive markers.
4. **Structural Bioinformatics:** PDB structure retrieval, atom coordinate extraction, distance matrix computation, and heatmap visualization.

## 💻 Usage
Clone the repository and open the primary `.ipynb` notebook in Google Colab or Jupyter Notebook to execute the end-to-end pipeline.
