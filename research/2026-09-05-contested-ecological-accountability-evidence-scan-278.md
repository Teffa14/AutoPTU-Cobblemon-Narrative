# Contested ecological accountability evidence scan — Pass 278

Status: RESEARCH / PROVENANCE ONLY. No canon effect.
Date: 2026-09-05

Purpose

Research how Ouros can handle disagreement about whether a delegated ecological task was performed correctly when the evidence itself is incomplete, method-sensitive, contested or interpreted differently. This pass continues Pass 277 without duplicating the generic adjudication/review layer.

Repository cross-check

- `design/ecological-delegated-authority-accountability-contract.md` already separates process compliance from ecological outcome and allows corrective action, suspension and revocation.
- `design/adjudication-hearing-decision-review-continuity-extension.md` already owns submitted matters, institutional decisions, review, stays, remand, amendment and reversal where a canon institution supports them.
- Therefore this pass must not create a second court/appeal lifecycle. It supplies an ecology-specific evidence-dispute packet that those layers can consume.
- `design/ouros-source-authority-and-species-policy.md` remains controlling: PTU is the mechanical baseline; Caelo/Kairos are comparative; Minecraft presentation cannot manufacture mechanical or institutional truth.
- The repository contains a local Kairos source pack but no local Caelo source pack. No Caelo rule is inferred or adopted here.

Public-source findings

1. Adaptive management depends on monitoring, evaluation and adjustment, but disagreement can concern both ecological models and management objectives. USGS work explicitly treats uncertainty and disagreement about objectives as separate from uncertainty about ecological dynamics.
   Source: Byron K. Williams, “Reducing uncertainty about objective functions in adaptive management,” USGS publication record, 2012.
   https://www.usgs.gov/publications/reducing-uncertainty-about-objective-functions-adaptive-management

2. Monitoring and auditing should not be collapsed. A literature review indexed by EPA distinguishes follow-up monitoring from auditing and notes that confusing their roles can weaken environmental management. For Ouros, an observation that a field condition changed is different from an audit conclusion about whether a delegate complied with an obligation.
   Source: Viegas et al., “A review of environmental monitoring and auditing in the context of risk,” Journal of Cleaner Production, 2013, EPA HERO record.
   https://hero.epa.gov/reference/6795328/

3. Adaptive-management accountability improves when trigger conditions and review points are specified in advance. Conservation Biology research found disputes often center on who designed, performed, interpreted and funded monitoring, as well as baseline selection and precaution level. Ouros should therefore preserve method ownership and interpretation provenance instead of storing one final compliance boolean.
   Source: “Decision Triggers in Adaptive Management,” Conservation Biology.
   https://conbio.onlinelibrary.wiley.com/doi/abs/10.1111/j.1523-1739.2012.01915.x

4. IUCN grievance processes separate the complaint from the project record and allow further review when the affected party remains unsatisfied. The reusable design lesson is escalation with preserved prior records, not importing IUCN procedure into Ouros.
   Sources:
   https://iucn.org/about-iucn/accountability-and-reporting/project-accountability/environmental-and-social-management-system
   https://iucn.org/our-work/region/asia/our-work/regional-projects/critical-ecosystem-partnership-fund-cepf-indo-2

5. Recent conservation-governance research finds that procedural equity depends on voice, transparency, trustworthiness and treatment, while co-management can improve or worsen equity depending on institutional design and participation. This supports recording who could challenge an interpretation and whether relevant evidence was available, without asserting that disagreement itself makes the ecological conclusion false.
   Sources:
   Gammage & Gurney, “Equity Through Co-Management in Small-Scale Fisheries—A Review,” Fish and Fisheries, 2025.
   https://onlinelibrary.wiley.com/doi/abs/10.1111/faf.12889
   “Preferences for fair decision-making principles in marine conservation,” Biological Conservation, 2026.
   https://doi.org/10.1016/j.biocon.2026.111869

6. Adaptive monitoring changes as questions, methods and conditions change. This means later evidence can legitimately be stronger than earlier evidence without retroactively fabricating that the earlier observer acted wrongly.
   Source: McCord & Pilliod, “Adaptive monitoring in support of adaptive management in rangelands,” USGS, 2022.
   https://www.usgs.gov/publications/adaptive-monitoring-support-adaptive-management-rangelands

7. USGS adaptive-management literature also emphasizes that complex ecological systems contain irreducible uncertainty and that management under uncertainty can fail when process design is weak. Ouros should allow a review to end as `EVIDENCE_REMAINS_INCONCLUSIVE` rather than forcing every dispute to identify a winner.
   Source: Allen & Gunderson, “Pathology and failure in the design and implementation of adaptive management,” 2011.
   https://www.usgs.gov/publications/pathology-and-failure-design-and-implementation-adaptive-management

Pokémon / TTRPG inspiration

A currently advertised PTU campaign, “The Social Ecology of Kanto,” explicitly uses relationships between society and nature as a mystery engine. Only the high-level structure is useful: social institutions and ecological observations can produce mysteries whose resolution requires both field evidence and human interpretation. No characters, factions, setting details, political claims, dialogue or plots are copied.
Source: StartPlaying campaign listing.
https://startplaying.games/adventure/cm9ydhbid00412xulbu7lzufh

Reusable Ouros structures

- One evidence item can support multiple interpretations without duplicating ecological truth.
- Method disagreement should point to the exact observation protocol, semantic window and provenance.
- A reviewer may find the evidence sufficient, insufficient, methodologically incomparable or still disputed.
- A challenge should not automatically stay, reverse or erase a delegation decision. Those effects belong to the governing decision/review procedure.
- Later stronger evidence may supersede an interpretation while preserving the historical record.
- A missing record can justify process concern without proving ecological harm or bad faith.
- An ecological outcome can remain uncertain even after a procedural dispute is resolved.

Candidate narrative use

A temporary Sendero stewardship assignment produces two observation logs. One reviewer says the marker-maintenance obligation was satisfied; another says the evidence window cannot establish that because the inspection occurred after a visibility change. The player can locate the original observations, reproduce the method, obtain an independent comparison or discover that the dispute cannot be resolved from surviving evidence. Any formal consequence is routed through existing authority/adjudication contracts.

Canon classification

CANON-APPROVED carried forward:
- existing Marea/Sendero geography and the authoritative Fletchling population remain unchanged;
- existing Ouros/PTU/Minecraft authority boundaries remain unchanged.

PROPOSED:
- ecology-specific evidence contest packet;
- interpretation lineage and method-comparability states;
- narrow audit outcome that can feed Pass 277 or the generic adjudication layer.

UNCERTAIN:
- which future canon institution, if any, reviews stewardship evidence;
- whether any canon actor has a formal appeal right;
- exact notice, hearing, stay or remedy procedures;
- whether player organizations may ever become delegates.

Mechanical rule adoption

None. No PTU, Caelo or Kairos combat rule is introduced. The reduced loop has zero AutoPTU dependency. Mechanically rich enforcement remains capability-gated by the engine readiness snapshot.