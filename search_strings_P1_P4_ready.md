# P1–P4: ready-to-paste search strings (Q3)

Run each string in each database separately. After each run, record in `q3_search_log.csv`: database, date, exact query as pasted, hit count, notes. Hit counts must come from the database itself. Do not estimate them.

Status: NOT YET RUN. Nothing below is a result.

## P1 (core: autophagy + ROS + WUS/CLV + meristem)
- PubMed: `(autophagy[tiab] OR "autophagic flux"[tiab]) AND (ROS[tiab] OR redox[tiab] OR "reactive oxygen"[tiab]) AND (WUS[tiab] OR WUSCHEL[tiab] OR CLV3[tiab] OR CLAVATA[tiab]) AND meristem[tiab]`
- Web of Science: `TS=((autophagy OR "autophagic flux") AND (ROS OR redox OR "reactive oxygen") AND (WUS OR WUSCHEL OR CLV3 OR CLAVATA) AND meristem)`
- Scopus: `TITLE-ABS-KEY((autophagy OR "autophagic flux") AND (ROS OR redox OR "reactive oxygen") AND (WUS OR WUSCHEL OR CLV3 OR CLAVATA) AND meristem)`
- Google Scholar: `("autophagic flux" OR autophagy) (ROS OR redox) (WUSCHEL OR CLV3 OR CLAVATA) meristem`

## P2 (temporal / stress-pattern)
- PubMed: `plant[tiab] AND (meristem[tiab] OR "stem cell niche"[tiab]) AND (autophagy[tiab] OR "autophagic flux"[tiab]) AND (ROS[tiab] OR redox[tiab]) AND (recovery[tiab] OR repeated[tiab] OR recurrent[tiab] OR continuous[tiab] OR chronic[tiab])`
- Web of Science: `TS=(plant AND (meristem OR "stem cell niche") AND (autophagy OR "autophagic flux") AND (ROS OR redox) AND (recovery OR repeated OR recurrent OR continuous OR chronic))`
- Scopus: `TITLE-ABS-KEY(plant AND (meristem OR "stem cell niche") AND (autophagy OR "autophagic flux") AND (ROS OR redox) AND (recovery OR repeated OR recurrent OR continuous OR chronic))`
- Google Scholar: `plant meristem autophagy ROS recovery repeated stress`

## P3 (computational models)
- PubMed: `("shoot apical meristem"[tiab] OR SAM[tiab]) AND (WUS[tiab] OR CLV3[tiab] OR CLAVATA[tiab]) AND (autophagy[tiab] OR ROS[tiab] OR redox[tiab]) AND (model[tiab] OR simulation[tiab] OR "dynamical system*"[tiab] OR "mathematical model*"[tiab])`
- Web of Science: `TS=(("shoot apical meristem" OR SAM) AND (WUS OR CLV3 OR CLAVATA) AND (autophagy OR ROS OR redox) AND (model OR simulation OR "dynamical system*" OR "mathematical model*"))`
- Scopus: `TITLE-ABS-KEY(("shoot apical meristem" OR SAM) AND (WUS OR CLV3 OR CLAVATA) AND (autophagy OR ROS OR redox) AND (model OR simulation OR "dynamical system*" OR "mathematical model*"))`
- Google Scholar: `"shoot apical meristem" WUSCHEL CLV3 model simulation ROS autophagy`

## P4 (time-course / recovery)
- PubMed: `(WUSCHEL[tiab] OR WUS[tiab]) AND (CLAVATA3[tiab] OR CLV3[tiab]) AND ("oxidative stress"[tiab] OR redox[tiab] OR autophagy[tiab]) AND ("time-course"[tiab] OR recovery[tiab] OR "stress adaptation"[tiab])`
- Web of Science: `TS=((WUSCHEL OR WUS) AND (CLAVATA3 OR CLV3) AND ("oxidative stress" OR redox OR autophagy) AND ("time-course" OR recovery OR "stress adaptation"))`
- Scopus: `TITLE-ABS-KEY((WUSCHEL OR WUS) AND (CLAVATA3 OR CLV3) AND ("oxidative stress" OR redox OR autophagy) AND ("time-course" OR recovery OR "stress adaptation"))`
- Google Scholar: `WUSCHEL CLAVATA3 oxidative stress redox autophagy recovery time-course`

## Notes
- PubMed syntax above was written from standard field-tag rules and has not been executed. If PubMed shows a query-translation warning, record it in the log.
- Google Scholar has no hit-count guarantee. Record only the first 100 results screened.
- Also do citation tracking (backward and forward) from the closest papers, per `search_protocol_q3.md`.
- Allowed wording only after all of this is done: "not identified in the reviewed literature (searched <dates>)". Never "does not exist".

## Log columns to fill (append to q3_search_log.csv)
search_id, database, search_date, exact_query, hit_count_from_database, screened_title_level, full_text_reviewed, relevant_or_related_titles, exclusion_reasons, search_limitations
