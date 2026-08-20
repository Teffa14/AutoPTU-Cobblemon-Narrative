# Outbreak, Health Surveillance & Epidemiology Layer

Status: PROPOSED SYSTEMS DESIGN. Not Ouros canon. Mechanical effects remain subordinate to PTU/Caelo and AutoPTU authority.

## Purpose

This layer lets Ouros detect, investigate and remember health events that affect multiple Pokémon, people, institutions or ecosystems without turning narrative observations into invented medical mechanics.

It connects existing care, science, crisis, ecology, sanitation, communications and institutional systems.

The layer does not create a disease simulator by default.

## Core separation

Ouros must preserve these as different states:

1. what happened to an individual;
2. what observers noticed;
3. what a care provider diagnosed;
4. whether the observation meets an investigation case definition;
5. what possible exposures occurred;
6. what investigators currently hypothesize;
7. what evidence supports or weakens each hypothesis;
8. what control measures institutions actually authorized;
9. what the public has heard;
10. what the battle engine says about mechanical statuses.

A narrative outbreak cannot directly write a PTU Status Condition.

A PTU Status Condition cannot directly create an outbreak.

## Primary objects

### HEALTH_SIGNAL

A health-related observation that may or may not become part of an investigation.

Suggested fields:

```yaml
signal_id: null
observed_at: null
location_id: null
subject_ref: null
subject_kind: pokemon_entity|person|population|unknown
observer_ref: null
observations: []
source_type: clinic|field|research|player|sensor|institution|other
care_case_id: null
evidence_refs: []
privacy_class: restricted
quality: unreviewed
```

`observations` should contain factual observations when possible.

Examples:

- repeated coughing was observed;
- appetite was reported lower;
- three wild Pokémon arrived from the same route;
- unusual mortality was observed in a remote population;
- several Pokémon failed to recover as expected.

Do not store a diagnosis in `observations` unless it was actually made by an authorized source.

### HEALTH_BASELINE

A versioned description of what is normally observed for a place, population, season or institution.

```yaml
baseline_id: null
scope_refs: []
period: null
measure_definition: null
expected_range: null
confidence: unknown
source_dataset_refs: []
valid_from: null
valid_to: null
```

A baseline can be weak or missing.

The system must be able to say:

`cluster suspected; baseline insufficient`.

### OUTBREAK_INVESTIGATION

Persistent investigation object.

```yaml
investigation_id: null
status: SUSPECTED
opened_at: null
lead_institution_refs: []
partner_institution_refs: []
case_definition_version_id: null
included_case_refs: []
excluded_case_refs: []
exposure_graph_id: null
hypothesis_refs: []
control_measure_refs: []
public_notice_refs: []
resolution_state: null
after_action_review_id: null
```

Suggested status vocabulary:

- SIGNAL_ONLY
- SUSPECTED
- ACTIVE_INVESTIGATION
- CAUSE_PARTIALLY_RESOLVED
- CONTROLLED
- MONITORING
- CLOSED
- REOPENED

Do not use `OUTBREAK_CONFIRMED` as an automatic state merely because a threshold is exceeded. Confirmation requirements are authored by the responsible institution and evidence model.

### OUTBREAK_CASE_DEFINITION

Versioned surveillance criteria.

```yaml
case_definition_version_id: null
investigation_id: null
version: 1
valid_from: null
subject_scope: null
place_scope: []
time_window: null
observed_criteria: []
exclusion_criteria: []
required_evidence_quality: null
created_by: null
supersedes: null
```

This object is for investigation consistency.

It is not a clinical diagnosis rule.

### SURVEILLANCE_CASE

A link between one subject/event and the current case definition.

```yaml
surveillance_case_id: null
subject_ref: null
signal_refs: []
care_case_ref: null
classification: POSSIBLE|PROBABLE|CONFIRMED_FOR_SURVEILLANCE|EXCLUDED|UNRESOLVED
case_definition_version_id: null
classified_at: null
classified_by: null
```

The term `CONFIRMED_FOR_SURVEILLANCE` means the record meets authored surveillance criteria. It must not silently mean a mechanically confirmed infection unless the actual authoritative health system says so.

### EXPOSURE_EVENT

Represents opportunity for shared exposure.

```yaml
exposure_event_id: null
subject_refs: []
location_ref: null
start_time: null
end_time: null
exposure_kind: shared_water|shared_space|direct_contact|shared_item|shared_transport|environment|unknown
observed_directly: false
source_refs: []
confidence: null
```

Important:

`EXPOSURE_EVENT != transmission event`.

### HEALTH_HYPOTHESIS

Investigation hypothesis.

```yaml
hypothesis_id: null
investigation_id: null
claim: null
status: OPEN|SUPPORTED|WEAKENED|REJECTED|UNRESOLVED
supporting_evidence_refs: []
contradicting_evidence_refs: []
created_at: null
last_reviewed_at: null
```

Possible hypothesis classes can include infectious, environmental, nutritional, behavioral, toxic, mechanical injury, common-source exposure, mixed-cause cluster or unknown.

Those classes describe investigative direction only. They do not create mechanics.

### CONTROL_MEASURE

A recorded institutional response.

```yaml
control_measure_id: null
investigation_id: null
measure_type: null
authorized_by: null
scope_refs: []
starts_at: null
ends_at: null
review_at: null
reason_refs: []
implementation_state: PLANNED|ACTIVE|PARTIAL|ENDED|WITHDRAWN
```

No measure can exist merely because the generator thinks it is sensible.

Authority must come from the authored institution/civic system.

### HEALTH_SURVEILLANCE_NETWORK

Links participating institutions and observation channels.

Potential members:

- Pokémon Centers;
- mobile clinics;
- field researchers;
- ranger/stewardship teams;
- nurseries;
- transport operators;
- sanitation facilities;
- weather/environment stations;
- player field reports;
- laboratories when canon establishes them.

The network does not imply universal data access.

Each data handoff must respect the existing communications/privacy layers.

## Baseline and anomaly logic

The system should distinguish three states:

`unusual compared with known baseline`

`several similar observations but baseline unknown`

`within expected variation`

This prevents quest generation from turning every two matching care cases into a regional emergency.

### Suggested anomaly trigger

A health signal can become investigation-eligible when one or more are true:

- count exceeds a versioned local threshold;
- severity is authored as sentinel-worthy;
- a rare observation occurs;
- the same signal appears across multiple independent sources;
- a care facility detects repeated geographic linkage;
- an environmental sensor and clinical signals align;
- a trusted actor explicitly opens an investigation.

Thresholds are world-design values, not PTU mechanics.

## Privacy model

Health data is restricted by default.

Public systems should usually receive aggregates such as:

- five comparable cases reported this week;
- multiple reports came from the north trail;
- cause remains under investigation;
- a temporary route advisory is active.

They should not automatically receive:

- patient identity;
- exact personal location history;
- private Trainer-Pokémon care notes;
- genetic/sample data;
- private contact network;
- unpublished diagnosis.

Player-created care information requires explicit authority before other players can read it.

## Investigation loop

A reusable loop:

health signals
→ compare with baseline
→ open investigation if justified
→ define surveillance case
→ classify comparable reports
→ build exposure graph
→ collect clinical/environmental/ecological evidence
→ revise hypotheses
→ authorize proportionate measures
→ observe response
→ verify decline/recovery
→ after-action review
→ preserve consequences.

This loop can stop early if the signal is a false alarm.

## Multi-cause investigations

The engine must support:

`one investigation -> several causal explanations`.

Example:

- some Pokémon are poisoned by runoff;
- others have an unrelated seasonal illness;
- a third group is only dehydrated after a route disruption.

The satisfying conclusion can be that the initial cluster was not one disease.

## Environmental-health integration

This layer can reference:

- `design/waste-sanitation-recycling-pollution-layer.md` for contaminants and waste pathways;
- `design/meteorology-forecasting-weather-layer.md` for environmental timing;
- `design/seasonality-calendar-phenology-layer.md` for normal seasonal patterns;
- `design/interspecies-ecological-relations-layer.md` for population contact opportunities;
- `design/conservation-protected-areas-stewardship-layer.md` for wildlife observation;
- `design/food-agriculture-hospitality-layer.md` for food batches and supply chains;
- `design/travel-transport-expedition-layer.md` for movement networks.

An investigation should link to those state objects instead of copying their data.

## Clinical integration

Individual diagnosis, treatment, health state and recovery remain owned by `care-recovery-welfare-layer.md` and authoritative PTU/Caelo mechanics when applicable.

This layer can ask:

- Are these care cases similar?
- Do they share time/place/exposure?
- Did several arrive from the same route?

It cannot decide:

- exact Medicine DC;
- healing amount;
- Injury removal;
- a new disease stat;
- contagion probability;
- immunity;
- treatment efficacy;
- whether a Pokémon mechanically has Poisoned or another Status.

## Pokérus guardrail

Pokérus must be modeled only if Ouros canon and the governing PTU/Caelo source explicitly define it.

Do not use main-series Pokérus probabilities or EV effects by default.

If it is ever supported, it should receive a dedicated authoritative state contract rather than being mapped casually to `Poisoned`.

## Quarantine/isolation guardrail

The words `quarantine`, `isolation`, `closure`, `visitor restriction` and `transfer pause` must not be interchangeable.

A future canon layer must define which institutions can authorize each measure and for what scope.

The narrative generator can propose an option, but cannot enforce it unless authority is established.

A person or Pokémon subject to a control measure is not thereby guilty, dangerous or confirmed infected.

## Public communication

Public messages should reference the investigation state, not invent certainty.

Useful message fields:

```yaml
public_health_notice_id: null
investigation_id: null
issued_by: null
issued_at: null
scope: null
known_facts: []
unknowns: []
actions_requested: []
expires_or_reviews_at: null
supersedes: null
```

Corrections remain in history.

Rumors continue separately.

## World-state consequences

Health events may legitimately affect:

- clinic capacity;
- staffing;
- transport schedules;
- event attendance;
- tourism;
- wildlife movement;
- nursery intake;
- market/service demand;
- public trust;
- research funding;
- route access;
- sanitation priorities;
- school/workplace schedules;
- conservation policy review.

Every consequence should point to a causal or institutional record.

## Multiplayer

Different players may know different parts of the same investigation.

A researcher may know sample results.

A clinic worker may know patient history.

A ranger may know wildlife observations.

A journalist may know only the public notice and witness interviews.

A party should not gain all private information because one member has access.

## Offline advancement

Outbreak clocks may advance while players are offline only if the world simulation has authored rules for:

- signal arrival;
- case progression;
- institutional response;
- transport/ecology changes;
- review cadence.

The system should not invent infections among unloaded entities merely to keep a curve moving.

Coarse aggregate change is preferred to simulating every contact.

## Encounter integration rule

Most outbreak gameplay should occur outside the battle grid.

Combat can happen because:

- a wild Pokémon is distressed or territorial;
- actors interfere with field work;
- a dangerous location must be reached;
- a route has become contested;
- responders need access to equipment.

The battle itself must still use ordinary legal PTU rules.

Illness cannot be represented by arbitrary combat debuffs unless the authoritative engine supports the exact condition.

## Encounter contract A — Trail Clinic Supply Run

Narrative premise:

A field clinic investigating a cluster has enough staff but loses access to sample containers and routine supplies after a route closure.

### REDUCED

Resolve logistics, delivery and clinic capacity in world state. If a conflict occurs, use a static encounter on a safe section of the route. Cargo remains outside tactical HP/objective rules.

Required categories:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- selected Moves/Abilities/Items/Features — PARTIAL only where used.

### FULL

Participants protect mobile medical cargo while moving through a changing chokepoint and preserving a route for retreat.

Additional dependencies:

- complete movement including interception/forced movement — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if route conditions matter tactically;
- full lifecycle — PARTIAL;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING.

No contamination or infection effect is applied by narrative fiat.

## Encounter contract B — Wildlife Sampling Perimeter

Narrative premise:

Researchers need observations from a wild collective near a suspected exposure source. The objective is safe access and withdrawal, not defeating the entire population.

### REDUCED

Sampling occurs in overworld/world state. Any defensive battle uses only currently present combatants and a static legal map. Sampling success is not decided by battle damage.

### FULL

Wild Pokémon can withdraw, researchers must hold a limited safe area, and AI behavior changes around escape routes.

Additional dependencies:

- complete movement/interception — BLOCKING;
- terrain/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

## Encounter contract C — Treatment Plant Access

Narrative premise:

An investigation needs access to a sanitation facility because environmental measurements and patient geography overlap.

### REDUCED

Facility access, samples and contamination state remain outside AutoPTU. If a battle occurs, isolate it to a dry static arena.

### FULL

Facility zones, active machinery and changing environmental hazards matter during the confrontation.

Additional dependencies:

- terrain/weather/hazards/zones/reactions — BLOCKING;
- complete movement — BLOCKING if machinery moves actors;
- full lifecycle — PARTIAL for timed changes;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

## No-inference rules

- Poisoned does not create an outbreak case automatically.
- A health signal cannot grant or remove a Status.
- A surveillance classification cannot alter HP.
- A negative test does not erase earlier observations.
- A closed investigation remains in historical state.
- A reopened investigation keeps its prior versions.
- Similar species symptoms do not prove same cause.
- A released former partner does not become a public-health risk merely because it appears near cases.
- Wild Pokémon are not automatically capturable because responders need samples.
- A player cannot inspect private patient data through proximity.
- A clinic cannot broadcast private details through Minecraft UI.

## Promotion gate

Before any outbreak concept enters canon, review must establish:

1. the actual condition or leave it intentionally unknown;
2. which institutions exist and who has authority;
3. what data is private/public;
4. which PTU/Caelo mechanics, if any, represent the condition;
5. whether AutoPTU supports those mechanics;
6. whether any tactical encounter needs reduced implementation;
7. how Cobblemon/world state represents affected populations without simulating unsupported contagion;
8. recovery and after-effects.

Until then, this layer is an investigation/world-state framework only.