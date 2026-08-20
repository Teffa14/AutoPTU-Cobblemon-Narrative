# Anomalous Spaces & Dimensional Exploration Layer — Pass 50

Status: proposed systems design. Not canon. This document defines narrative/world-state architecture only. It does not create PTU mechanics.

## Purpose

Ouros needs a controlled way to represent objectively explorable spaces that violate ordinary geography: portals, stable alternate realms, mirror regions, pocket spaces, local distortions and dungeons whose layout changes between visits.

The system must preserve wonder without creating free teleportation, progression bypasses, softlocks, duplicate items/Pokémon, invented time travel or a second combat-rules engine inside Minecraft.

## Relationship to existing layers

This layer extends:

- `ouros-narrative-architecture.md` for persistent world graph and Chronicle;
- `mission-dungeon-grammar.md` for adventure structure;
- `travel-transport-expedition-layer.md` for ordinary routes and journeys;
- `cartography-survey-wayfinding-layer.md` for maps and known geography;
- `science-research-discovery-layer.md` for anomaly study;
- `myth-archaeology-sacred-sites-layer.md` for interpretation and old sites;
- `conservation-protected-areas-stewardship-layer.md` for ecological crossing effects;
- `digital-systems-cyberspace-data-layer.md` for simulations and virtual spaces;
- `dreams-aura-psychic-information-layer.md` for subjective dream regions;
- `encounter-implementation-contracts.md` for battle dependency declarations.

It does not replace any of them.

## Core separation

Never collapse these concepts into one generic `dimension` field:

1. Physical location identity.
2. Access edge or portal.
3. The actor/entity that opened or stabilized it.
4. Destination certainty.
5. Topology/layout version.
6. Return-path state.
7. What observers believe the space is.
8. What science/institutions currently claim it is.
9. Mechanical PTU effects, if any.
10. Minecraft visual representation.

A portal can be real while its destination is unknown. A map can change while the place remains the same persistent location. A space can resemble a known city while sharing none of its residents, property records or public institutions.

## Space classes

### STABLE_ALTERNATE_REALM

A persistent place with a stable identity and possibly unusual geometry or environmental rules.

The place keeps its own:

- location IDs;
- ecology;
- inhabitants;
- discoveries;
- institutions if authored;
- Chronicle events;
- access history.

Unusual geometry does not automatically create tactical movement effects.

### MIRROR_OR_ECHO_REGION

A realm that resembles or maps onto a known physical location but has independent state.

Similarity may exist in:

- street pattern;
- landmarks;
- building shells;
- terrain;
- historical traces.

Similarity does NOT automatically duplicate:

- NPCs;
- Pokémon individuals;
- inventories;
- ownership;
- cases;
- institutions;
- active quests;
- public memory.

### POCKET_SPACE

A bounded persistent or temporary area whose access depends on one or more anomaly anchors.

Its interior size does not need to correspond to ordinary exterior dimensions.

### RECONFIGURING_DUNGEON

A persistent place where semantic identity remains stable while room/corridor topology can change between layout instances.

The persistent layer stores:

- semantic anchors;
- historical discoveries;
- resolved objectives;
- permanent state changes;
- prior layout versions;
- entry/exit constraints.

The generated instance stores the current room graph and presentation.

### LOCAL_SPATIAL_ANOMALY

A bounded distortion inside an otherwise normal location. Examples can include a corridor that connects unexpectedly, a door with uncertain destination or a short-lived overlap between places.

### SUBJECTIVE_OR_DIGITAL_SPACE

These are not handled as anomalous physical realms by default.

- Dream or psychic spaces use `dreams-aura-psychic-information-layer.md`.
- Cyberspace/simulations use `digital-systems-cyberspace-data-layer.md`.

A later canon decision may connect systems, but no generator may merge them because their visuals happen to look strange.

## Persistent world-state objects

### ANOMALOUS_SPACE

```yaml
anomalous_space_id: null
space_class: STABLE_ALTERNATE_REALM | MIRROR_OR_ECHO_REGION | POCKET_SPACE | RECONFIGURING_DUNGEON | LOCAL_SPATIAL_ANOMALY
canon_status: proposed
persistent_identity: true
known_anchor_ids: []
semantic_anchor_ids: []
current_topology_version_id: null
known_inhabitant_ids: []
ecological_state_refs: []
research_program_refs: []
public_belief_refs: []
access_history_refs: []
chronicle_refs: []
mechanical_effect_refs: []
```

### ANOMALY_ANCHOR

Represents a physical or persistent point associated with a crossing.

```yaml
anchor_id: null
location_id: null
observed_state: DORMANT | ACTIVE | INTERMITTENT | UNKNOWN
activation_evidence_refs: []
opening_actor_refs: []
linked_portal_edge_ids: []
access_restriction_refs: []
last_verified_at: null
```

An anchor does not need to be the cause of an anomaly. It may only be where the anomaly is observed.

### PORTAL_EDGE

Represents one access relation between locations/spaces.

```yaml
portal_edge_id: null
origin_anchor_id: null
destination_space_id: null
destination_anchor_id: null
destination_certainty: UNKNOWN | PROBABLE | VERIFIED
state: CLOSED | OBSERVED_OPEN | STABILIZED | INTERMITTENT | LOST
activation_requirements: []
verified_eligible_actor_refs: []
verified_passenger_rules: []
verified_cargo_rules: []
return_policy_id: null
source_provenance_refs: []
```

Do not assume bidirectionality. `A → B` does not prove `B → A`.

### RETURN_CONTRACT

This is a safety and narrative-state object, not a legal contract.

```yaml
return_policy_id: null
portal_edge_id: null
return_guarantee: UNKNOWN | NO | CONDITIONAL | VERIFIED
known_return_anchor_ids: []
required_conditions: []
known_failure_modes: []
emergency_recovery_refs: []
last_tested_at: null
```

A generated expedition should not strand PCs permanently unless a human-approved canon scenario explicitly allows that risk.

### TOPOLOGY_VERSION

```yaml
topology_version_id: null
anomalous_space_id: null
generation_seed: null
semantic_graph_version: null
room_graph_ref: null
connectivity_validation: UNKNOWN | FAILED | VERIFIED
required_anchor_ids: []
entry_node_ids: []
objective_node_ids: []
exit_node_ids: []
created_at: null
supersedes: null
```

For generated layouts, `connectivity_validation` must be VERIFIED before player entry.

### SEMANTIC_ANCHOR

A persistent narrative/objective landmark whose identity survives topology changes.

Examples:

- an observation station;
- a shrine already discovered;
- a nesting chamber;
- an exit structure;
- a sealed research vault;
- a unique specimen site.

Its current room position can change only when the anomaly's authored rules permit it.

### CROSSING_RECORD

```yaml
crossing_id: null
portal_edge_id: null
actor_ids: []
pokemon_entity_ids: []
item_instance_ids: []
origin_time: null
arrival_time: null
return_crossing_id: null
witness_refs: []
mechanical_state_refs: []
```

This record is important for custody and duplication protection. An item or Pokémon crossing a portal remains the same persistent entity.

### SPATIAL_RULE_CLAIM

Researchers, witnesses or institutions may form claims such as:

- “the northern door changes destination after sunset”;
- “the space preserves one central chamber”;
- “both entrances lead to the same interior.”

These are claims with evidence, not automatic truth.

## Topology model for changing dungeons

Separate two layers.

Persistent semantic graph:

```text
ENTRY
  ↓
SURVEY HUB
  ├── OPTIONAL ARCHIVE
  └── REQUIRED KEY STATE
            ↓
       CORE CHAMBER
            ↓
           EXIT
```

Current spatial graph:

```text
rooms + corridors + doors + visual geometry
```

The spatial graph may vary. The semantic dependencies must remain satisfiable.

## Generation feasibility gate

Before committing a generated topology:

1. Confirm every required entry can reach the first required objective.
2. Confirm objective dependencies occur in legal order.
3. Confirm all required unique objects have reachable placements.
4. Confirm at least one authorized exit/recovery path.
5. Confirm no permanent world-state object exists only inside an unreachable disposable room.
6. Confirm player-specific access requirements do not make the generated solution impossible.
7. Store the generation seed and topology version for reproduction/debugging.

If validation fails, discard the candidate before the player sees it.

## Progression integrity

An anomalous connection must not silently bypass:

- Gym/League progression;
- faction access;
- custody or ownership restrictions;
- conservation closures;
- case/evidence permissions;
- dungeon completion state;
- settlement restrictions;
- ordinary Minecraft access gates;
- interregional recognition requirements.

If an anomaly intentionally creates an exception, the exception needs an authored access edge and consequence state.

## No automatic time travel

Altered or uncertain time perception does not prove time travel.

Store separately:

- departure timestamp;
- arrival timestamp;
- actor-reported duration;
- clock/device records;
- institutional interpretation.

The system must not create past/future selves, retroactive Chronicle edits or paradoxes without explicit canon approval.

## Entity duplication protection

Portal crossing cannot clone persistent entities by default.

For every crossing:

- Pokémon keep their `pokemon_entity_id`;
- unique items keep their item-instance ID;
- custody/ownership records follow the same object;
- the Chronicle records movement, not creation;
- a mirror-world visual copy is a separate entity only if canon explicitly creates one.

## Ecology across anomalous connections

A portal can create ecological consequences without being a combat hazard.

Possible states:

- temporary spillover observation;
- repeated crossings by the same Pokémon individual;
- new foraging route;
- pathogen/biosecurity concern without assumed diagnosis;
- local population avoidance;
- protected-area response;
- scientific monitoring;
- tourism pressure.

Do not spawn rare Pokémon merely because players intentionally manipulate anomaly state unless a validated ecological rule supports it.

## Legendary/Mythical protection

Spatial anomalies must not escalate automatically to Hoopa, Giratina, Palkia or another Legendary/Mythical explanation.

Valid chain:

```text
anomaly observed
→ measurements and witness reports
→ competing hypotheses
→ repeated evidence
→ species/Legendary hypothesis if justified
→ human canon approval
→ direct appearance only when explicitly approved
```

## PTU capability boundary

Python AutoPTU contains tactical recognition of `Phasing` and `Teleporter` in specific contexts, including grapple escape.

This does not authorize:

- making portals;
- world-to-world travel;
- selecting arbitrary destinations;
- moving a party through walls in the overworld;
- transporting cargo;
- bringing non-users through a teleport;
- bypassing route restrictions;
- escaping every dungeon;
- teleporting as an automatic battle reaction.

Any exact Teleporter/Phasing use must be checked against PTU/Caelo text and current engine implementation.

## Minecraft representation boundary

Minecraft may present:

- a portal visual;
- a separate dimension/instance;
- non-Euclidean-looking transitions;
- layout changes between visits;
- altered sky/light/biome presentation;
- spatial audio and particles;
- persistent anomaly markers.

Minecraft must not independently decide:

- who is mechanically allowed to teleport;
- forced movement;
- damage from anomaly contact;
- status application;
- time travel;
- item duplication;
- battle escape;
- destination selection governed by PTU rules.

## Encounter contract A — Folding Causeway

Narrative premise: a causeway inside an anomalous space appears to reconfigure between observation cycles. Players must cross to a stable survey anchor.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if platforms relocate actors or crossing triggers displacement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for timed reconfiguration;
- full stateful damage pipeline — PARTIAL if combat occurs;
- status lifecycle — PARTIAL if exact statuses occur;
- terrain/weather/hazards/zones/reactions — BLOCKING for disappearing platforms or active anomaly zones;
- move-specific behavior — PARTIAL when exact Moves interact with geometry;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for REACH_ANCHOR/WITHDRAW behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Use one validated static topology for the battle. Reconfiguration happens only between scenes or visits. A conventional encounter may occur on the causeway, but no tile disappears and no actor is moved by the anomaly. After combat, overworld state advances the expedition to the survey anchor.

## Encounter contract B — Portal Ecology Spillover

Narrative premise: several wild Pokémon are observed on the overworld side of an intermittent anomaly. Players need to understand whether this is a one-time crossing or a repeated ecological route.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if actors can cross/withdraw dynamically through the portal during battle;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if portal windows are timed;
- terrain/weather/hazards/zones/reactions — BLOCKING if the portal is an active grid zone;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for autonomous retreat/portal-seeking behavior;
- adapter/playback — BLOCKING.

Reduced version:

Resolve the crossing before battle as world state. Any Pokémon already on the ordinary side can enter a normal static encounter. The portal cannot be entered from the tactical grid. Capture/retreat results write back to the persistent Pokémon and ecological state.

## Encounter contract C — Mirror Facility Survey

Narrative premise: investigators enter a spatial echo of a known facility. The layout resembles the original, but records, occupants and object state do not automatically match.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if internal doors behave as live teleport edges;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for phase-sensitive transformations;
- terrain/weather/hazards/zones/reactions — BLOCKING if geometry changes during battle;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for investigation/protection objectives;
- adapter/playback — BLOCKING.

Reduced version:

Instantiate the mirror facility as a separate authored Minecraft location with fixed geometry for the visit. Any battle uses a static arena. Differences between the ordinary and mirror facility remain ordinary world-state facts, not combat modifiers.

## Encounter contract D — Reconfiguring Ruin Survey

Narrative premise: an old ruin retains three persistent semantic anchors while corridors differ on later expeditions.

This concept can be largely non-combat.

Required system work before procedural use:

- topology seed/version storage;
- semantic graph contract;
- connectivity validation;
- objective-to-exit feasibility validation;
- persistent-object placement protection;
- adapter support for instancing/rebuilding the layout.

If a battle occurs, it should use a frozen topology instance for the duration of the encounter unless terrain/hazard/reaction families become verified.

## Promotion checklist

Before anomalous-space content enters canon:

1. Space class is explicit.
2. Dream/digital/anomalous physical spaces are not conflated.
3. Portal origin and destination are independent state objects.
4. Return semantics are explicit.
5. Progression bypass is reviewed.
6. Persistent entities cannot duplicate through crossings.
7. No time travel is inferred from altered clocks or perception.
8. Legendary/Mythical causation remains unclaimed unless approved.
9. Generated layouts pass connectivity and objective feasibility checks.
10. Unique persistent objects survive topology changes safely.
11. PTU Teleporter/Phasing rules are checked before mechanical use.
12. Encounter capability dependencies use the permanent engine categories.
13. A reduced version exists when the full version relies on blocking capabilities.
14. Minecraft presentation does not implement missing PTU rules.
15. External inspiration is transformed and attributed in `research/`.
