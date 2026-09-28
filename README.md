## Research Matrix & Literature Database

This repository includes an automated research matrix tracking key molecular mechanisms of plant meristem longevity and cellular resilience across multiple studies.

### Core Pathways Tracked:
* **Hormone Signaling & Stem Cell Maintenance:** Cytokinin signaling (`AHK/WUS`) and feedback loops.
* **Stress Memory & Signaling:** Heterotrimeric G-protein signaling in abiotic stress responses.
* **Genome Stability & DNA Repair:** Ku70 and NHEJ components in long-lived perennials like *Ginkgo biloba*.
* **Proteostasis & Autophagy:** `ATG8` dynamics and basal autophagy flux.
* **Epigenetic Regulation:** DNA methylation and Polycomb group histone modifications.
* **Stem Cell Niches:** `CLV3/WUS` negative feedback regulation.
* **Antioxidant Defense:** ROS scavenging pathways (`SOD`/`CAT`) in woody perennials.
* **Somatic Mutation Control:** Replication fidelity and mutation load tracking across centuries in trees like *Quercus robur*.

### Python Integration
A helper function (`add_research_paper`) is provided in the analysis pipeline to dynamically append new literature entries with standardized fields (DOI, pathways, experimental methods, limitations, and confidence labels) directly into `research_matrix.csv`.

