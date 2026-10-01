# Plant Meristem Longevity Research Lab: Experimental Validation & Protocol Blueprint

## 1. Overview & Project Transition
This document outlines the experimental validation protocols designed to transition our findings from **computational discovery** (Stages 1–21.1) and **literature verification** (Stages 22–28) into **empirical hypothesis testing** (Stages 29–31). 

While computational models and sequence alignments established high structural conservation (e.g., *Ginkgo biloba* Ku70 sharing 68.4% identity and 100% basic channel residue conservation with human Ku70/XRCC6), physical bench validation is required to test whether meristematic quality control mechanisms causally mitigate stem-cell exhaustion.

---

## 2. Core Experimental Protocols

### Protocol A: *Arabidopsis thaliana* SAM Culture & Growth Conditions
* **Plant Material:** *Arabidopsis thaliana* (ecotype *Landsberg erecta* [WT] and *clv3-2* mutant lines).
* **Media Composition:** Half-strength Murashige and Skoog (1/2 MS) medium containing 0.8% (w/v) phytoagar, 1.0% (w/v) sucrose, pH 5.7.
* **Environmental Parameters:** Growth chamber set to 22°C, 60% relative humidity, under a 16h light / 8h dark photoperiod (120 µmol m⁻² s⁻¹ photosynthetic photon flux density).
* **Shoot Apex Enrichment:** At 9 days post-germination, micro-dissect enriched shoot apices (SAM dome + P1–P4 leaf primordia) under a stereomicroscope to exclude mature hypocotyl and cotyledon tissues.

### Protocol B: Controlled Abiotic Stress Induction Time-Courses
* **Salinity Challenge:** Transfer 9-day-old seedlings onto 1/2 MS plates supplemented with 0 mM, 100 mM, 150 mM, or 200 mM NaCl.
* **Time-Course Sampling:** Harvest enriched shoot apices at t = 0h, 3h, 6h, 12h, 24h (acute stress phase) and t = 48h post-washout on standard 1/2 MS media (recovery phase).
* **Downstream Assays:** Split harvested apices into three technical replicates for qRT-PCR (measuring *TPX2*, *CYC1BAT*, *ENODL14*, *ENODL15*, *WUS*, *CLV3*), ROS quantification, and autophagic flux imaging.

### Protocol C: Reactive Oxygen Species (ROS) Fluorogenic Assays
* **Fluorogenic Staining:** Incubate dissected shoot apices in 10 µM H2DCFDA (2',7'-dichlorodihydrofluorescein diacetate) in 10 mM Tris-HCl (pH 7.4) for 30 minutes in the dark at room temperature to detect total intracellular ROS (superoxide and H₂O₂).
* **Confocal Quantification:** Image stained apices using Leica SP8 confocal microscopy (excitation 488 nm, emission 515–545 nm).
* **Densitometry:** Quantify mean fluorescence intensity across Central Zone (CZ) vs. Peripheral Zone (PZ) stem-cell niches using ImageJ/Fiji.

### Protocol D: GFP-ATG8a Autophagic Flux & Vacuolar Clearance Imaging
* **Transgenic Lines:** *Arabidopsis* lines expressing *pUBQ10::GFP-ATG8a*.
* **Vacuolar Blockade:** Treat dissected apices with 1 µM Bafilomycin A1 (or DMSO control) in liquid MS medium for 4 hours during salt/thermal stress to inhibit vacuolar V-ATPase and block autophagosome degradation.
* **Western Blot Quantification:** Extract total protein, separate on 12% SDS-PAGE, and blot with anti-GFP antibody. Quantify the accumulation ratio of free GFP (cleaved in vacuole) relative to intact GFP-ATG8a to establish net autophagic clearance flux ($\Delta\text{ATG8-II}$).

### Protocol E: WUS–CLV Spatial Reporter Tracking
* **Reporter Lines:** Dual-reporter line *pWUS::GFP / pCLV3::mCherry*.
* **Live Confocal Microscopy:** Mount intact shoot apices in custom microfluidic chambers under constant media perfusion.
* **Spatial Mapping:** Track mCherry (CLV3 in L1/L2 CZ) and GFP (WUS in L3 OC) signal domain boundaries across baseline, 24h salt shock, and 48h recovery phases to test spatial feedback stability under abiotic stress.

---

## 3. Experimental Results Data Schema (`experimental_results_matrix.csv`)

To ensure reproducible downstream analysis, all physical bench experiments must be logged into `experimental_results_matrix.csv` using the following standardized schema:

| Column Name | Data Type | Description | Example / Range |
| :--- | :--- | :--- | :--- |
| `experiment_id` | String | Unique protocol run identifier | `EXP-2026-SAM-001` |
| `genotype` | String | Genetic background | `WT_Ler`, `clv3-2`, `pUBQ10::GFP-ATG8a` |
| `treatment_type` | String | Stress or control condition | `Control_0mM`, `NaCl_200mM`, `BafA1_1uM` |
| `timepoint_hours` | Float | Exposure duration | `0.0`, `3.0`, `6.0`, `12.0`, `24.0`, `48.0` |
| `tissue_type` | String | Dissected tissue domain | `Enriched_SAM`, `Central_Zone`, `Leaf_P1-P4` |
| `target_gene_marker` | String | Molecular target measured | `TPX2`, `CYC1BAT`, `ENODL14`, `GFP-ATG8a`, `WUS` |
| `relative_expression_fold` | Float | Normalized expression (qRT-PCR vs. ACT2) | `0.45`, `3.21`, `12.80` |
| `ros_fluorescence_au` | Float | H2DCFDA mean signal intensity | `142.5` |
| `autophagic_flux_delta` | Float | Net GFP clearance ratio ($\Delta\text{ATG8-II}$) | `2.84` |
| `evidence_tier` | String | 4-Tier taxonomy classification | `🟢 Established`, `🔵 Supported`, `🟡 Hypothesis` |
| `replicate_number` | Integer | Biological replicate ID | `1`, `2`, `3` |
