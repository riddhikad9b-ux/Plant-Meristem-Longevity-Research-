# Dossier corrections (find -> replace)

Applies to `ginkgo_full_research_master_dossier` (3-page and 4-page versions). The PDF source is yours, so these are edits to apply there. Items marked [YOU] need information only you have.

## A. Header and abstract
| Find | Replace |
|---|---|
| `Budget: ,005,000 USD (3 Years)` | `Budget: $1,005,000 USD (3 Years)` [YOU: confirm the figure; the dollar signs were lost when the file was generated, so check every amount] |
| `Utilizing a strict 4-Tier Evidence Evaluation Taxonomy, we systematically dissect` | `Using a 4-tier evidence taxonomy, we organise` |
| `Ku70/80 scaffold sharing 68.4% identity with human XRCC6` | `Ku70/80 scaffold (Ginkgo–human Ku70 similarity not computed; earlier 68.4% figure unverified and excluded)` |
| `complete, audited scientific synthesis` | `AI-assisted scientific synthesis (revised draft; citations being verified)` |
| `primary-literature verification` | `primary-literature review (in progress; no reference list in this document)` |

## B. Evidence-tier text
| Find | Replace |
|---|---|
| `Established Evidence (8 Steps) (proven in model plants)` | `Established Evidence (evidence reported in model plants; tier assigned per claim, see matrix)` |
| `all 12 core biological mechanisms are classified into a rigorous 4-tier taxonomy` | `the 12 mechanisms are classified using a 4-tier taxonomy; several steps carry two tiers` |
| Step 5 tier `Established / Supported` | `Candidate (in silico comparison only; no Ginkgo experiment)` |
| Step 10 tier (`Established / Hypothesis`) | `Not applicable (method step, not a biological claim)` |
| Steps 6, 7, 10 shown as counted in "Established (8)" | Report the tier per claim and drop the "8 steps" count, or state which part of each step is Established and which part is Candidate |

## C. Ku70 and the "Proof" wording
| Find | Replace |
|---|---|
| `Bioinformatic Proof: Present the 68.4% pairwise sequence identity ...` | `Remove the 68.4% figure. State: Ginkgo Ku70 similarity not computed; BLAST on 2026-10-15 found no Ginkgo Ku70 record in NCBI nr/WGS` |
| `Sequence alignment reveals that Ginkgo biloba Ku70-like protein shares 68.4% sequence identity, 82.1% chemical similarity, 98% query coverage, and 100% preservation ...` | `Remove the 68.4%, 82.1%, 98% and 100% figures. State: a Ginkgo–human Ku70 comparison has not been computed; BLAST on 2026-10-15 found no Ginkgo Ku70 record in NCBI nr or the searched WGS database.` |
| `This preformed ring scaffold threads double-strand DNA breaks ...` | `By homology, a Ku70/80 ring scaffold is expected to ...` |

## D. Simulated data
| Find | Replace |
|---|---|
| `/outputs/ - Computational metrics (tree_neb_cohort_summary_metrics.csv, tree_neb_snrna_counts_summary.csv)` | `/outputs/ - SIMULATED demonstration outputs (np.random, seed 42); cohort differences are pre-programmed inputs, not findings` |
| `single-nuclei Python pipeline (analyze_tree_neb.py)` | `single-nuclei analysis pipeline demonstrated on simulated data (analyze_tree_neb.py)` |

## E. Budget and scope
| Find | Replace |
|---|---|
| Section 4 table (amounts such as `10k`, `0,000`, `00,000`) | [YOU] rebuild with literal $ amounts that sum to the total; reconcile with the other budget versions (PDF 450/300/200/55; slides 380/325/185/115) |
| Section 5 item 4: `official 2nd-Year B.Tech Biotechnology Mini-Project` alongside a $1.005M budget | [YOU] separate the two purposes: a mini-project scoped to what a student can do (literature review, computational framework, a small simulated demonstration) and a separate grant concept |
| Footer `Full Research Details for Claude Verification` | remove |

## F. Add
- AI-assistance disclosure (Gemini Notebook / NotebookLM for literature mapping and drafting; Python in Google Colab).
- A reference list for the 19 priming genes, ~40-fold WUS induction, clv3-2 salt result, and 121 priming genes, each with author, year and DOI.
- Rebuild the Section 2 matrix table (it renders as dots) and strip stray Markdown symbols.


Note 2026-10-15: BLAST (control human vs Arabidopsis Ku70 about 31% identity; no Ginkgo Ku70 hit) means the 68.4% figure should not appear as a result anywhere. See claim register M40.
