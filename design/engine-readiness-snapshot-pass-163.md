# Engine Readiness Snapshot — Pass 163

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `804860a180fb94e52d98d5d87c1a407663827cc1`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`8d7fb85c24c71940228dd2064123509c9a24ed69` — merged PR #301, `Freeze forced movement runtime ordering context`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No engine file was modified by Pass 163.

## New Java evidence — PR #301

PR #301 extends the contract freeze introduced by PR #300.

The inspected commit now freezes not only the inventory of Python forced-movement callsites but also the local execution-order context around the runtime callsite in `auto_ptu/rules/battle_state.py`.

The contract records:

- the enclosing function;
- the statement containing `forced_movement_instruction`;
- the containing statement block;
- the immediately previous statement;
- the immediately following statement.

The Java contract still asserts that production sources contain no calls to `RuntimeForcedMovementMoveApplication.apply` outside its implementation class. The assertion text remains explicit that Java forced-movement ordering must remain unbound until the pinned `battle_state` order is frozen.

This is positive parity infrastructure because the future Java binding now has a more precise Python ordering contract to match.

It is also explicit evidence that complete forced movement is not production-bound in Java yet.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 163.

## Why complete movement remains PARTIAL

Positive evidence accumulated before this pass includes:

- shared targeting/line geometry;
- server-owned Intercept candidate discovery and attempt planning;
- canonical combatant rule content for Intercept;
- authoritative generic Push/Pull move metadata;
- target and anchor revalidation before forced displacement;
- shared displacement and partial-stop behavior for tested branches;
- a server-owned forced-movement Ability modifier path with tested Thrust behavior;
- a frozen Python runtime callsite inventory;
- now, a frozen local execution-order context around that callsite.

Still not globally verified:

- production Java runtime binding of `RuntimeForcedMovementMoveApplication.apply`;
- parity of the complete ordering once Java is bound;
- every Push source;
- every Pull source;
- general Knockback;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from status, terrain, weather, Features, Items or other sources;
- escort/rescue;
- protected-object carrying;
- crowd routing;
- moving vehicles/platforms;
- generalized reaction windows;
- dynamic tactical objectives.

Therefore none of the mechanically rich research-site encounters may rely on complete movement today.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes viewport coordinate synchronization as presentation-only and says no battle rule or outcome changes.

It provides no new evidence for the permanent tactical categories in this pass.

## PTU/Caelo scientific-research boundary

Internal source priority remains:

- PTU Core Rulebook;
- Pokédex material;
- Caelo Player's Guide;
- Caelo rulebook / errata;
- character-creation material;
- Caelo Region Location & Encounter List.

Public PTU references confirm that Researcher and Scientist are real mechanical surfaces with explicit prerequisites and effects. That increases the need for a conservative boundary rather than authorizing generic “science” bonuses.

UNKNOWN until exact project-source and implementation review:

- universal scientific-research Skill Checks;
- generic experiment or hypothesis DCs;
- Researcher branch changes in Caelo;
- Scientist changes in Caelo;
- generic research XP or Trainer XP;
- automatic Skill Edge, Feature or Tutor rewards from completed studies;
- universal sampling mechanics;
- tagging or telemetry mechanics;
- generic tranquilization procedures;
- laboratory crafting outside exact PTU/Caelo Features;
- generic sensor behavior from Moves or Abilities;
- Pokémon Type granting measurement or laboratory capabilities;
- Pokédex registration proving a scientific claim;
- Aura/Psychic/Telepathy proving truth;
- sample collection granting ownership;
- any Caelo publication, research-institution or academic procedure.

The Pass 163 layer is therefore narrative/evidentiary world state unless a specific mechanic is separately validated.

## Encounter A — Field Observation Perimeter Incident

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected attacks require
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active field conditions matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/site-control semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic field-team and equipment playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level when selected ordinary combat content is individually audited.

Before initiative, Ouros terminates collection and removes researchers, instruments and noncombat research subjects from BattleSpec. Static geometry only. Permitted tactical output: `IMMEDIATE_FIELD_SITE_APPROACH_CLEAR`.

Forbidden inference:

`BATTLE_WON != DATA_COLLECTION_COMPLETED`

`BATTLE_WON != HYPOTHESIS_SUPPORTED`

`BATTLE_LOST_WITHOUT_RESCUE_CONTRACT != RESEARCHERS_HARMED`

## Encounter B — Sample Transfer Chokepoint

Full version requires protected-object carrying/escort semantics, complete movement, lifecycle, objective-aware AI and semantic adapter playback.

Overall full status: BLOCKED.

Reduced status: READY.

The sample, container and custody state remain outside BattleSpec. Transport pauses before initiative. Players may clear a static corridor and return only `IMMEDIATE_SAMPLE_ROUTE_CLEAR`.

`IMMEDIATE_SAMPLE_ROUTE_CLEAR != SAMPLE_DELIVERED`

`SAMPLE_DELIVERED != ANALYSIS_COMPLETE`

`BATTLE_WON != CUSTODY_TRANSFERRED`

## Encounter C — Research Station Power Isolation Perimeter

Full version may require dynamic electrical/environmental hazards, zones, reactions, changing equipment state, lifecycle and objective-aware AI.

Overall full status: BLOCKED.

Reduced status: READY.

Infrastructure state is frozen by the owner system before initiative. Staff and equipment are outside BattleSpec. The battle may return only `IMMEDIATE_RESEARCH_STATION_ACCESS_CLEAR`.

`BATTLE_WON != POWER_RESTORED`

`POWER_RESTORED != DATA_RECOVERED`

`ACCESS_CLEAR != EXPERIMENT_RESUMED`

## Encounter D — Wildlife Tagging Support Incident

A full version depends on the exact tagging procedure.

Potential required families include:

- action economy/initiative;
- status lifecycle;
- move-specific behavior;
- items;
- Trainer Features/perks;
- complete movement;
- capture or other exact PTU mechanics not represented by a generic narrative verb;
- AI tactical policy if protection/withdrawal matters;
- adapter/playback for semantic tagging state.

Overall full status: BLOCKED unless every exact mechanic used by the authored procedure is verified.

Reduced status: CONDITIONAL READY only when the research observation/tagging episode happens entirely outside BattleSpec before or after a conventional audited battle.

`POKEMON_VISIBLE != TAGGING_AUTHORIZED`

`BATTLE_WON != POKEMON_TAGGED`

`POKEMON_DEFEATED != SAMPLE_OBTAINED`

`TAGGING_COMPLETED != OWNERSHIP_CHANGED`

## Noncombat readiness

The core Pass 163 architecture is READY as narrative world-state design because it can operate without battle rules:

- research question history;
- project portfolios;
- method/protocol versions;
- links to Observation events;
- links to samples/specimens owned by other systems;
- dataset versions;
- analysis provenance;
- scoped scientific claims;
- review episodes;
- publication lineage;
- replication links;
- corrections/retractions/supersession;
- downstream reliance and reassessment;
- null/negative findings.

All concrete generated content remains NON-CANON until reviewed.

## AI boundary

AI legal-action infrastructure remains VERIFIED.

AI tactical policy remains BLOCKING for rich research incidents because legal-action enumeration does not prove that an actor understands goals such as:

- protect a field-team exit rather than maximize damage;
- withdraw without disturbing a research subject;
- protect equipment that is not a legal combat target;
- stop contesting after access is clear;
- avoid damaging a sample or instrument;
- escort an actor or object through a route.

Scientific value or project priority must never substitute for tactical policy.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon/Craftics may display already-authoritative:

- laboratories;
- field stations;
- researchers and assistants;
- notebooks and displays;
- sample containers;
- preserved specimens;
- instruments;
- monitoring stations;
- publication boards;
- project status changes.

It may not derive:

- research truth from visible entities;
- sample provenance from item skin/NBT alone;
- authorization from physical access;
- dataset membership from loaded entities;
- scientific claims from animations;
- publication acceptance from a UI screen;
- replication success from repeated Minecraft behavior;
- ownership from specimen possession;
- combatants from research-subject presence;
- PTU bonuses from laboratory machinery;
- weather/hazard battle state from Minecraft presentation when AutoPTU has not authored it.

Adapter/playback remains BLOCKING as a permanent category.

## Canon questions unresolved

- Which research institutions exist in Ouros canon?
- Which fields and long-running projects are active?
- Which labs, field stations and research collections map to existing locations?
- Which local actors can authorize collection or access?
- How are wild Pokémon observations and any physical samples handled?
- Which PTU/Caelo Researcher and Scientist mechanics are adopted exactly?
- What Caelo-specific changes exist for Researcher fields, Scientist, Education Skills or crafting?
- Do any regions use formal peer review?
- How are results published and distributed?
- Which correction, supersession or retraction procedures exist?
- Are there protected research locations or sensitive ecological records?
- Which current Chronicle facts create the first canon knowledge gaps?
- Which monitoring technologies exist without inventing Move/Ability effects?
- When may a research project safely produce a BattleSpec, and which actors are actual combatants?

## Pass 163 conclusion

Ouros can safely advance scientific worldbuilding now as provenance-rich noncombat state. Projects can accumulate observations, samples, dataset versions, analyses, claims, publications, replications and corrections without giving Narrative authority over PTU mechanics.

PR #301 improves the forced-movement parity contract by freezing local runtime ordering context around Python's callsite. It does not bind Java forced movement into production runtime and does not justify a capability promotion. Rich field evacuation, sample escort, dynamic laboratory hazards and tagging-in-combat remain blocked by the exact permanent capability families they require.