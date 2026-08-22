# Pokémon-Built Structures & Ecosystem Engineering Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 95

## Purpose

This layer represents persistent physical structures created, maintained, abandoned or reused by Pokémon.

It owns structure identity, builder attribution, construction history, maintenance history, occupancy state, abandonment, reuse, coarse physical condition and evidence-backed ecological consequences.

It does not own the downstream systems themselves. Hydrology owns water-regime change. Soil owns erosion/compaction. Flora owns vegetation response. Wild Collectives owns persistent groups. Infrastructure owns human-built systems. Architecture owns authored buildings. Conservation owns stewardship decisions. AutoPTU owns battle rules.

## Authority boundary

Keep these separate:

builder species lore -> observed construction behavior -> structure identity -> physical revision -> environmental response observations -> interpretation -> management decision -> future revision -> Minecraft projection -> optional battle snapshot.

Examples:

- a Bibarel dam can exist without being a battle obstacle;
- a raised water level does not prove the dam caused it unless the evidence graph supports that conclusion;
- an underground tunnel does not prove Excadrill built it;
- a colony nest does not grant tactical bonuses;
- abandoned does not mean ownerless or safe to dismantle;
- damage to a structure does not prove malicious action;
- a player removing blocks does not erase the structure's Chronicle history.

## POKEMON_BUILT_STRUCTURE

```yaml
pokemon_built_structure_id: null
structure_class: dam|lodge|burrow|tunnel_network|nest|colony_nest|hive_or_wall|silk_bridge|mound|cache|shelter|other|unknown
location_ref: null
footprint_ref: null
vertical_extent_ref: null
builder_attribution_ids: []
physical_revision_ids: []
construction_event_ids: []
maintenance_event_ids: []
occupancy_revision_ids: []
disturbance_event_ids: []
reuse_event_ids: []
environmental_effect_refs: []
heritage_refs: []
canon_status: proposed
```

A structure can persist after its original builder leaves or dies. It is not the same object as the Pokémon that built it.

## BUILDER_ATTRIBUTION

```yaml
builder_attribution_id: null
structure_id: null
candidate_entity_refs: []
candidate_collective_refs: []
candidate_species_refs: []
attribution_class: observed_directly|strongly_supported|possible|disputed|unknown
observation_refs: []
media_refs: []
source_refs: []
confidence: null
supersedes_id: null
```

Do not infer builder from species presence alone.

## STRUCTURE_PHYSICAL_REVISION

```yaml
structure_physical_revision_id: null
structure_id: null
observed_at: null
condition_class: active_intact|active_damaged|inactive_intact|inactive_damaged|partially_collapsed|collapsed|removed|reworked|unknown
footprint_ref: null
material_refs: []
openings_refs: []
chamber_refs: []
water_control_ref: null
surface_connection_refs: []
source_refs: []
supersedes_id: null
```

This is coarse world geometry. It does not create structure HP, cover or movement cost by itself.

## CONSTRUCTION_EVENT

```yaml
construction_event_id: null
structure_id: null
started_at: null
ended_at: null
builder_entity_refs: []
builder_collective_refs: []
observed_actions: []
material_source_refs: []
observation_refs: []
result_revision_id: null
```

Construction time remains unknown unless actually observed or authored.

## MAINTENANCE_EVENT

```yaml
maintenance_event_id: null
structure_id: null
observed_at: null
actor_entity_refs: []
actor_collective_refs: []
maintenance_type: patch|reinforce|expand|clear_opening|replace_material|reopen_passage|other|unknown
observation_refs: []
result_revision_id: null
```

Repeated maintenance can be used to infer continuing use, but it does not prove ownership.

## OCCUPANCY_REVISION

```yaml
occupancy_revision_id: null
structure_id: null
observed_at: null
occupancy_class: occupied|seasonally_occupied|partially_occupied|vacant|abandoned|reused|unknown
occupant_entity_refs: []
occupant_collective_refs: []
indirect_sign_refs: []
source_refs: []
confidence: null
supersedes_id: null
```

Vacant and abandoned are distinct. A structure can be empty during one survey and occupied later.

## STRUCTURE_FUNCTION_ASSESSMENT

```yaml
structure_function_assessment_id: null
structure_id: null
valid_period_ref: null
function_claims:
  - nesting
  - shelter
  - nursery
  - storage
  - water_control
  - transit
  - predator_defense
  - display
  - resource_processing
  - unknown
evidence_refs: []
assessment_status: supported|possible|unsupported|insufficient_data|unknown
reviewer_ref: null
supersedes_id: null
```

Function is evidence-backed. A chamber containing eggs supports nursery use; an empty chamber does not.

## ENVIRONMENTAL_EFFECT_LINK

```yaml
environmental_effect_link_id: null
structure_id: null
effect_domain: freshwater|soil|flora|wild_collective|road_ecology|stormwater|decomposition|other
observation_refs: []
causal_hypothesis_ref: null
verified_effect_ref: null
valid_period_ref: null
confidence: null
```

The effect itself remains owned by the receiving layer.

Example:

Bibarel dam -> Hydrology water-regime revision -> Soil sediment observation -> Flora recruitment change -> Wild Collective route change.

This layer only preserves the structure as a common causal candidate and provenance anchor.

## DISTURBANCE_EVENT

```yaml
disturbance_event_id: null
structure_id: null
occurred_at: null
disturbance_class: storm|flood|fire|construction|vehicle|deliberate_removal|battle_nearby|unknown
observed_damage_refs: []
cause_claim_refs: []
result_revision_id: null
```

A battle nearby does not mean the battle damaged the structure unless an authoritative result says so.

## REUSE_EVENT

```yaml
reuse_event_id: null
structure_id: null
occurred_at: null
previous_occupancy_ref: null
new_user_entity_refs: []
new_user_collective_refs: []
reuse_class: shelter|nesting|storage|crossing|research_site|heritage_site|salvage_source|other|unknown
source_refs: []
```

Abandoned Pokémon structures can become habitat for other species, research sites or human landmarks.

## REMOVAL / ALTERATION REVIEW

Any deliberate removal should record:

```yaml
structure_alteration_review_id: null
structure_id: null
proposal_ref: null
reason: infrastructure_conflict|flood_risk|safety|habitat_restoration|research|access|other|unknown
stakeholder_refs: []
ecology_refs: []
infrastructure_refs: []
heritage_refs: []
decision_ref: null
result_revision_ref: null
```

This does not define legal authority. Civic Governance, Conservation and local canon decide who can act.

## Minecraft projection

Minecraft can project:

- dam blocks;
- lodge entrances;
- burrow mouths;
- tunnel segments;
- colony chambers;
- nest materials;
- signs of maintenance;
- partial collapse;
- abandoned/reused visual variants.

The server-owned structure record remains authoritative.

Block edits must become proposed structure revisions. A chunk reload must never restore an obsolete version merely because a schematic exists.

## Cobblemon projection

Cobblemon may project only a bounded subset of persistent occupants or builders.

Loaded Pokémon counts never define:

- population size;
- builder identity;
- occupancy truth;
- colony membership;
- structure function.

If a persistent entity is important, retain its entity ID through the existing Pokémon-agency layer.

## Encounter contracts

### Dam Maintenance Conflict

Narrative premise:
A stream crossing used by a settlement has changed after a Pokémon-built dam was expanded. The builders are actively maintaining it while travelers need passage.

FULL version:
- water zones can change during battle;
- actors can attempt CROSS / WITHDRAW / PROTECT_STRUCTURE;
- damage to a supported object can alter geometry;
- forced movement/current rules exist;
- tactical AI can prioritize maintenance, retreat and defense rather than KO.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if any status is used;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
Resolve water level and safe crossing geometry before battle. The dam remains outside tactical destructibility. If a confrontation occurs, AutoPTU receives a static bank/shore arena and only real combatants. Afterward, world-state choices can alter, preserve or reroute around the structure.

### Tunnel Breakthrough Survey

Narrative premise:
A construction crew opens into an older underground Pokémon tunnel network. The immediate question is whether the route is occupied and how it connects to nearby infrastructure.

FULL version:
- new openings can appear during encounter execution;
- actors can retreat through multiple exits;
- collapse/blocked-route state can change;
- tactical AI understands EXIT / PROTECT_NURSERY / WITHDRAW;
- vertical or multi-level movement is supported.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED for frozen geometry;
- base movement legality: VERIFIED;
- complete movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- tactical AI: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:
Survey and occupancy checks happen in overworld state. Freeze one safe chamber as the arena. Collapses, workers, nursery chambers and newly discovered side tunnels remain outside battle resolution.

### Colony Nursery Perimeter

Narrative premise:
A deep colony nest overlaps a proposed public-works corridor. Surveyors need evidence of active use before any decision is made.

FULL version:
- colony members move between chambers;
- protection and withdrawal objectives exist;
- eggs/juveniles are protected world objects rather than HP targets;
- tactical AI recognizes nonlethal disengagement;
- tunnels can constrain or open routes dynamically.

REDUCED version:
Eggs and juveniles never enter the grid. Survey state is resolved first. Any battle uses a static perimeter and updates only combat outcomes. Occupancy and infrastructure decisions remain world-state work.

## Narrative generation rules

Allowed:
- structure discovered before builders are known;
- conflicting builder-attribution hypotheses;
- construction changing another layer over time;
- maintenance occurring while players are absent;
- old structures being reused by other Pokémon;
- structure removal creating later ecological consequences;
- human infrastructure adapting around Pokémon construction;
- builders adapting to human infrastructure.

Forbidden without authored/mechanical support:
- assuming human-like architecture or motives;
- assigning ownership from occupancy;
- declaring a structure safe because it looks stable;
- applying environmental combat effects from flavor;
- generating shared colony buffs;
- treating all builders as hostile when their structure causes a conflict;
- deleting provenance when a structure is abandoned or altered.

## Long-term value

This layer gives Ouros an important kind of causality: Pokémon can physically shape the world before players arrive, while players are elsewhere and after they leave.

The result is a landscape whose history is partly written by Pokémon themselves rather than a static human-built map decorated with wild spawns.
