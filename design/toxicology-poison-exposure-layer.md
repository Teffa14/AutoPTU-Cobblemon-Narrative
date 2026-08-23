# Toxicology, Poison Exposure & Exposure-Route Layer

Status: PROPOSED SYSTEMS DESIGN. Not Ouros canon. Mechanical effects remain subordinate to PTU/Caelo and AutoPTU authority.

## Purpose

This layer lets Ouros represent toxic agents, exposure opportunities, route-specific contact, uncertain dose, toxicology evidence, decontamination and source-attribution over time without converting environmental fiction directly into PTU Poisoned or Badly Poisoned.

It sits between source-owning world systems and care/health investigation.

Examples of source-owning systems:

- Air Quality for atmospheric plumes;
- Drinking Water/Freshwater/Groundwater for water state;
- Waste/Sanitation for waste streams;
- Food for contaminated batches;
- Manufacturing/Material Culture for chemicals and product batches;
- Flora/Decomposition for biological material;
- Pokémon Agency for an individual Pokémon producing venom, gas, spores or another substance.

Care owns diagnosis and treatment.
Outbreak/Health Surveillance owns cluster investigation.
Cases owns allegations/evidence around wrongdoing.
AutoPTU owns battle Status state.

## Core separation

Ouros must preserve these as separate states:

1. hazardous agent exists;
2. source of that agent is known or hypothesized;
3. subject had an opportunity for contact;
4. route of contact is known or hypothesized;
5. actual exposure is confirmed, probable, possible or unresolved;
6. magnitude/dose is measured, estimated or unknown;
7. observable effects exist or do not exist;
8. diagnosis is known or unresolved;
9. treatment/decontamination was ordered or completed;
10. public interpretation exists;
11. PTU mechanical Status exists or does not exist.

No layer may collapse these stages for narrative convenience.

## Primary objects

### TOXIC_AGENT_PROFILE

Persistent knowledge object for a substance, mixture, biological secretion or other agent relevant to toxicology.

```yaml
agent_profile_id: null
name: null
agent_class: biological|industrial|environmental|foodborne|unknown
identity_confidence: null
known_source_refs: []
known_routes: []
known_effect_claim_refs: []
mechanical_rule_refs: []
created_at: null
last_reviewed_at: null
status: PROVISIONAL|REVIEWED|SUPERSEDED
```

Important:

This object stores current knowledge, not universal truth.

`mechanical_rule_refs` may point to exact PTU effects when one exists. It does not authorize extrapolation beyond those rules.

### TOXIC_SOURCE_EVENT

A source-release or source-availability event.

```yaml
source_event_id: null
agent_profile_ref: null
source_ref: null
source_kind: pokemon|container|process|water|air|food|plant|fungus|waste|unknown
location_ref: null
starts_at: null
ends_at: null
observed_quantity: null
containment_state: null
observation_refs: []
source_attribution_state: CONFIRMED|PROBABLE|POSSIBLE|DISPUTED|UNKNOWN
```

A source event can exist without any exposed subject.

### EXPOSURE_OPPORTUNITY

Records circumstances in which exposure may have occurred.

```yaml
exposure_opportunity_id: null
source_event_ref: null
subject_refs: []
location_ref: null
start_time: null
end_time: null
possible_routes: []
protective_state_refs: []
activity_context: null
evidence_refs: []
```

`EXPOSURE_OPPORTUNITY != exposure confirmed`.

### EXPOSURE_RECORD

Subject-specific toxicology record.

```yaml
exposure_record_id: null
subject_ref: null
agent_profile_ref: null
source_event_ref: null
route: ingestion|inhalation|injection|bite|sting|dermal|ocular|mixed|unknown
route_confidence: null
exposure_status: POSSIBLE|PROBABLE|CONFIRMED|EXCLUDED|UNRESOLVED
magnitude_kind: measured|estimated|unknown
magnitude_value: null
unit: null
exposure_window: null
protective_state_refs: []
clinical_observation_refs: []
care_case_ref: null
mechanical_status_refs: []
reviewed_at: null
```

Do not invent dose values when no authoritative measurement exists.

### TOXICOLOGY_SAMPLE

Sample or retained material used in investigation.

```yaml
sample_id: null
sample_kind: blood|saliva|venom|gas_capture|water|soil|food|surface_swab|plant|unknown
subject_or_source_ref: null
collected_at: null
collected_by: null
location_ref: null
custody_refs: []
storage_state_refs: []
analysis_refs: []
research_ethics_ref: null
```

Sampling of a person or Pokémon requires the appropriate Research Ethics/Care authority.

### TOXICOLOGY_ASSESSMENT

Versioned interpretation.

```yaml
assessment_id: null
subject_or_event_refs: []
agent_profile_ref: null
exposure_record_refs: []
assessment_version: 1
conclusion_state: SUPPORTED|WEAKLY_SUPPORTED|UNRESOLVED|WEAKENED|REJECTED
interpretation: null
supporting_evidence_refs: []
contradicting_evidence_refs: []
limitations: []
assessed_by: null
assessed_at: null
supersedes: null
```

The assessment may change later without rewriting the underlying sample or observation.

### SOURCE_ATTRIBUTION_HYPOTHESIS

Keeps source attribution separate from exposure assessment.

```yaml
hypothesis_id: null
incident_ref: null
candidate_source_ref: null
claim: null
status: OPEN|SUPPORTED|WEAKENED|REJECTED|UNRESOLVED
supporting_evidence_refs: []
contradicting_evidence_refs: []
last_reviewed_at: null
```

A Poison-type Pokémon may be one candidate source among several. Type alone is never evidence of causation.

### DECONTAMINATION_EVENT

Records an action intended to remove or reduce an external agent.

```yaml
decontamination_event_id: null
target_ref: null
agent_profile_ref: null
procedure_ref: null
authorized_by: null
starts_at: null
ends_at: null
completion_state: PLANNED|PARTIAL|COMPLETED|ABORTED
verification_refs: []
mechanical_effect_ref: null
```

Narrative decontamination does not cure a PTU Status unless an authoritative mechanic is called and recorded in `mechanical_effect_ref`.

### EXPOSURE_ADVISORY

Institutional communication about risk.

```yaml
advisory_id: null
scope_refs: []
agent_profile_ref: null
issued_at: null
issued_by: null
recommended_actions: []
evidence_refs: []
confidence: null
status: ACTIVE|UPDATED|LIFTED
supersedes: null
```

An advisory is an institutional response. It is not proof that every actor in scope was exposed.

## Exposure routes

Default narrative vocabulary can distinguish:

- ingestion;
- inhalation;
- injection;
- bite;
- sting;
- dermal contact;
- ocular contact;
- mixed;
- unknown.

These categories are world-state descriptors only.

Do not assign PTU damage, Status, save DCs or treatment from the route unless a governing rule explicitly defines them.

## Biological toxins and Pokémon

A Pokémon can be associated with venom, poison, spores, gas or irritating secretions through authored species lore or direct observation.

Store separately:

- species-level lore;
- individual production event;
- source identity;
- exposure opportunity;
- subject-specific exposure;
- observed outcome;
- mechanical effect.

Example:

A Seviper bites a field worker.

Possible records:

- attack observed;
- bite wound observed;
- Seviper identity confirmed;
- venom exposure probable or confirmed depending on evidence;
- symptoms recorded separately;
- diagnosis/treatment owned by Care;
- PTU Poisoned only if the authoritative rules event actually applied it.

Do not assume every bite injects the same amount or every affected subject develops the same outcome.

## Environmental toxicology

Environmental systems can create candidate source events.

Examples:

- Air Quality reports a plume;
- Drinking Water reports a contaminated zone;
- Waste records a leaking container;
- Manufacturing records a process deviation;
- Food records a suspect batch;
- Groundwater records a plume hypothesis;
- Flora records a plant material sample;
- Decomposition records fungal material.

The toxicology layer then evaluates exposure relationships.

This prevents source systems from inventing health outcomes.

## Clinical handoff

When a subject has symptoms or requires assessment:

1. Toxicology records exposure history and evidence.
2. Care opens or updates a `CARE_CASE`.
3. Care owns diagnosis and treatment.
4. AutoPTU/PTU owns any mechanical HP/Status change.
5. Outbreak/Health Surveillance may aggregate cases if a cluster exists.

A toxicology assessment can remain unresolved even after the patient improves.

## Outbreak integration

Outbreak/Health Surveillance may open a common-source toxic investigation.

Examples:

- multiple subjects used the same water source;
- several Pokémon entered the same warehouse;
- repeated symptoms occur after a festival meal;
- several workers occupied the same process area.

The exposure graph must allow:

- one source, several routes;
- several sources, one symptom pattern;
- one apparent cluster that later splits into unrelated events.

## Case and liability boundary

Toxicology evidence can support a Case.

It cannot decide criminal intent, negligence, sabotage or liability.

Examples:

- a container leaked;
- an operator was present;
- a source was identified;
- exposure occurred.

None of those facts alone proves wrongdoing.

## Time and persistence

Exposure-related records are append-only.

A later identification may change:

- agent classification;
- source attribution;
- estimated exposure magnitude;
- interpretation of old symptoms.

It must not alter:

- original sample time;
- original observer report;
- original raw measurement;
- original public notice;
- original mechanical battle transcript.

## Minecraft projection

Minecraft may display:

- closed rooms;
- warning signs;
- protective gear;
- damaged containers;
- visible gas/smoke when authored;
- cleanup crews;
- sampling equipment;
- restricted access;
- decontamination staging.

Minecraft must not infer:

- toxicity from particle color;
- exposure from proximity alone;
- PTU Status from entering an area;
- safe concentration from particle absence;
- Poison immunity from Pokémon Type;
- source identity from a nearby Poison-type.

## Battle handoff

When toxicology intersects combat, there are two legal patterns.

Pattern A: exact PTU effect exists.

The battle uses the authoritative Move/Ability/Item/Feature/field rule and records the resulting Status or damage normally.

Pattern B: narrative environmental exposure exists without a validated PTU battle mechanic.

Resolve the toxicology/exposure state outside the battle. Freeze a conventional legal arena. Do not fabricate a custom Poison zone.

## Guardrails

Never infer:

- exposure from hazard presence alone;
- dose from distance alone;
- diagnosis from symptoms alone;
- source from Pokémon Type alone;
- PTU Poisoned from environmental contamination;
- environmental toxin from PTU Poisoned;
- immunity to toxins from Poison or Steel Type;
- universal protection from Gas Mask;
- treatment success from decontamination;
- decontamination success from cleanup visuals;
- causation from timing alone;
- wrongdoing from a confirmed source event;
- exact effects from community/homebrew rules.

## Engine-facing capability boundary

This systems layer does not require AutoPTU for ordinary investigation.

Mechanically rich toxic encounters may require:

- targeting/footprints/range/LoS for exact Move targeting;
- base movement legality for ordinary movement;
- complete movement for evacuation, withdrawal, interception or forced relocation;
- full turn/round lifecycle for escalating Status/delayed effects;
- full stateful damage pipeline for authoritative damage;
- status lifecycle for Poisoned/Badly Poisoned/Sleep or other exact effects;
- terrain/weather/hazards/zones/reactions only when an exact validated battlefield environmental effect exists;
- move-specific behavior for Poison Gas, Toxic, Poison Fang, Toxic Spikes or other concrete Moves;
- abilities for immunity/prevention/suppression interactions;
- items for Gas Mask, Antidote or other exact equipment/consumables;
- Trainer Features/perks for exact medical/toxicology-related effects if present;
- AI tactical policy for EVACUATE/WITHDRAW/PROTECT/REACH_SAFE_ZONE behavior;
- Minecraft/Cobblemon/Craftics playback for semantic representation.

The world-state layer must never fill missing battle families itself.

## Open canon questions

- Which toxic substances and biological hazards exist as authored Ouros world material?
- Which regions have toxicology laboratories or specialist care?
- Who can issue exposure advisories?
- Which environmental incidents predate the players?
- How are biological samples stored and protected?
- Which Pokémon have authored institutional roles in detection or response?
- What environmental exposure rules, if any, exist in Caelo?
- What exact PTU/Caelo rules govern Gas Mask, Antidote, Medicine, Poisoned, Badly Poisoned and toxic environments?
- Should Ouros ever model dose numerically outside exact source mechanics, or keep most exposure magnitude qualitative?

Until those questions are resolved, the layer remains evidence-first and mechanically conservative.
