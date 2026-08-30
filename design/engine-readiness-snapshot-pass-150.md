# Engine Readiness Snapshot — Pass 150

Status: ENGINE EVIDENCE SNAPSHOT. Read-only evidence and dependency classification only. This file does not modify AutoPTU-Java or AutoPTU and does not promote a capability from one representative mechanic.

Date: 2026-08-30

## Live repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`c5b2a34ff23887770268bfe4108dfc86e9a796fb`

Commit:

`Compose Intercept position from server-owned Shift legality (#288)`

This is newer than the Pass 149 evidence.

The new `RuntimeInterceptPositionResolver` composes an Intercept destination using the attack-line cells plus authoritative `BattleRuntimeState`. Combatant position, footprint and legal Shift destinations are read server-side. The code explicitly states that this keeps Minecraft/Cobblemon adapters from selecting the intercept destination.

Tests cover:

- remaining at the current position when already on the attack line;
- selecting the nearest reachable attack-line tile from server-owned legal Shift destinations;
- returning no destination when the attack line cannot be reached by legal Shift.

Recent preceding commits also moved Shift destination legality into authoritative battle state and added/gated server-owned Intercept-position composition.

This strengthens a concrete Intercept + Shift-legality path. It does not verify every source or sequencing case in the broader complete-movement family.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer commit was observed. The commit remains explicitly presentation-only and says battle rules and outcomes do not change.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category changes during Pass 150.

## Why the new Intercept evidence does not promote complete movement

The current live evidence verifies another important composition step for Intercept: the runtime now selects an Intercept position from authoritative legal Shift destinations rather than allowing an adapter to choose that tile.

The permanent family remains PARTIAL because the family named by the project is deliberately broader:

`complete movement including push/pull/knockback/interception/forced movement`.

A category promotion would require evidence covering the category rather than one representative path. Current evidence does not establish all Push sources, all Pull sources, all Knockback sources, every Intercept path, arbitrary collision behavior, escort movement, carried/object movement, moving platforms, environmental forced movement, reaction ordering or every stop/partial-stop interaction.

## Companion-continuity readiness rule

Recurring companion state is mostly narrative/world-state orchestration and can advance now.

The following do not require a new tactical capability:

- recording that an NPC accompanied one journey segment;
- recording a guide's participation scope;
- storing a causal departure event;
- remembering a temporary separation;
- checking whether a reunion is plausible from knowledge, reach and motive;
- returning the same NPC in a different role;
- representing absence without inferring relationship rupture;
- keeping a noncombat companion outside BattleSpec;
- showing an already-decided companion presence in Minecraft.

A companion concept becomes engine-dependent when the authored encounter asks AutoPTU to resolve escort, protection, withdrawal, timed arrival, objective-aware cooperation or dynamic hazards.

## Companion Extraction Corridor

Full-version intent:

A temporary companion must withdraw through a contested corridor while combatants can intercept, displace, protect or block movement.

Capability matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | explicit combatant spatial relationships and target legality |
| base movement legality | VERIFIED | ordinary legal movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | escort positioning, Intercept, displacement and collision effects |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | ordinary sequencing |
| full turn/round lifecycle | PARTIAL | extraction timing and encounter-end window |
| full stateful damage pipeline | PARTIAL | exact persistent combat damage state |
| status lifecycle | PARTIAL | exact status consequences while withdrawing |
| terrain/weather/hazards/zones/reactions | BLOCKING | generalized protection reactions or unsafe route zones if used |
| move-specific behavior | PARTIAL | selected legal move semantics |
| abilities | PARTIAL | selected ability semantics |
| items | PARTIAL | selected battle-item semantics |
| Trainer Features/perks | PARTIAL | selected feature/interrupt semantics |
| AI legal-action infrastructure | VERIFIED | legal candidate actions |
| AI tactical policy | BLOCKING | objective-aware blocking, protection and withdrawal decisions |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative tactical extraction presentation/handoff |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- Ouros establishes the companion episode and withdrawal intent before battle;
- the semantic companion leaves tactical state before initiative;
- AutoPTU receives only explicit combatants and static geometry;
- no escort path, protection reaction, dynamic arrival or tactical companion AI is simulated;
- an allowed result is limited to `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or another reviewed narrow spatial fact;
- Travel/World Agency then evaluate the NPC's actual onward state.

## Separated Expedition Reunion Perimeter

Full-version intent:

Members of a temporary expedition approach a rendezvous from separate routes and may arrive while a battle is already active.

Relevant capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including forced movement/interception — PARTIAL where the encounter uses it
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for timed arrivals and phase boundaries
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if the perimeter changes dynamically
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for multi-objective arrival/holding behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative arrival handoff

Full version: BLOCKED.

Reduced version: READY.

Ouros determines exactly which actors reached the rendezvous before BattleSpec creation. The battle starts with a fixed explicit roster and static arena. A narrow result such as `IMMEDIATE_REUNION_PERIMETER_CLEAR` may be committed. AutoPTU does not decide who arrived.

## Mentor Withdrawal Chokepoint

Full-version intent:

A mentor or specialist ends their operational role and withdraws while hostile actors can contest the route.

Relevant capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for authoritative withdrawal/end semantics
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if reactions/zones are used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for independent withdrawal priorities
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

The mentor leaves BattleSpec before initiative. The remaining battle can clear the immediate chokepoint but cannot establish the mentor's later route, survival, relationship status, institutional authority or future return.

## Specific evidence added by commit #288

The current Java head improves the confidence of one exact design claim used by these encounters: when Intercept position selection is eventually used, the Minecraft/Cobblemon adapter should not be responsible for choosing the position.

The runtime now composes that destination from server-owned legal Shift state.

That is consistent with the permanent Ouros authority rule:

- Ouros chooses world participants and world facts;
- AutoPTU owns tactical rules and state;
- Minecraft/Cobblemon/Craftics presents authoritative results.

It does not authorize a Minecraft follower path to become a tactical escort path.

## PTU / Caelo assumptions kept UNKNOWN

Pass 150 does not invent:

- a universal NPC companion slot;
- a follower party-size rule;
- generic companion AI;
- automatic player control over allied NPC Trainers;
- automatic companion obedience;
- automatic battle inclusion because an NPC traveled with the party;
- universal escort/protect semantics;
- universal extraction or withdrawal rules;
- universal knowledge synchronization among co-travelers;
- generic mentor combat bonuses;
- generic mentor progression rewards;
- generic loyalty thresholds for joining, staying or leaving;
- a universal Skill Check that forces companionship;
- a universal rule for carrying HP/status/initiative between separate companion encounters;
- generic ally reinforcement timing.

If a PTU or Caelo source defines an exact relevant mechanic, the authored encounter must cite and validate that mechanic separately.

## Minecraft/Cobblemon/Craftics boundary

The presentation layer may show already-established narrative state such as:

- a guide walking with the player;
- a researcher waiting at a field site;
- a mentor observing a scene;
- a temporary camp;
- a departure animation or dialogue;
- an NPC waiting at a rendezvous;
- a later reunion at a valid location;
- route and clothing changes established by their owning systems.

It must not decide:

- that an NPC joined or left;
- why they are present;
- whether they are willing or available;
- whether they reached a destination;
- whether they are a battle participant;
- their PTU position/HP/status;
- tactical escort movement;
- Intercept destination;
- objective success;
- survival;
- relationship change;
- reunion eligibility.

An entity being physically near the player does not make it a companion in narrative state. An entity despawning does not establish departure, disappearance or death.

Cobblemon BattleState remains outside Ouros battle-state authority.

## Readiness conclusion

Pass 150 changes no permanent capability status.

The recurring-companion continuity layer itself is READY as world-state architecture because it records bounded participation episodes and references existing authoritative owners. Mechanically rich companion encounters remain blocked exactly where they require incomplete escort/forced-movement behavior, lifecycle, generalized reactions, tactical policy or adapter playback.

Reduced encounters remain READY by removing semantic companions from BattleSpec before initiative and allowing AutoPTU to resolve only a static explicit combatant problem with narrow outputs.