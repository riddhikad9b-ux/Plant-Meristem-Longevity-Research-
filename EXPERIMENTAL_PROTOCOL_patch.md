# Suggested edits to EXPERIMENTAL_PROTOCOL.md

1. Section 1, line 6 — replace:
   "While computational models and sequence alignments established high structural conservation (e.g., *Ginkgo biloba* Ku70 sharing 68.4% identity and 100% basic channel residue conservation with human Ku70/XRCC6), physical bench validation is required ..."
   with:   "No Ginkgo biloba Ku70 sequence comparison with human Ku70/XRCC6 has been computed. A previously reported 68.4% identity could not be reproduced: on 2026-10-15, BLASTp (human Ku70 P12956 and Arabidopsis Ku70 NP_564012.1 against Ginkgo biloba, NCBI nr) and tblastn (WGS database JANKJI02) returned no significant similarity, while the control search (human Ku70 against Arabidopsis) returned a Ku70-like protein at about 31% identity. Whether a Ginkgo Ku70 sequence exists in other databases has not been established. Physical bench validation is required before any functional claim."
2. Section 1, line 4 — make the stage ranges consistent with the whitepaper (22-28 vs 22-34, 29-31).
3. Protocol D — the free-GFP/GFP-ATG8a western blot reports vacuolar degradation of the GFP-ATG8 fusion; it is not the same quantity as endogenous ATG8-II lipidation. Say which readout is meant, and keep the label "net autophagic flux" for assays that include a Bafilomycin A1 comparison.
4. Add a note that any files named tree_neb_* are simulated.

5. Evidence-table origin of the number: the row "Deciphering Genomic Longevity: Evolutionary Conservation of the Ku70/XRCC6 Repair Architecture" (Year: "Not in source", Source: 2) is the only citation for the 68.4% figure in the repository. A web search for that exact title found nothing; treat it as an internal or unpublished source document until it is identified.


## Update 2026-10-15 (BLAST run by the author; values read from screenshots, author to confirm)
- Control: human Ku70 (P12956, 609 aa) vs Arabidopsis thaliana nr: top hit NP_564012.1 (621 aa), 31.37% identity, 98% cover, E=5e-72.
- Human Ku70 vs Ginkgo biloba (taxid 3311) blastp nr: no significant similarity.
- Human Ku70 vs WGS JANKJI02 tblastn: no significant similarity.
- Arabidopsis NP_564012.1 vs Ginkgo biloba blastp nr: no significant similarity.
- XP_056157321.1 (suggested by another AI): not verified; not retrieved by the searches above.
Please record the RIDs (D16K1Y6E016, D16U5J48014, D17RU7RP014, D188PA6T014; expire after about 24 h) and the date in the repository.
