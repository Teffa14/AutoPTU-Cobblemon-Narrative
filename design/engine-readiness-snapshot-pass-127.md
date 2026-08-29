# Engine Readiness Snapshot — Pass 127

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

This is unchanged from Pass 126.

The bounded Intercept route still demonstrates:

- PRE-target runtime integration;
- successful interceptor movement to the resolved position;
- effective-defender replacement before authoritative Move resolution;
- Acrobatics and Athletics derived from server-owned `CombatantRuleContent`;
- Coaching automatic-success state derived from server-owned temporary effects;
- exact `Justified [Errata]` detection and its pinned +4 Intercept modifier derived from server-owned Ability state;
- similarly named `Justified` does not satisfy that exact contract;
- the input factory remains core-internal;
- terrain remains an explicit internal input whose authoritative environment contract has not been frozen.

This still does not establish broad movement, reaction, Ability, Feature or terrain coverage.

AutoPTU current head: `2991a5492306678d49629d2001f076852032c4b0` — `Career: repair whitespace-corrupt recovered lineup ids (#236)`.

Compared with Pass 126 head `91b15a2efc0d762fc87937b2514095bb4937d5f8`, this Career slice trims persisted active-roster IDs before deduplication and Pokémon lookup, drops blank IDs, preserves valid order and adds regression coverage. It is persistence/browser-recovery hardening and provides no tactical battle coverage.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No capability family is promoted in Pass 127.

## Why the Intercept work remains PARTIAL evidence

A representative Intercept path now has substantially stronger authority boundaries than earlier passes. That evidence is valuable but narrow.

Still outside verified scope:

- broad Push;
- broad Pull;
- broad Knockback;
- every forced-movement source;
- every Intercept timing/window;
- environmental displacement;
- edge/fall displacement;
- generalized competing reactions;
- generalized reaction ordering;
- broad terrain authority;
- all Ability registrations and interactions;
- all Trainer Feature registrations and interactions;
- broad Item behavior;
- objective-aware AI tactical policy;
- semantic adapter playback.

Narrative encounter contracts must continue naming these exact dependencies when used.

## Pass 127 narrative readiness

The settlement/wild-Pokémon coexistence response extension is primarily world-state, provenance, institutional-handoff and observation infrastructure.

READY without new tactical capability:

- coexistence-case identity and chronology;
- bounded resident/staff/visitor reports;
- verification state separate from testimony;
- versioned subject scope;
- species-supported versus individual-supported identity;
- impact claims separated from cause;
- competing cause hypotheses;
- stakeholder positions;
- owner-system handoffs;
- mitigation proposals and implementation references;
- follow-up observation;
- recurrence/reopening history;
- public-safe summaries;
- closure with unresolved causality;
- facility/waste/schedule/access changes executed by existing owner systems;
- stable coexistence outcomes where the wild Pokémon remains present;
- mysteries based on chronology, identity confidence and monitoring gaps.

The following proposal seeds are READY as narrative/world-state content when instantiated against local canon:

- `The Same Bin Every Tuesday`;
- `The Nest Above Door Three`;
- `The Drain Noise Has Three Owners`;
- `The Pokémon Everyone Calls Back`;
- `The Store Fixed the Hole, the Alley Got Busier`;
- `The Market Opened Earlier, the Pokémon Did Too`;
- `The Roof Camera Changed the Story`;
- `Three Reports, Zero Damage`;
- `The Damage Is Real, the Culprit Is Not`;
- `Five Times the Pokémon "Came Back"`;
- `Four Doors, One Broken Screen`;
- `The Quiet Week`;
- `The Alley With Three Generations of Gates`;
- `The Underpass Everyone Stopped Using`;
- `A District Learns Who Shares Its Edges`.

A generic relocation workflow is not automatically READY because authority, capture/restraint method, welfare process and destination rules remain canon/mechanics dependent. The record structure is ready; execution is conditional.

## Encounter readiness — Service Yard Withdrawal

Narrative premise: an unrelated hostile encounter begins while staff are leaving a coexistence-investigation service yard.

Targeting/footprints/range/LoS — VERIFIED baseline.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL for active staff escort, Intercept or forced displacement.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL if staff withdrawal or service shutdown advances through staged turns.

Full stateful damage pipeline — PARTIAL for selected exact governed combat effects.

Status lifecycle — PARTIAL for selected exact governed statuses.

Terrain/weather/hazards/zones/reactions — BLOCKING for protected withdrawal corridors, crossing reactions, dynamically changing safe areas or environmental displacement.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL. Current `Justified [Errata]` evidence is only one exact Intercept interaction.

Items — PARTIAL.

Trainer Features/perks — PARTIAL. Current Coaching evidence is only one exact Intercept interaction.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW objectives.

Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic staff withdrawal, paused service state and coexistence-objective playback.

Reduced form: READY.

Before BattleSpec creation:

- finish staff withdrawal in authoritative Ouros world state;
- secure records and controlled equipment;
- pause service operations;
- keep noncombatants outside BattleSpec;
- keep the coexistence-case Pokémon outside BattleSpec unless Ouros independently selects it as an explicit legal combatant;
- use static reviewed geometry.

Battle victory may secure immediate access. It cannot identify the subject, prove the source of damage, authorize removal, complete relocation or reopen the facility.

## Encounter readiness — Nesting Roof Access Perimeter

Narrative premise: a restricted roof/nesting scope remains protected while a separate hostile encounter threatens its access perimeter.

Targeting/footprints/range/LoS — VERIFIED baseline for static geometry. Dynamic smoke, weather or visibility is not implied.

Base movement legality — VERIFIED baseline for static reviewed geometry.

Complete movement — PARTIAL for Intercept, forced displacement or active withdrawal near edges.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL for timed closure or withdrawal phases.

Full stateful damage pipeline — PARTIAL only for exact governed combat effects. Generic falling/environmental damage is not inferred.

Status lifecycle — PARTIAL only for exact governed statuses. Nesting, fear, odor or stress do not create statuses automatically.

Terrain/weather/hazards/zones/reactions — BLOCKING for fall edges as tactical hazards, changing exclusion cells, generalized crossing reactions, wind displacement or unstable surfaces.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT, WITHDRAW or AVOID_ZONE behavior.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for authoritative restriction boundaries, nesting-sensitive state or evacuation playback.

Reduced form: READY.

Close public access before battle. Keep the nesting/roost subject and sensitive roof scope outside BattleSpec. Resolve the encounter on a static safe approach with explicit combatants. Victory secures only that approach. Conservation, Facilities and the coexistence case continue afterward.

## Encounter readiness — Authorized Relocation Staging Diversion

Narrative premise: only after canon has already established a legitimate relocation workflow, a separate hostile encounter blocks access near staging.

Targeting/footprints/range/LoS — VERIFIED baseline.

Base movement legality — VERIFIED baseline.

Complete movement — PARTIAL for escort, Intercept, carrying-like movement or forced displacement. Carrying itself is not established by the category baseline.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL for timed departure/staging windows.

Full stateful damage pipeline — PARTIAL for exact governed effects only.

Status lifecycle — PARTIAL for exact governed effects only. Sedation/tranquilization is UNKNOWN unless separately governed.

Terrain/weather/hazards/zones/reactions — BLOCKING if a protected carrier/enclosure, crossing reactions, dynamic safe zones or environmental effects are active on-grid.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL. No generic restraint/carrier item behavior is inferred.

Trainer Features/perks — PARTIAL. No universal Ranger/wildlife-control authority is inferred.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT/WITHDRAW.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for semantic custody, enclosure, vehicle and relocation playback.

Reduced form: CONDITIONALLY READY.

Condition: an authorized world-state relocation workflow must already exist independently of combat.

Then:

- pause or finish staging before BattleSpec creation;
- place the relocation subject outside BattleSpec;
- preserve custody/placement truth in the owner systems;
- use static reviewed route geometry;
- resolve a conventional battle among explicit combatants.

Victory can clear immediate route access. It cannot create relocation authority, capture legality, custody transfer, destination acceptance, release/placement or follow-up success.

## PTU / Caelo boundary

The project source scan supports sandbox jobs, local situations, social play, wild encounters and exact authored environmental mechanics when the governing source defines them.

Toxic Ravine remains the project example of a specific location with an explicit environmental mechanical identity.

That precedent does not create a generic settlement/wild-Pokémon interaction mechanic.

Remain UNKNOWN without exact governing evidence:

- generic calming actions;
- universal capture-as-removal authority;
- relocation checks;
- restraint procedures;
- carrying unwilling or incapacitated wild Pokémon;
- tranquilization/sedation;
- generic territorial or nesting reactions;
- automatic aggression from proximity;
- generic garbage/sludge/odor penalties;
- automatic Poison, disease or exposure from sharing a space;
- trap object behavior;
- generic deterrent behavior;
- species-derived nuisance/aggression classifications;
- Type-derived urban/environmental immunity;
- generic Repel use outside exact Item rules;
- Moves as automatic wildlife-control tools;
- Abilities as automatic wildlife detectors or deterrents;
- Trainer Features granting universal wildlife-management authority;
- Ranger-like institutional powers without authored Ouros canon and exact mechanical support.

If a future PTU/Caelo or project source establishes an exact effect, implement that effect narrowly and update the corresponding capability family from tests/contracts rather than narrative need.

## Existing narrative-system boundary

Interspecies Ecology owns ecological relations and pressures.

Conservation owns stewardship objectives, protected-area/corridor management and adopted policy where canon establishes authority.

Wildlife Monitoring owns subject re-identification, tags, detections and monitoring gaps.

Pokémon Agency owns durable individual identity, custody, capture/release and partnership history.

Pokémon Shelter/Sanctuary owns placement/admission when applicable.

Waste, Food, Water, Housing, Public Space, Workplaces, Agriculture/Ranch, Roads and Facility Maintenance own their operational conditions.

Care and Community Health own health truth.

Crisis/Rescue owns immediate life-safety response.

Case/Authority owns allegations and culpability investigations.

Public Notices owns delivery/publication.

Pass 127 links these records through a persistent coexistence-response case. It does not replace any owner.

## Minecraft / Cobblemon boundary

Minecraft/Cobblemon may present:

- recurring Pokémon sightings;
- alleys, roofs, drains, gardens, fields and service yards;
- damaged/repaired containers, screens, gates and openings;
- temporary barriers and signage;
- changed NPC/service schedules;
- observation equipment when canon supports it;
- visible nesting/roost state;
- changed paths and access points;
- vehicles or enclosures as playback after authoritative world-state decisions.

Minecraft/Cobblemon cannot decide:

- same-individual identity;
- causal responsibility for damage;
- aggression/danger classification;
- health risk;
- ecological harm;
- capture or relocation authority;
- destination suitability;
- mitigation effectiveness;
- case closure.

Entity despawn is not removal or relocation. Spawn suppression is not evidence of intervention success. A barrier block does not create a reaction zone. Native damage/status does not substitute for PTU. Cobblemon BattleState remains outside coexistence truth, combatant selection, legality, HP/status, tactical position authority and narrative outcomes.

## Current implementation-safe pattern

For any coexistence scene with unsupported tactical complexity:

1. resolve observation, authority, facility/service state and noncombatant movement in Ouros world state;
2. exclude unresolved wildlife-control mechanics from BattleSpec;
3. keep noncombatants and controlled evidence/items off-grid;
4. use static reviewed geometry;
5. explicitly select combatants in Ouros;
6. let AutoPTU decide the supported tactical battle only;
7. return the battle result as one world-state fact;
8. let the coexistence case and owner systems decide what the result actually changes.

This keeps worldbuilding moving without making the Minecraft adapter duplicate missing PTU rules.

## Unresolved canon questions

- Does any Ouros region have a formal coexistence/wildlife-response institution?
- Which actors can receive ordinary settlement reports?
- Which actors can order exclusion, capture, relocation or placement?
- Are wild-Pokémon feeding rules, norms or stewardship practices formalized anywhere?
- What welfare safeguards exist for intervention?
- Which nest/den locations are sensitive information?
- What privacy applies to household reports?
- Which facilities or districts have historical coexistence arrangements?
- Which persistent wild Pokémon are known community characters?
- How are disputed interventions reviewed?

No answer is assumed in Pass 127.