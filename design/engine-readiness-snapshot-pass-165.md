# Engine Readiness Snapshot — Pass 165

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `9b435d75865b2dd9a1ce5019cb1b15c089b16da0`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`ccc2982d9f7512d77c89f58e7c7a4a5515d597af` — merged PR #303, `Freeze forced movement runtime consumer order`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No engine repository was modified by Pass 165.

## New Java evidence — PR #303

PR #303 extends the forced-movement parity contract around the existing Python runtime consumer.

The inspected commit updates the forced-movement parity workflow so the Python exporter also emits a runtime consumer artifact. The commit message and patch describe three related controls:

- freeze the Python forced-movement consumer guard and local order;
- assert the pinned consumer phase contract;
- gate forced-movement consumer ordering against the Python oracle.

This is useful implementation evidence because the eventual Java production path now has a more explicit ordering contract to match. It reduces ambiguity about where the forced-movement instruction is consumed relative to neighboring runtime work.

It remains parity-infrastructure evidence. It does not by itself demonstrate that every Java production forced-movement callsite exists or that the full category has complete runtime parity.

Therefore complete movement remains PARTIAL.

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

No capability category is promoted in Pass 165.

## Why complete movement remains PARTIAL

Positive evidence accumulated across recent Java work includes shared targeting and line geometry; server-owned Intercept candidate discovery; canonical combatant rule content; authoritative generic Push/Pull metadata; current-state target and anchor revalidation; shared displacement/partial-stop behavior for tested branches; tested forced-movement Ability modifiers such as Thrust; frozen Python runtime callsite inventory; local-order snapshots; instruction dataflow tracing; and now a frozen consumer guard/order contract.

Still not globally verified:

- full production Java binding of the forced-movement application path;
- all runtime ordering interactions after binding;
- every Push source;
- every Pull source;
- general Knockback;
- every Intercept variant/order interaction;
- arbitrary forced movement from status, terrain, weather, Item, Ability and Feature sources;
- escort/rescue movement;
- protected-object carrying;
- crowd/procession movement;
- moving vehicles/platforms;
- generalized reaction windows;
- dynamic tactical-objective policy.

The new funerary encounter concepts therefore cannot assume complete escort, procession, protection or withdrawal mechanics.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes a viewport coordinate synchronization fix as presentation-only and states that no battle rules or outcomes change.

It provides no new mechanical capability evidence for Pass 165.

## PTU/Caelo mortality boundary

Public PTU discussion supports one narrow boundary: Fainted is a recoverable rules state and should not be treated as canonical death.

The Narrative repository search did not surface an exact project-approved Caelo mortality contract or death-threshold specification.

UNKNOWN until exact PTU/Caelo source and engine review:

- fatal HP thresholds, if any;
- fatal Injury thresholds, if any;
- Trainer death procedure;
- Pokémon death procedure;
- death saves or equivalent, if any;
- consequences of reaching extreme negative HP beyond Fainted;
- Caelo-specific lethality modifications;
- permanent-injury-to-death transitions;
- resurrection or return-from-death rules;
- exact handling of Revive items relative to canonical death;
- Ghost-type identity implications, if any authored setting rule exists;
- funerary or bereavement mechanical benefits;
- Loyalty changes caused by death;
- Trainer XP or progression from bereavement;
- Skill/Feature effects that establish cause of death or identify remains;
- supernatural detection effects that can prove identity or afterlife state.

No such mechanic is invented in Pass 165.

Until exact project authority is found:

`FAINTED != DEAD`

`REVIVED_FROM_FAINTED != RESURRECTED_FROM_DEATH`

## Encounter A — Resting-Site Approach Incident

Full capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as roster/content requires
- status lifecycle — PARTIAL as roster/content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic grave-site hazards, unstable terrain, fog-as-mechanic or reactive protection
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for site-protection/withdrawal semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic resting-site playback

Full status: BLOCKED.

Reduced status: READY at narrative-contract level after individual combat-content audit.

All visitors, caretakers, remains and markers remain outside BattleSpec. Static combat may return only:

`IMMEDIATE_RESTING_SITE_APPROACH_CLEAR`

This does not establish funeral completion, marker integrity, mortality, identity or spiritual outcome.

## Encounter B — Memorial Procession Route Interruption

Full capability requirements include all ordinary combat families plus reliable escort/crowd/procession movement, protected-object handling when relevant, lifecycle, dynamic hazards/reactions if present, tactical AI policy and adapter playback.

Full status: BLOCKED.

Reduced status: READY.

The procession pauses before initiative. Participants and funerary objects remain outside BattleSpec. AutoPTU can return only:

`IMMEDIATE_PROCESSION_ROUTE_CLEAR`

This does not resume the procession, complete a rite or transfer remains.

## Encounter C — Search-Site Perimeter

Full capability requirements:

- targeting/LoS — VERIFIED
- base movement — VERIFIED
- complete movement — PARTIAL
- calculations — VERIFIED
- initiative — VERIFIED
- lifecycle — PARTIAL
- damage/status families — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING when search conditions become tactical
- moves/abilities/items/features — PARTIAL and individually audited
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for search/protect/withdraw objectives
- adapter/playback — BLOCKING

Full status: BLOCKED.

Reduced status: READY.

Only `IMMEDIATE_SEARCH_SITE_APPROACH_CLEAR` may be returned.

That result cannot establish subject found, remains found, identity, death, survival or search completion.

## Encounter D — Groundskeeper Record-Recovery Perimeter

Full version requires escort/protect/object-carrying semantics, full lifecycle, tactical objective policy and any relevant hazard/reaction families.

Full status: BLOCKED.

Reduced status: READY.

Caretaker and records remain outside BattleSpec. AutoPTU may establish only:

`IMMEDIATE_CARETAKER_ACCESS_PERIMETER_CLEAR`

That does not prove records were recovered, marker identity was verified or a resting place was confirmed.

## Mortality authority and adapters

Minecraft/Cobblemon/Craftics may present:

- an already-canonical grave or memorial marker;
- flowers, offerings and site maintenance;
- a funeral procession after Ouros establishes its participants and state;
- cemetery layout changes after an authoritative world-event update;
- a Fainted Pokémon animation matching AutoPTU state.

They may not establish:

- that an entity died because it despawned;
- that a Pokémon died because it fainted;
- that a tombstone block proves a grave exists;
- that visible Ghost-type Pokémon identify a deceased being;
- that an apparition proves an afterlife claim;
- that a marker contains remains;
- that a destroyed block destroys remains or public memory;
- that a battle result completed a funeral or resolved grief.

## Readiness conclusion

Pass 165 requires no category promotion.

The reduced versions of its tactical incidents can operate today by isolating social/funerary state from BattleSpec and using only individually audited ordinary battle content. Their full versions remain blocked by the same incomplete capability families already tracked permanently.

The core mortality continuity layer itself does not depend on battle implementation. It can advance as narrative architecture while exact PTU/Caelo lethality rules remain unresolved.