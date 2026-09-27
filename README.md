# Plant Meristem Longevity – Research Labs v1 to v7

An end-to-end computational biotechnology pipeline designed to evaluate meristematic stem-cell resilience, genomic stability, and longevity pathways in perennial species like *Ginkgo biloba*.

## 🔬 Project Overview

This repository contains a modular Google Colab notebook framework divided into progressive research phases:
- **Research Lab v1:** Literature evidence matrix tracking, structured Pandas data integration, distribution visualizations, and automated reporting.
- **Research Lab v2:** Advanced bioinformatics processing via Biopython (FASTA parsing, translation, Open Reading Frame scanning, restriction mapping).
- **Research Lab v3:** Structural bioinformatics pipeline utilizing Biopython (`Bio.PDB`) to fetch PDB structures (`1LCD`), extract $C_{\alpha}$ backbone coordinates, compute pairwise Euclidean distance matrices, and render heatmaps.
- **Research Lab v4:** Binary contact map generation ($8.0 \text{ \AA}$ threshold) and distance distribution statistics.
- **Research Lab v5:** Residue contact network graph construction, degree centrality scoring, and structural hub identification.
- **Research Lab v6:** Thermal flexibility and B-factor profiling (with positional deviation proxy fallback).
- **Research Lab v7:** Amino acid physicochemical composition and hydrophobic core profiling.
