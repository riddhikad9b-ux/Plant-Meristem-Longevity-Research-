# 🌱 Plant-Meristem-Longevity-Research (PDB: 1LCD)

An advanced multi-modal structural bioinformatics and thermal flexibility workspace designed for analyzing plant meristem longevity characteristics using PDB ID `1LCD`.

## 🚀 Overview
This repository features an interactive web-based dashboard built with **Python**, **Gradio**, and **Matplotlib**. It automatically parses crystallographic coordinate files from the Protein Data Bank (RCSB PDB) and computes quantitative structural metrics.

## 📊 Analytical Dashboard Tabs
* **3D Spatial View**: Maps alpha-carbon ($CA$) atomic coordinates in a 3D projection color-coded by thermal mobility (B-factor).
* **Thermal Profile (B-Factor)**: Plots sequence-level thermal fluctuations across residue indexes to differentiate rigid structural domains from flexible regulatory loops.
* **Residue Contact Network**: Computes pairwise Euclidean distance matrices to map intramolecular contacts and spatial packing.

## 🛠️ Tech Stack & Requirements
* Python 3.x
* `gradio`
* `matplotlib`
* `numpy`

## 🏃 Quick Start
To launch the interactive dashboard locally or in Google Colab:
```bash
python app_gradio.py

