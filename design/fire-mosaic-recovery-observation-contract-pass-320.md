# Fire mosaic and recovery observation contract — Pass 320

Status: DESIGN CONTRACT / NON-CANON WORLD CONTENT

Date: 2026-09-06

## Purpose

Define a reusable Ouros boundary for landscapes affected by fire or comparable patchy disturbance. The contract prevents presentation, broad event records, or one observation from becoming omniscient local truth.

The contract supports investigation, access decisions, ecological monitoring, recovery revisits, NPC reasoning, and optional later AutoPTU encounters.

## Core invariant

`EVENT_FOOTPRINT != LOCAL_SEVERITY != CURRENT_FEATURE_STATE != NPC_KNOWLEDGE != NPC_INTERPRETATION`

A broad fire perimeter says that a place was within the disturbance footprint. It does not prove how intensely every patch burned, whether a route is currently usable, whether a habitat refuge exists, or what an NPC knows.

## Required state layers

### Disturbance event record

Stores durable historical facts such as:
- event ID;
- semantic time range;
- known or unresolved origin classification;
- broad footprint reference;
- source/provenance;
- later revisions.

The event record remains historical after recovery.

### Patch / feature identity

The affected landscape is divided into meaningful persistent features, not arbitrary combat tiles. Examples:
- route segment;
- drainage strip;
- ridge patch;
- surviving canopy island;
- service track;
- settlement edge;
- monitoring plot;
- emergency-access corridor.

Feature boundaries may be authored at world scale and projected into Minecraft.

### Observation record

An observation must include:
- observer or instrument;
- semantic time;
- feature/location reference;
- channel of observation;
- observed content;
- confidence/quality when available;
- provenance/source root;
- whether the observation is direct or relayed.

Examples of valid content:
- visible canopy loss;
- surviving cover;
- route obstruction;
- recent regrowth;
- track/sign presence;
- repaired marker;
- sediment or debris evidence;
- smoke seen at a distance;
- historical map notation.

Observation labels are evidence. They are not PTU statuses.

### Interpretation record

Interpretation is a claim derived from observations. It may include:
- inferred severity;
- inferred cause;
- inferred safety;
- inferred habitat value;
- inferred recurrence risk;
- inferred route usability.

Interpretations retain their evidence references and can be revised without deleting prior claims.

### Operational feature state

Examples:
- `OPEN`;
- `RESTRICTED`;
- `CLOSED`;
- `MONITORING`;
- `ACCESS_PENDING_REVIEW`.

This state comes from an authorized world decision/consequence path. It does not come from block appearance or an NPC opinion.

### Ecological monitoring state

Examples may include authored descriptors such as:
- `REFUGE_OBSERVED`;
- `REGENERATION_OBSERVED`;
- `USE_BY_SPECIES_OBSERVED`;
- `RECOVERY_UNRESOLVED`.

These remain observation/management data unless an explicit ecology subsystem contract gives them stronger semantics.

## Knowledge and belief boundary

Named NPCs learn fire/recovery information only through:
- their own observation;
- explicit private delivery;
- explicit public publication receipt;
- archive lookup or other external evidence path already allowed by the global NPC memory system.

A route authority can know a closure exists without knowing why one refuge patch survived.

A researcher can know that one patch regenerated without knowing whether a route has been legally reopened.

A resident can remember pre-fire conditions while lacking current field evidence.

No faction membership creates shared awareness.

## Spatial-scale boundary

Every disturbance assertion must have a scale.

Examples:
- whole-event footprint;
- landscape sector;
- persistent feature;
- local observation point;
- tactical zone.

Do not promote a statement made at one scale to another without evidence.

`INSIDE_EVENT_PERIMETER != HIGH_SEVERITY_PATCH`

`HIGH_SEVERITY_PATCH != CURRENTLY_IMPASSABLE`

`GREEN_PATCH != SAFE_ROUTE`

## Temporal boundary

Recovery state changes through semantic time.

A valid record may preserve:
- pre-event baseline;
- immediate aftermath;
- first survey;
- first reopening decision;
- seasonal or scheduled revisit;
- later disturbance;
- revised assessment.

Later recovery never deletes earlier disturbance history.

## Decision integration

Feature-level access or management decisions should use the existing global NPC decision chain:
- evidence available to actor;
- assessment;
- decision;
- consequence;
- later correction/review when new evidence arrives;
- selective repair of only affected consequences.

Reopening one route must not automatically clear every closure, remove every notice, restore every social consequence, or mark every patch recovered.

## Reduced implementation contract

The reduced implementation is valid when dynamic environmental mechanics are unavailable.

Use:
- persistent feature IDs;
- authored route states;
- between-scene state changes;
- semantic-time observation records;
- provenance-backed NPC knowledge;
- static Minecraft projection;
- deterministic consequences.

Do not require:
- spreading fire;
- smoke simulation;
- dynamic hazard propagation;
- Burn application;
- environmental damage;
- weather-driven changes within combat;
- forced movement;
- rescue reactions;
- tactical fire-response AI.

## Full tactical implementation boundary

A full active-fire or flare-up encounter may exist only when its required mechanics are verified.

### Targeting / footprints / range / LoS

Existing audited geometry can support ordinary targeting. Smoke/obscurement modifying visibility is a separate subfamily and must not be inferred from visual particles.

### Base movement legality

Existing audited movement can support ordinary open terrain. Debris, steep terrain, temporary barriers, fire lines, or special traversal require exact rules when they alter legality or cost.

### Complete movement

Required for authored push/pull/knockback/interception/forced evacuation/rescue movement. A flame animation never causes displacement by itself.

### Core calculations

Existing deterministic arithmetic remains authoritative where applicable. This contract defines no fire spread, heat, fuel, smoke concentration, ecological recovery, or suppression formula.

### Action economy / initiative

Existing primitives can sequence validated response actions. This contract does not create firefighting, evacuation, stabilization, or rescue actions by itself.

### Full turn / round lifecycle

Required for timed ignition, flare-up, spread, zone expiration, weather transition, delayed collapse, or other environmental effects tied to round/turn phases.

### Full stateful damage pipeline

Required for any fire, smoke, impact, collapse, or related environmental damage.

### Status lifecycle

Required for Burn or any other persistent condition. Narrative labels such as `SMOKE_OBSERVED` are never statuses.

### Terrain / weather / hazards / zones / reactions

Required for dynamic fire sectors, smoke zones, changing weather effects, terrain hazards, reactive rescue, or other mechanically active environmental fields.

### Move-specific behavior

Every Move used for ignition, suppression, weather, clearing, terrain alteration, rescue, or combat requires individual verification.

### Abilities

Every Ability interaction with fire, heat, weather, smoke, terrain, rescue, or damage requires individual verification.

### Items

Rules-level protective equipment, suppression tools, detection gear, held items, or rescue equipment require item evidence.

### Trainer Features / perks

Specialized fire response, hazard mitigation, weather control, rescue, interruption, or tactical modification requires individually sourced Features/perks.

### AI legal-action infrastructure

Can enumerate legal actions only after the relevant action and environmental contracts exist.

### AI tactical policy

General autonomous evacuation, suppression prioritization, rescue, hazard anticipation, and dynamic-zone navigation remain blocked until policy coverage exists.

### Minecraft / Cobblemon / Craftics adapter/playback

May present:
- charred/regrowing terrain;
- smoke/fire visuals;
- route barriers;
- NPC response animation;
- Pokémon movement/animation;
- changing world props.

May not decide:
- PTU damage;
- Burn;
- LoS penalties;
- forced movement;
- action legality;
- hazard timing;
- event cause;
- species behavior;
- route authority;
- NPC belief.

## Species evidence boundary

Official Pokédex behavior may support a hypothesis or ecological candidate. It does not create PTU mechanics.

For example, official Fletchinder behavior can justify considering local ember-scattering behavior as a narrative possibility if that species is later regionally enabled. It does not establish ignition probability, hazard radius, spread, culpability, or immunity.

## PTU / Caelo / Kairos boundary

Current repository source inventory exposes `sources/kairos` and no adopted `sources/caelo` directory.

Kairos references route readers toward PTU movement/terrain, status, hazards, terrain/weather, and encounter sections, but the source index explicitly warns that Kairos/homebrew rules are not automatically Ouros rules.

Before enabling tactical fire mechanics, verify the active Ouros rules profile and current AutoPTU contracts for every relevant family.

## Canon boundary

This contract authorizes architecture only. It does not establish an Ouros fire history, fire regime, vegetation community, regional climate, settlement, institution, species population, hazard, or quest outcome.
