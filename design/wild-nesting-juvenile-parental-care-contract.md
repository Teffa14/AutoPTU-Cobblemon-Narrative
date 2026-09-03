# Wild Nesting, Juvenile and Parental Care Contract

Status: PROPOSED DESIGN. Not canon-approved.
Date: 2026-09-03

## Purpose

Define persistent wild nesting and dependent-young ecology without conflating it with Trainer breeding, nursery custody or hidden tactical combat.

This contract extends the ecology programme and global interaction graph. It consumes mechanically/canonically resolved Egg or species facts when available but does not decide breeding eligibility, hatch output, inheritance, mechanical hatch timing or ownership.

## Authority boundary

```text
approved species ecology
+ persistent population / individual state
+ real Minecraft habitat facts after world lock
+ local disturbance / predator / resource state
-> Ouros nesting and care state
-> Cobblemon/Minecraft visible projection
-> observation / intervention
-> explicit Ouros handoff if structured mechanics begin
-> AutoPTU tactical resolution
-> semantic result returned to ecology
```

Minecraft entity presence, vanilla aggression, despawn or pathfinding failure cannot author nest failure, juvenile death, abandonment or capture.

## Core nesting-site record

```yaml
nest_site_id: null
ecosystem_id: null
location_ref: null
microhabitat_ref: null
substrate_tags: []
cover_score: null
accessibility_score: null
resource_access_refs: []
predator_pressure_refs: []
human_disturbance_refs: []
occupancy_state: UNKNOWN
caregiver_ids: []
dependent_ids: []
dependence_stage: null
provisioning_state: null
vigilance_state: null
relocation_pressure: 0.0
abandonment_pressure: 0.0
observation_confidence: 0.0
source_refs: []
last_updated_at: null
```

Exact numeric scoring is not canonized here.

Candidate `occupancy_state` values:
- UNKNOWN;
- PREPARING;
- ACTIVE;
- TEMPORARILY_UNATTENDED;
- THREATENED;
- RELOCATING;
- ABANDONED;
- FAILED_CONFIRMED;
- INDEPENDENCE_REACHED;
- RESOLVED.

`FAILED_CONFIRMED` requires evidence. Absence alone is insufficient.

## Care relationship record

```yaml
care_relationship_id: null
caregiver_id: null
dependent_id: null
relationship_type: null
status: ACTIVE
provenance_grade: null
source_refs: []
observed_since: null
last_observed_at: null
```

Allowed relationship semantics:
- `PARENT_OF` — only when mechanically or canonically established;
- `CARES_FOR` — observed care;
- `PROVISIONS_FOR` — repeated food/resource delivery;
- `DEFENDS_YOUNG` — protective behaviour;
- `DEPENDENT_ON` — juvenile dependence;
- `ESCORTS_YOUNG` — mobile caregiver relationship;
- `NESTS_AT` — occupancy relationship.

No edge automatically implies another.

## Dependent-young state

```yaml
dependent_young_state:
  entity_id: null
  species_id: null
  life_stage: null
  mobility_profile_ref: null
  independence_state: null
  caregiver_dependency_refs: []
  nest_site_id: null
  exposure_state: null
  persistent_entity: true
  mechanical_state_ref: null
```

Life-stage labels are ecological organization unless a PTU/Caelo rule gives them mechanical meaning.

The ecology system must not invent combat stats, level, Ability, Nature, injury, hatch progress or Tutor effects from a life-stage label.

## Protective-intent policy

Protective behaviour is a context-sensitive intent, not a permanent hostility flag.

Conceptual inputs:

```text
species protective prior
+ individual condition and verified capabilities
+ dependent vulnerability
+ distance from dependent / nest
+ perceived threat relevance
+ recent disturbance history
+ site accessibility / cover
+ predator pressure
+ escape / relocation options
+ alternate caregiver availability
+ habituation to local humans
= candidate protective intent
```

Candidate intents:
- conceal;
- remain close;
- observe;
- alarm;
- shadow;
- display;
- warn;
- block approach;
- herd/escort dependent away;
- relocate dependent;
- flee with dependent;
- engage;
- disengage once separation is restored.

These are Ouros behaviour states, not tactical statuses.

## Disturbance ledger

Nesting disturbance must accumulate from actual world events rather than one generic proximity check.

```yaml
nest_disturbance_event:
  event_id: null
  nest_site_id: null
  source_type: null
  source_actor_ids: []
  world_event_ref: null
  started_at: null
  ended_at: null
  intensity: null
  recurrence_key: null
  evidence_refs: []
```

Possible sources:
- repeated player approach;
- road or trail traffic;
- harvesting;
- construction;
- loud machinery;
- predator presence;
- weather exposure;
- resource depletion;
- wildfire/flood/other ecological pulse;
- failed relocation attempt;
- sustained observation pressure.

Disturbance may decay when pressure ends. No universal decay constant is fixed by this contract.

## Disturbance consequences

Increasing disturbance pressure may change:
- caregiver attendance;
- vigilance;
- exposure;
- provisioning route;
- active time window;
- defensive display probability;
- relocation pressure;
- route avoidance;
- player/NPC access recommendations.

It must not directly write:
- HP;
- injury;
- tactical status;
- death;
- hatch failure;
- capture;
- forced movement;
- battle defeat.

## Provisioning loop

Provisioning should be represented as a world-state loop when species evidence supports it.

```text
caregiver hunger / dependent demand
-> candidate resource target
-> foraging trip pressure
-> resource acquisition or failed acquisition
-> return / transfer attempt
-> dependent-care observation
-> resource network and caregiver schedule update
```

Off-screen resolution is statistical. It never instantiates a hidden tactical battle between caregiver and prey.

Provisioning can modify interaction-graph intensity temporarily, including predation or foraging pressure.

## Mobile care

Not all dependent-young ecology is site-centred.

A caregiver may carry, escort or continuously accompany a dependent. In that case:
- the caregiver/dependent group is the primary ecological object;
- `nest_site_id` may be null;
- protective radius follows the group;
- separation events can create search/reunion pressure;
- generic spawn reconciliation must preserve the persistent dependent.

## Nest-site quality and relocation

Nest quality is a physical-world property after the global world is locked.

Potential inputs:
- actual Minecraft block/substrate context;
- cover and visibility;
- vertical accessibility;
- water proximity;
- weather exposure;
- route/settlement overlap;
- nearby feeding resources;
- predator access;
- species-native biome compatibility.

Ouros may derive relocation pressure from approved inputs. It must not teleport a nest merely because the site is inconvenient for a quest.

A relocation event records old and new site references atomically.

## Human-management interventions

Noncombat interventions can include:
- temporary trail closure;
- rerouting traffic;
- limiting harvest near the site;
- reducing observation frequency;
- restoring cover/resource access;
- creating a quiet buffer;
- waiting for a dependence stage to end;
- supervised relocation when world/canon policy authorizes it.

Intervention success must be verified through later observations rather than immediately inferred from the player's intention.

## Observation contract

Players and NPCs receive evidence rather than hidden nesting state.

Possible evidence:
- repeated food-carrying trips;
- warning displays at a consistent boundary;
- juvenile calls/movement;
- fresh nesting material;
- reduced adult attendance after disturbance;
- route changes;
- abandoned material with uncertain cause;
- relocation traces;
- successful independence/fledging observation.

Observation packets should link to the existing ecology observation and information-propagation systems.

## Interaction graph extensions

Add optional local relationship types:
- `CARES_FOR`;
- `PROVISIONS_FOR`;
- `DEFENDS_YOUNG`;
- `NESTS_AT`;
- `DEPENDENT_ON`;
- `USES_NEST_RESOURCE`;
- `AVOIDS_NEST_ZONE`;
- `PREDATES_NEST_CONTENTS` when explicitly supported and locally plausible.

`PREDATES_NEST_CONTENTS` is not inferred from a general carnivore tag alone.

## Population and spawn projection

A nest may influence visible distribution without creating new population truth.

Potential projection effects:
- caregiver concentration near nest;
- lower free-roaming exposure for dependent young;
- increased provisioning-path activity;
- temporary territorial/avoidance zone;
- reduced visibility after disturbance;
- relocated concentration after a confirmed move.

Persistent caregivers/dependents must not be duplicated by generic Cobblemon spawns.

## Structured encounter handoff

### Reduced version — boundary warning and route management

Narrative premise:
The player approaches an active nesting area and receives escalating behavioural evidence before combat.

Resolution:
- Ouros updates vigilance and disturbance;
- Minecraft/Cobblemon presents warning, retreat, route blocking or despawn/reprojection using available adapter behaviour;
- player can withdraw, reroute or change local activity;
- no AutoPTU battle is required.

Dependencies:
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end for rich semantic behaviour;
- no tactical category required if structured combat does not begin.

Fallback presentation can use simple presence/absence, path avoidance and observation packets.

### Full version — protective territorial escalation

Narrative premise:
A caregiver engages after warnings fail and the intruder remains within the defended area.

Required capability families:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL when displacement/interception is used;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

The defended radius is an Ouros ecological fact before battle. If tactical zone/reaction mechanics are required to enforce it inside battle, category 9 is an explicit dependency.

### Reduced battle version

After Ouros explicitly decides escalation has occurred:
- instantiate a simple legal AutoPTU battle on static terrain;
- keep Egg/juvenile entities outside tactical participation unless rules explicitly support them;
- do not use custom escort, reaction, weather, moving-hazard or forced-displacement mechanics;
- ordinary retreat/disengagement can end the narrative threat once authoritative battle semantics permit it;
- write ecological consequences after the battle result.

This preserves the premise: the caregiver is protecting dependents, while unsupported mechanics are not fabricated.

### Full version — evacuation / relocation under pressure

Possible intended mechanics:
- escorting dependents;
- interception;
- forced movement;
- shifting safe zones;
- weather/hazard phases;
- delayed environmental effects;
- Trainer Feature interrupts;
- objective-oriented AI.

Dependencies:
- complete movement: PARTIAL and potentially blocking for exact forced/escort semantics;
- full turn/round lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI tactical policy: BLOCKING;
- adapter/playback: PARTIAL/BLOCKING.

Reduced version:
Resolve route selection, evacuation timing and dependent movement as overworld/world-state events. If combat interrupts the process, pause the ecological movement, run a simple supported battle, then resume from the authoritative semantic result.

## Live engine evidence for this contract

AutoPTU-Java `main` checked at:
- `21e0b02e5ff17132f3a7ed04007784884323df12` — stateful movement landing consequence executor.

This verifies a bounded server-authoritative landing/trap consequence seam, including status application through a shared pipeline and deterministic trap consumption ordering. It does not promote the full terrain/hazard family, complete movement, generic escort logic, parental AI or reaction policy.

Permanent readiness remains conservative:

VERIFIED within audited contracts:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

MIXED/PARTIAL/BLOCKING outside verified slices:
- terrain/weather/hazards/zones/reactions.

BLOCKING as complete family:
- AI tactical policy.

PARTIAL/BLOCKING end-to-end:
- Minecraft/Cobblemon/Craftics adapter/playback.

## Validation invariants

1. Wild nesting does not invoke Trainer breeding mechanics by default.
2. Caregiving does not prove parentage.
3. One approach does not automatically cause abandonment.
4. Repeated disturbance can matter without any battle occurring.
5. Absence does not prove death, failure or abandonment.
6. Generic spawning never clones persistent dependents or caregivers.
7. Off-screen predation/foraging never runs hidden tactical battles.
8. Protective ecological intent is not a PTU status.
9. AutoPTU receives authority only after explicit structured-combat handoff.
10. Rich encounter variants name every partial/blocking capability family they require.
11. A reduced implementation path exists without changing the narrative premise.
12. Exact species/site assignments wait for real worldgen and Cobblemon habitat compatibility.

## Open questions

- whether dependence stage is global or species-profile-specific;
- how quickly disturbance pressure decays;
- how to distinguish temporary unattended state from abandonment with limited observation;
- how caregiver loss is represented without inferring death;
- how multiple caregivers divide provisioning and defence;
- whether some species form communal nesting colonies;
- how predation pressure on nests affects demography without double-counting ordinary predator edges;
- exact Cobblemon projection controls for persistent juveniles;
- settlement policy for temporary route closure or authorized relocation;
- how actual generated terrain changes Marea's legacy nesting-site candidates.
