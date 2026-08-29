# Ouros Community Health Surveillance & Cluster Investigation Research — Pass 117

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-28

## Research question

What reusable structures can Ouros borrow from Pokémon fiction, Pokémon tabletop/community material, public-health investigation practice and adjacent game-design sources to support community health signals, clusters, exposure investigations and recovery without inventing disease mechanics, medical authority, contagion rules or setting institutions?

This pass deliberately separates research provenance from canon. External sources inspire architecture and story grammar only. PTU/Caelo and the project engine remain authoritative for actual mechanical health, status, damage, treatment and battle behavior.

## Repository gap found before research

The complete repository tree was inspected before writing and was not truncated. Existing systems already cover substantial adjacent territory:

- `care-recovery-welfare-layer.md` owns individual care cases, observations, diagnosis/treatment boundaries, facility capacity and aggregate health signals;
- `batch-traceability-recall-quarantine-extension.md` owns product/batch holds, quarantine, distribution trace, recall/correction and disposition handoffs;
- `crisis-rescue-recovery-layer.md` owns broad emergencies, evacuation, shelters, response coordination and recovery projects;
- food, wastewater, drinking-water, pollution, cold-chain, workplace-safety, housing, schools/community institutions and communications layers own their respective operational facts;
- `case-authority-custody-layer.md` owns formal evidence/allegation/authority workflows;
- ecology systems own wild-Pokémon population observations and environmental interpretation.

The missing layer is the evidence bridge between many separate health-relevant observations and downstream owner systems. Care can say several similar cases appeared. A clinic, shelter, workplace, school, market, wildlife team or laboratory can each have partial evidence. Nothing currently owns the persistent cross-source question: are these reports meaningfully related, what scope is being investigated, what is still unknown, which definitions changed, which exposure hypotheses exist, which actors have been notified, and which downstream systems must decide their own actions?

That gap is suitable for a continuity layer because it creates investigations and consequences without fabricating mechanics.

## Source 1 — Pokémon: Pokérus

Source:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9rus

Pokérus is useful mainly as a guardrail. In the games it is a specific virus-like Pokémon mechanic with its own infection/spread/recovery behavior. It is explicitly distinct from ordinary status conditions and is not removed by normal Pokémon Center/status-healing behavior. Different generations also alter whether it generates, spreads or is visibly represented.

Reusable high-level lesson:

A Pokémon-world health phenomenon can have its own identity, detection state, persistence and presentation without being reducible to a generic status label or ordinary healing action.

Ouros transformation:

- never treat `ill`, `infected`, `exposed`, `Poisoned`, `Pokérus`, `injured` and `needs care` as synonyms;
- preserve the governing source for any named condition;
- let a care provider observe or classify a phenomenon without automatically changing tactical status;
- preserve historical state even if later presentation changes;
- do not extrapolate Pokérus transmission rules to other pathogens, species or regions.

Rejected imports:

- Pokérus probabilities;
- adjacency-based spread;
- day counts;
- EV benefits;
- immunity rules;
- PC-storage behavior;
- any inference that all Pokémon diseases work like Pokérus.

## Source 2 — Pokémon illness as a broad narrative category

Source:
https://bulbapedia.bulbagarden.net/wiki/Illness

Pokémon media contains many unrelated illness stories rather than one universal disease subsystem. Their causes, subjects, symptoms and resolutions differ across games, animation and manga.

Reusable high-level lesson:

Narrative health events should begin with specific observations and source-bounded claims rather than a generic `disease_level` or universal pathogen model.

Ouros transformation:

A regional story may preserve:

- repeated similar observations;
- a named condition only when canon establishes it;
- an uncertain cluster with no final cause;
- a noninfectious common exposure;
- a Pokémon-only, human-only or mixed set of observations when a governing source supports that scope;
- recovery without identifying a definitive source.

The system should support uncertainty as a valid ending.

## Source 3 — Pokémon Adventures hospital/Pokérus recognition

Source:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9rus

The Pokérus material also contains a narrative structure in which a phenomenon is recognized in a care/hospital context after affected Pokémon have already been present there.

Reusable high-level lesson:

Detection time, probable onset time, first care encounter and later classification time are distinct chronology points.

Ouros transformation:

A clinic can discover that several prior cases share an observation pattern. That discovery may revise a cluster backward in time without rewriting the original records as though staff knew the connection earlier.

This is important for mysteries and institutional memory.

## Source 4 — Pokémon tabletop community search

Public searches across Pokémon Tabletop community discussions were performed for disease, outbreak, infection and quarantine campaign material.

No disease-specific PTU community source located in this pass was strong enough to establish a reusable mechanical rule. One surfaced discussion was explicitly from the wrong tabletop RPG, so it was rejected rather than treated as PTU evidence.

Useful general community evidence remains the existing project corpus: Pokémon tabletop campaigns work best when world premise, player interests and the chosen system's actual rules stay aligned. Health-investigation material therefore belongs primarily in world-state, investigation, care and social play unless an exact PTU/Caelo mechanic is verified.

Research outcome:

No community homebrew disease rule is imported.

## Source 5 — CDC: cluster versus outbreak and case definitions

Source:
https://www.cdc.gov/urdo/php/surveillance/outbreak-case-definitions.html

The CDC distinguishes a cluster from an outbreak and emphasizes a case definition scoped by person, place, time and observable/clinical criteria.

Reusable structural lessons only:

- a cluster can be an unusual aggregation that merits investigation before the cause is known;
- a case definition is an investigation tool and can be revised;
- scope dimensions matter;
- classification should be reproducible rather than intuitive;
- a cluster does not by itself establish common cause or transmission.

Ouros transformation:

Use a versioned `working_case_definition` that records inclusion/exclusion criteria and evidence sources. Classification under that definition remains separate from diagnosis and mechanical health state.

Rejected imports:

- real disease thresholds;
- jurisdiction-specific definitions;
- clinical criteria;
- laboratory procedures;
- real-world outbreak policy.

## Source 6 — CDC: case surveillance

Source:
https://www.cdc.gov/nndss/what-is-case-surveillance/

Case surveillance aggregates information from local providers and institutions to detect patterns and support public-health action. The real system also demonstrates that surveillance can include infectious and noninfectious conditions.

Reusable structural lessons:

- surveillance is a network of reports, not omniscience;
- source institutions retain important context;
- standardization helps compare observations across locations and time;
- aggregate analysis can expose a shared pattern without exposing every private patient record;
- surveillance can apply to noninfectious exposure as well as infectious disease.

Ouros transformation:

Community health signals can arise from care facilities, shelters, workplaces, schools, environmental systems, wildlife observations, food systems or authored research programs. The layer stores only the minimum evidence needed for the investigation and references protected source records rather than copying private case content into public world state.

## Source 7 — CDC foodborne outbreak investigation

Source:
https://www.cdc.gov/foodborne-outbreaks/outbreak-basics/investigation-steps.html

The investigation process is dynamic. Detection, defining/finding cases and identifying commonalities can overlap rather than progressing through a perfectly linear quest chain.

Reusable lesson:

A strong investigation system should support parallel evidence gathering and revision.

Ouros transformation:

Players or NPC institutions may simultaneously:

- verify reports;
- compare timelines;
- inspect an environment;
- trace a batch through the existing Batch Traceability layer;
- interview affected actors with appropriate privacy/consent rules;
- compare wildlife or infrastructure observations;
- issue limited precautionary notices without declaring a cause.

The graph can converge, branch or close with insufficient evidence.

## Source 8 — WHO contact-tracing guidance

Source:
https://www.who.int/publications/i/item/9789240102965

The WHO guideline separates case investigation from contact tracing and treats contact identification, notification, follow-up and release as separate operations.

Reusable structural lesson:

Even when a canon health event includes person-to-person or Pokémon-to-Pokémon transmission, `contact identified`, `exposure supported`, `notification delivered` and `case classified` are different facts.

Ouros transformation:

If an authored condition has verified transmission rules, the narrative layer may preserve exposure/contact records and delivery evidence. It must not infer exposure from simple proximity or use Minecraft entity distance as a disease engine.

Rejected imports:

- real contact-distance/time rules;
- real disease-specific monitoring periods;
- quarantine durations;
- treatment/prophylaxis guidance;
- legal authority.

## Source 9 — investigation uncertainty and changing scope

Sources:
https://www.cdc.gov/urdo/php/surveillance/outbreak-case-definitions.html
https://www.cdc.gov/foodborne-outbreaks/outbreak-basics/investigation-steps.html

A useful narrative consequence of versioned definitions is that two correct reports can disagree because they were created under different scopes or at different times.

Ouros can use this for mysteries without manufacturing deception.

Example structure:

- clinic A reports four cases under definition v1;
- a later environmental clue causes definition v2 to exclude one and include two older cases;
- a newspaper still quotes the earlier count;
- a workplace reports only its own employees;
- a wildlife team describes a similar observation in Pokémon but has not established the same cause.

The mystery is resolved by provenance and scope, not a hidden truth score.

## Cross-source design synthesis

The strongest reusable structures from this pass are:

1. health surveillance begins with observations and signals, not a predetermined disease;
2. clusters, outbreaks, diagnoses and causes must remain separate concepts;
3. working definitions and scope can change while earlier records remain historically correct;
4. infectious and noninfectious patterns can use the same evidence architecture without sharing transmission rules;
5. individual care records should stay private while aggregate signals can become public or institution-visible;
6. contact/exposure logic must exist only when a governing condition defines it;
7. interventions and notices can occur under uncertainty without becoming proof of cause;
8. downstream systems keep their own authority;
9. investigation can close as unresolved, partially resolved or split into multiple causes;
10. later seasons can reuse old cluster records, changed procedures, altered routines and public memory.

## Narrative opportunities for Ouros

Potential situation families, all NON-CANON until approved:

- several clinics observe the same unusual but nonspecific presentation;
- a shelter reports similar symptoms after a utility outage, while the source remains unknown;
- Pokémon and people using the same route show different observations that may or may not share an exposure;
- a market product is suspected, then Batch Traceability shows the cases do not share a batch;
- a workplace cluster points toward ventilation, water, food, stress, a chemical exposure or unrelated causes; the investigation must not assume infection;
- an old outbreak file becomes relevant when a new cluster uses the same place but not necessarily the same cause;
- a temporary testing/observation site becomes a long-term community institution;
- public rumor attributes illness to a species seen nearby while evidence remains absent;
- a Pokémon Center notices a pattern but cannot legally/technically resolve the underlying cause alone;
- a no-new-reports period is mistaken publicly for formal closure even though follow-up remains open.

## Privacy and social guardrail

Health investigation can easily become intrusive if every actor record becomes globally visible.

Research therefore supports a strict separation between:

- protected source records;
- investigation-only identifiers;
- institution-internal aggregates;
- public notices;
- public rumor;
- canon facts.

Player access must depend on role, consent, authority and scenario design. The system should not reward unauthorized reading of private health data unless an authored story explicitly makes that misconduct part of the narrative and downstream consequences.

## PTU/Caelo cross-check result

The existing internal source scan remains controlling. It proves that PTU/Caelo can give specific locations or mechanics explicit environmental effects. It does not establish a universal epidemiology system.

This pass found no project evidence authorizing generic rules for:

- disease transmission by adjacency;
- infection rolls;
- incubation periods;
- symptom progression;
- quarantine duration;
- automatic Poison or other status from illness/exposure;
- automatic cure at a Pokémon Center;
- immunity by Pokémon Type;
- species-level disease sensing;
- Trainer Feature-based diagnosis or treatment outside exact rule support;
- environmental contamination as a battle hazard without an exact governing rule.

All remain UNKNOWN until source and engine evidence exist.

## Battle implementation implications

Most community-health investigation content should remain world-state/social/investigation play.

Mechanically rich encounters become relevant only when a separate active threat occurs around a health operation, for example:

- protecting evacuation from a temporary assessment site;
- clearing access to a field observation station;
- securing a records/sample handoff after staff have withdrawn.

No encounter should weaponize illness by default.

Any version involving exposure zones, dynamic contamination, status application, delayed symptom effects, protective interrupts or active treatment inside battle depends on the exact engine families required by those mechanics.

## Minecraft/Cobblemon guardrail

Minecraft/Cobblemon may present:

- clinics and temporary observation sites;
- signage and notices;
- queue/routine changes;
- masks or protective props if canon authorizes them;
- sample/storage props;
- blocked rooms;
- NPC and Pokémon movement;
- sounds, particles and UI;
- persistent location changes after an event.

It may not infer infection from entity proximity, apply PTU status because a particle touched an entity, decide who is a case, calculate transmission through chunk co-presence, cure a condition through a visual interaction or use Cobblemon battle state as health authority.

Ouros owns world facts and investigation records. AutoPTU owns tactical battle facts. The adapter presents authoritative state.

## Research exclusions

This pass does not reproduce protected dialogue, plots or distinctive characters. It does not import real-world medical procedures, thresholds or disease-control policy into the setting. Public-health sources were used only to derive robust state boundaries, provenance practices and uncertainty-aware investigation grammar.

No canon institution, pathogen, outbreak history or regional health law is established here.

## Recommended implementation direction

Create a proposed `community-health-surveillance-cluster-investigation-continuity` layer whose job is evidence continuity rather than medicine. It should consume protected/aggregate signals from existing systems, maintain versioned investigation scope, preserve uncertainty and issue handoffs to the systems that actually own treatment, environment, products, operations, crisis coordination or public notice.

Mechanically rich encounters should ship with reduced static variants until the exact missing tactical families are verified.