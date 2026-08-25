# Pass 159 — Plant Pathology, Disease Surveillance & Diagnostic Uncertainty Scan

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-08-24

## Repository audit and scope decision

Pass 159 is deliberately a protocol extension, not a new high-level plant authority.

Existing authorities inspected before writing:

- `design/integrated-pest-management-crop-pressure-layer.md` owns crop-pressure management, scouting, thresholds and intervention decisions.
- `design/decomposition-fungi-deadwood-nutrient-cycling-layer.md` remains the authority for fungal occurrence and decomposition ecology.
- `design/fungal-fruiting-survey-harvest-monitoring-protocol.md` extends that fungal authority with detectability, repeated surveys, fruiting episodes, sample provenance and harvest monitoring.
- existing Flora/Agriculture, Soil, Irrigation, Toxicology, Biosecurity, Science, Metrology, Botanical Gardens, Food Safety and Research Ethics authorities remain downstream/upstream owners for their respective state.

The unresolved gap is diagnostic: when plants show wilting, chlorosis, lesions, dieback, poor growth, unusual fruiting, root damage or other decline, Ouros needs a persistent evidence chain that can preserve competing biotic and abiotic explanations instead of jumping directly from symptom to pathogen.

Proposed Pass 159 authority is therefore narrow:

`plant symptom/sign surveillance -> sample provenance -> diagnostic hypothesis -> test/assessment -> scoped disease determination -> intervention handoff -> follow-up`

## New public sources reviewed

### International Plant Protection Convention — ISPM 6, Surveillance

Source: https://www.ippc.int/en/publications/guidelines-surveillance/
Current public page published 2025-07-28.

Reusable lesson:

Surveillance is a system with defined methods and evidence, not a magical absence detector. Ouros should preserve where, when, how and with what effort an observation was made. `NOT_DETECTED` must remain distinct from `ABSENT`.

Transformation into Ouros:

- fixed-plot, transect, nursery, orchard and forest-health surveys can share a common evidence protocol;
- coverage gaps remain visible in Chronicle;
- later surveys can revise confidence without rewriting old observations;
- quarantine or management decisions can cite the best available survey rather than claiming omniscience.

### IPPC — ISPM 27 and Technical Panel on Diagnostic Protocols

Sources:

- https://www.ippc.int/en/publications/593/
- https://www.ippc.int/en/commission/standards-committee/technical-panels/technical-panel-diagnostic-protocols/

Reusable lesson:

Diagnosis separates detection from identification and evaluates methods using properties such as sensitivity, specificity and reproducibility. Different organism groups require different protocols.

Transformation into Ouros:

- a diagnostic result records method revision and target scope;
- `DETECTED` does not automatically mean `CAUSAL`;
- a negative result is scoped to sample, method and detection limits;
- an institution can upgrade its methods while keeping earlier results historically valid for their time.

No real-world phytosanitary law, regulated-pest list or quarantine regime is imported into Ouros.

### Penn State Extension — Diagnosing a Plant Problem 101

Source: https://extension.psu.edu/diagnosing-a-plant-problem-101
Updated 2025-02-12.

Reusable lesson:

Similar symptoms can arise from pathogens, animals, irrigation, soil, nutrition, temperature, light, chemical injury and other site conditions. Distribution pattern and symptom progression help narrow alternatives.

Transformation into Ouros:

A plant-health case can remain open while Agriculture, Soil, Irrigation, Air Quality, Toxicology, IPM, fungi and Weather each contribute evidence. A visible organism near an affected plant is evidence of presence, not automatic causation.

### Penn State Extension — Overview of Plant Diagnostics

Source: https://extension.psu.edu/overview-of-plant-diagnostics
Updated 2025-09-19.

Reusable lesson:

Signs and symptoms are different. A sign is physical evidence of an organism; a symptom is the plant's response. Multiple stresses can coexist, and host/site history matters.

Transformation into Ouros:

- `SYMPTOM_OBSERVATION` and `SIGN_OBSERVATION` remain separate records;
- a fungal fruiting body may hand off to Pass 72/158 fungal records without proving that fungus caused the plant decline;
- a drought-stressed tree with a secondary pathogen can preserve both factors instead of forcing a single-cause story.

### Penn State Extension — Diagnosing Poor Plant Health

Source: https://extension.psu.edu/diagnosing-poor-plant-health
Updated 2026-06-29.

Reusable lesson:

Plant decline requires reviewing history and multiple possible causes. Pests and disease are only two categories among many.

Transformation into Ouros:

NPC expertise becomes useful through longitudinal records, maintenance history and sample quality, not through a universal diagnostic Skill check invented by the narrative layer.

## PTU / campaign / fan-design material

### PTU Community Adventure Book — Puce Forest

Public source surfaced through: https://www.scribd.com/document/439861954/PTU-Community-Adventure-Book-v0-1

The adventure presents a village disease, apparently scarce medicinal Paras mushrooms and a later causal reveal involving poisoning and poaching.

Reusable high-level structure only:

`visible health crisis -> scarce apparent remedy -> economic/social pressure -> ecological anomaly -> investigation -> causal explanation differs from first assumption`.

Ouros transformation:

Use the investigative pacing, but avoid copying the adventure's poison-water reveal, herbalists, Paras exploitation or plot. A Pass 159 case should support multiple evidence-backed endings, including mixed or unresolved causes.

Design lesson: a treatment appearing to help does not by itself prove the original diagnosis. A non-specific intervention can improve symptoms for the wrong inferred reason.

### Pokémon Blight fangame

Public source: https://pokemon-blight.itch.io/pokemon-blight

The fangame uses a parasitic plant disease as part of a large villain/environment premise.

Reusable lesson:

Plant decline can affect public memory, political narratives and attitudes toward nature for years.

Ouros anti-pattern:

Do not let every plant disease become a region-ending corruption, villain origin or supernatural plague. Most cases should remain local, uncertain and institutionally manageable. Escalation must come from evidence and authored stakes.

### Kairos Isles PTU — Iniko Orchard

Public source: https://kairosptu.fandom.com/wiki/Isle_Iniko

The living-world page describes an orchard maintained with recurring Pokémon participation and physical collection infrastructure.

Reusable lesson:

An orchard can be a persistent institution with workers, Pokémon roles and material systems. A health problem there can therefore produce callbacks through Workplaces, Working Pokémon, IPM, Food and Supply Chains rather than existing only as a one-scene encounter.

Do not copy the named characters, exact upgrades or facility mechanics.

## PTU mechanical boundary

Public PTU material contains a mechanical `Blight Condition` under a specific Poison-oriented Trainer Feature. That combat term is not plant pathology.

Pass 159 must never map:

- plant blight -> PTU Blight Condition;
- diseased plant -> Poisoned;
- fungal sign -> Effect Spore;
- spore detection -> `Spore` Move;
- plant decline -> Grassy Terrain or Rough Terrain;
- treatment -> healing Move or Item;
- Grass/Poison type -> diagnostic authority.

Exact PTU/Caelo Moves, Abilities, Items and Features remain downstream mechanics and require source/runtime evidence individually.

## Reusable Ouros narrative structures

### 1. Same symptom, different cause

Two orchards show the same leaf discoloration. One traces to irrigation salinity; the other to a biological agent. The mystery is comparative diagnosis, not finding a single regional villain.

### 2. Same cause, different expression

One agent produces different visible patterns because host variety, soil condition, weather or plant age differ. This creates disagreements that can all begin from honest observation.

### 3. Positive detection, uncertain causality

A lab detects an organism in damaged tissue. It remains possible that the organism is secondary, incidental or one factor in a mixed syndrome.

### 4. Negative result, useful uncertainty

A sample tests negative. The record narrows one hypothesis under that method and sample. It does not establish universal absence.

### 5. Treatment worked, diagnosis still open

Pruning, irrigation correction, sanitation or access changes improve the site. The intervention may have affected several possible causes at once.

### 6. Institutional memory improves future response

After several seasons, a nursery learns which samples to collect, which weather records matter and which symptoms deserve immediate isolation. Successful world progression can reduce future quest load.

## Guardrails for original Ouros material

- Keep symptom, sign, detection, identification, diagnosis and causality separate.
- Preserve raw observations after later reclassification.
- Preserve sample provenance and method revision.
- Treat `NOT_DETECTED` as scoped evidence.
- Do not infer disease from a Pokémon species being nearby.
- Do not infer toxicity from Poison typing.
- Do not infer infection from fungal fruiting.
- Do not infer safety from one clean sample.
- Do not infer outbreak from one affected plant.
- Do not infer malicious introduction from a new detection.
- Do not infer treatment authorization from battle victory.
- Minecraft blocks, particles and loaded entities are presentation, not diagnosis.

## Canon status

Everything in this scan is research or proposed structure. No pathogen, disease, quarantine regime, diagnostic institution, crop syndrome, plant-loss event or Pokémon association becomes Ouros canon through Pass 159.

## Unresolved source questions

The project-accessible search did not recover a complete primary Caelo rules corpus for plant disease, botanical diagnosis, quarantine or environmental exposure. Super PTU Online Helper was not exposed as an invocable capability in this runtime. Pass 159 therefore does not invent Caelo mechanics or helper output.