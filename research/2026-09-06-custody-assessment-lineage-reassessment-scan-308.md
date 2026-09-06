# Custody assessment lineage and reassessment scan — pass 308

Status: RESEARCH / PROVENANCE ONLY / NOT CANON
Date: 2026-09-06

This pass researches how a persistent investigation can change its supported conclusion after new documentation appears while retaining what was supportable at earlier times. It does not import real-world evidentiary law into Ouros and does not establish any Ouros institution, profession, legal standard, Skill check or PTU mechanic.

## Repository gap checked before research

Passes 306–307 already model physical-evidence custody, integrity assessment, provenance-backed support and durable checkpoint restoration. The existing Pass 307 contract explicitly preserves old assessments as historical state and names the missing `supersedes_assessment_id` relation as a future seam. Repository search found no existing assessment-supersession implementation. Pass 308 therefore extends lineage rather than creating a second custody system.

## External sources and reusable lessons

NIST OSAC Lexicon, “Amended Report,” added 2023 and a second discipline entry added 2025: an amended report documents modifications that affect or correct an earlier result or interpretation. Reusable structure: a later conclusion should identify the earlier issued conclusion it changes instead of making the earlier state disappear. Source: https://www.nist.gov/glossary-term/18416 and https://www.nist.gov/glossary-term/42561

NIST, OSAC 2024-S-0016, Standard for Case File Management and Reporting in Forensic Anthropology, published in 2026: supplemental reports document information that becomes available after an earlier report; amended reports reference the previously issued report and clearly indicate modifications. Preliminary results can also be identified as such because later finalized findings may differ. Reusable structure: explicit predecessor reference, temporal ordering and retained distinction between earlier and later findings. Source: https://www.nist.gov/document/osac-2024-s-0016-standard-case-file-management-and-reporting-forensic-anthropology-version

National Institute of Justice, “Amending Reports,” created 2023: additional evidence can lead to supplemental reporting, while corrections or clarification can lead to amended reporting, with the requesting party informed and the reason explained. Reusable structure: new evidence can trigger a new assessment event and subsequent communication rather than retroactive memory replacement. Source: https://nij.ojp.gov/nij-hosted-online-training-courses/law-101-legal-guide-forensic-expert/report-writing-and-supporting-documentation/amending-reports

Nintendo, Pokémon Pokopia overview, 2025–2026: the game structures progression around restoring a damaged world, improving habitats and returning to a landscape whose available inhabitants and uses change with environmental work. Reusable structure: a previously visited place can become narratively legible in a new way after durable world-state change. Pass 308 uses only the revisit/state-change pattern; no characters, setting events, dialogue, maps or plot are copied. Source: https://www.nintendo.com/au/news-and-articles/catch-a-cosy-new-video-about-pokemon-pokopia/

StartPlaying, “PokeU Panic!”, publicly listed PTU campaign, accessed 2026-09-06: the campaign combines ordinary campus life, friendships, rivalries, battles, disappearances and a larger investigation. Reusable structure: an investigation can coexist with recurring social routines and reveal itself over multiple sessions instead of resolving every clue immediately. No campaign characters, university, conspiracy details or authored plot are imported. Source: https://startplaying.games/adventure/cmr6r2xws01ecl604wm1bf5qr

## Transformation into Ouros design

A custody assessment becomes an immutable historical statement of what one investigator could support at one semantic time. A later assessment may explicitly supersede it only when it concerns the same investigator and same evidence artifact and does not travel backward in semantic time. Supersession means “this later assessment revises the investigator’s supported conclusion.” It does not mean the earlier assessment never existed, that every other NPC knows the new result, that the later result is canonical truth, or that custody integrity establishes substantive guilt, sabotage, scientific validity or legal admissibility.

This preserves the distinction already established across Ouros between canonical world fact, private evidence, actor knowledge, interpretation, publication and social consequence. Communication of a changed assessment remains a separate delivery problem.

## PTU/Caelo boundary

The project README requires exact mechanics to come from the supplied PTU Core Rulebook, Pokédex material, Caelo Player’s Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List plus current AutoPTU evidence. Nothing in the public forensic sources is treated as PTU authority. Pass 308 does not define a Skill, DC, Trainer Feature, Pokémon sensory capability, item effect, investigation roll, evidence bonus or legal procedure.

## Originality boundary

Only abstract structures were retained: linked revisions, later evidence, revisiting changed places and long-running investigations embedded in ordinary world activity. Protected prose, named story characters, distinctive mysteries, maps, encounter scripts and plots remain external-source material.
