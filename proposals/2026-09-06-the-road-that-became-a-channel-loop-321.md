# The Road That Became a Channel — Pass 321

Status: PROPOSED / NON-CANON
Date: 2026-09-06
Canon authority: NONE. Region, settlement names, institutions, species, historical events, and final explanation remain intentionally unassigned.

## Premise

A low causeway crosses a broad seasonal floodplain. For most of the recent travel season it has functioned as an ordinary route. After a high-water event, two apparently contradictory reports arrive.

One field crew reports that the road is dry enough to walk and that the main crossing is structurally present. Another reports fresh aquatic use, a reactivated side channel, debris above the road surface, and a section that should remain restricted.

The investigation is not 'which witness is lying?'. The player must determine which feature each report describes, when it was observed, what the flood actually changed, and what can safely reopen without erasing ecological or operational consequences elsewhere.

## Narrative objective

Make temporal and spatial provenance playable.

The player should finish able to distinguish:
- the historical floodplain from the water footprint of one event;
- evidence of past peak water from current inundation;
- dry surface from safe route;
- water present from mechanically dangerous current;
- one reopened feature from the state of the whole corridor;
- an observation from an interpretation;
- hidden world truth from what each NPC has actually received.

## Core locations

### The old survey rise

A stable elevated point with route markers and an old reference monument. It gives players a fixed spatial frame before they enter contradictory evidence.

Useful evidence:
- old route alignment;
- elevation reference;
- a view of the main causeway and side channel;
- a place to compare historical records with current geometry.

### The causeway crossing

The visible road may currently be dry or shallowly inundated depending on authored state. A previous peak left physical traces on fixed structures.

Useful evidence:
- mud/seed/debris line candidates;
- silt over road markings;
- scour near one shoulder;
- intact or damaged route marker;
- recent footprints or wheel traces only if authored and provenance-backed.

A high-water mark demonstrates a past level. It never directly sets the current water state.

### The culvert throat

A culvert or drainage opening controls whether floodwater leaves the road corridor efficiently. It can be open, partially obstructed, historically undersized, or simply irrelevant to the final cause.

Useful evidence:
- fresh debris against the inlet;
- sediment pattern downstream;
- maintenance record;
- evidence of recent clearing;
- mismatch between expected and actual flow path.

The culvert is a hypothesis generator, not an automatic culprit.

### The side channel / refuge strip

A low swale or old channel has recently carried water and may now support temporary habitat use. This can remain ecologically important even after the main road becomes usable again.

Useful evidence:
- fresh silt;
- waterline traces;
- deposited plant material;
- species observations if later canon-approved;
- evidence that the channel connected two habitat patches during the flood pulse.

### The downstream access fork

A feature-level decision becomes visible here. The main route can reopen while one spur stays closed, one refuge remains monitoring-only, or a temporary detour persists.

## People and institutional tensions

All roles are placeholders until canon approval.

A route steward wants a defensible reopening decision because the crossing matters to routine travel and supply movement.

A field ecologist or habitat observer wants recent side-channel use documented before maintenance erases the evidence.

A logistics operator cares about predictable access and may be correct that the main causeway is currently usable.

An upstream or downstream resident may care about where water is being redirected rather than whether the road itself is open.

A maintenance worker may remember a previous channel alignment or repair that is absent from current paperwork. Memory is evidence to investigate, not automatic truth.

No role requires corruption, incompetence, or villainy.

## Investigation loop

The player first receives two reports that appear incompatible.

The player establishes feature identity and semantic time for each report.

The player visits at least two fixed reference points rather than relying on one dramatic trace.

The player compares field evidence with one documentary source such as a gauge record, maintenance note, route inspection, or old survey.

The player formulates a provisional explanation.

A controlled action or later observation tests that explanation. Examples include clearing a small inspectable blockage, checking the same section after water recedes, comparing upstream/downstream observations, or revisiting after the next routine rise.

The final institutional action is scoped by feature rather than by the whole floodplain.

A later revisit shows which consequences persisted.

## Possible explanations

None is canon-approved.

The flood pulse followed the expected floodplain route, but the first report generalized from the dry causeway to the whole corridor.

A culvert blockage temporarily sent water across the road and reactivated an older side channel.

Recent maintenance improved road drainage while unintentionally reducing a temporary habitat connection.

Sediment from the event raised one shallow crossing enough to change where later water moved.

An older map omitted a small channel that has always activated above a certain water state.

Two events occurred close together, causing reports from different days to be treated as one snapshot.

A Pokémon species used the newly connected waterway, but only species-specific, canon-approved evidence may support that branch.

Several causes may coexist.

## Consequences

A successful investigation does not need to restore a single binary normal state.

Possible feature-scoped outcomes include:
- reopen the main causeway;
- keep a side spur restricted;
- schedule culvert monitoring rather than immediate replacement;
- preserve one temporary refuge until observations finish;
- revise signage or route notices;
- update the flood/maintenance record;
- create a seasonal detour protocol;
- compensate or reschedule affected deliveries through separate economic workflows if those systems are later connected;
- revise a prior closure without deleting the historical decision that caused it.

These outcomes should connect to existing decision dependency, review, consequence, and selective-repair systems rather than resetting the world.

## Reduced implementation version

Narrative premise remains intact with no tactical fluid simulation.

Use ordinary persistent route/feature IDs and scene-authored state such as:
- `DRY_OPEN`;
- `SHALLOW_RESTRICTED`;
- `INUNDATED_CLOSED`;
- `BYPASS_OPEN`;
- `MONITORING`.

Use provenance-backed observations such as:
- `HIGH_WATER_MARK_OBSERVED`;
- `FRESH_SILT_OBSERVED`;
- `DEBRIS_LINE_OBSERVED`;
- `CULVERT_BLOCKAGE_OBSERVED`;
- `SIDE_CHANNEL_ACTIVE_OBSERVED`;
- `GAUGE_RECORD_RECEIVED`;
- `PASSABILITY_UNRESOLVED`.

Water-state changes happen between scenes or through explicit authored world-state events.

Do not implement:
- current vectors;
- forced displacement;
- rising water during a tactical round;
- drowning;
- underwater/turbidity penalties;
- slipping status;
- environmental damage;
- rescue reactions;
- automatic species behavior;
- Move/Ability/Item/Feature effects inferred from flavor.

## Full mechanically rich version

A later full version may allow the same crossing to change during a tactical encounter through a scheduled rise/fall, active current sectors, debris movement, intermittently exposed footing, rescue/interception, weather-driven changes, or water-sensitive visibility.

Those additions are optional enhancements, not prerequisites for the story.

Exact capability dependencies:

Targeting / footprints / range / LoS: ordinary audited geometry is usable, but underwater visibility, turbidity, concealment through water, and elevation/water-surface interactions require separate verified support.

Base movement legality: ordinary audited movement can support the reduced route graph. Swimming, wading, special water traversal, or terrain costs must use verified PTU contracts before they become mechanical.

Complete movement including push/pull/knockback/interception/forced movement: required for current-driven displacement, rescue/interception, debris impact displacement, or any forced movement in water. Current status: PARTIAL.

Core calculations: ordinary deterministic arithmetic is verified within audited contracts. Hydrodynamic equations, current strength, water depth thresholds, or flood models are not engine rules.

Action economy / initiative: audited primitives can sequence already-legal actions. They do not define rescue, swimming, stabilization, or flood-control actions themselves.

Full turn / round lifecycle: required for timed rises/falls, scheduled flood pulses, delayed debris, changing water sectors, or round-boundary hydrologic effects. Current status: PARTIAL.

Full stateful damage pipeline: required if the full version authors drowning, crushing, debris impact, fall, or other environmental battle damage. Current status: PARTIAL.

Status lifecycle: required only if a real persistent PTU condition is used. Narrative water-state labels are not statuses. Current status: PARTIAL.

Terrain / weather / hazards / zones / reactions: required for active current zones, rain-driven changes, water boundaries, rescue reactions, dynamic footing, and related hazard behavior. Current status: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior: every Move used for water manipulation, weather, rescue, terrain change, or combat must be individually verified. Current status: PARTIAL.

Abilities: every Ability interaction must be individually verified. Pokédex ecology grants no tactical Ability behavior. Current status: PARTIAL.

Items: ropes, flotation, pumps, gauges, protective equipment, held items, or other rules-level tools require exact evidence. Current status: PARTIAL.

Trainer Features / perks: Survival, rescue, navigation, weather, terrain, or intervention Features require individual verification. Current status: PARTIAL.

AI legal-action infrastructure: usable once exact actions and environmental legality exist. It does not infer flood semantics. Current status: VERIFIED within audited contracts.

AI tactical policy: autonomous current navigation, rescue prioritization, evacuation, hazard avoidance, and dynamic crossing strategy remain blocking for generalized policy.

Minecraft / Cobblemon / Craftics adapter/playback: may render water, silt, debris, signs, barriers, routes, and animation. It must not infer current, damage, PTU legality, route authority, ecological truth, or NPC knowledge from blocks or particles. End-to-end dynamic flood playback remains PARTIAL / BLOCKING.

## Canon questions intentionally unresolved

Region and river system.

Why the causeway exists and who maintains it.

Flood seasonality and historical baseline.

Whether the side channel is natural, engineered, or both across different eras.

Which communities rely on the crossing.

Which Pokémon, if any, use the temporary connection.

The final causal explanation.

Any PTU/Caelo rule for Swim, current, drowning, rough/water terrain, visibility, rescue, weather, Move behavior, Ability behavior, Item behavior, or Trainer Features.
