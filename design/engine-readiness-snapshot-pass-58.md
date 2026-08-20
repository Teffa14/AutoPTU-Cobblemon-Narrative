# Engine Readiness Snapshot — Pass 58

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`201e52e68184b52b14a5040f8a440058e6d8daa9`

Latest inspected commit:

`Advance canonical initiative into combatant turns`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/201e52e68184b52b14a5040f8a440058e6d8daa9

The commit adds a semantic turn-start event, initiative-turn advancement results and authoritative advancement into combatant turns. It freezes the initiative-turn lifecycle contract against Python and wires parity into Gradle/CI.

This is strong evidence for action economy/initiative and further evidence for lifecycle infrastructure.

It does not prove:

- complete turn/round lifecycle;
- interrupts/reactions;
- complete status timing;
- complete damage sequencing;
- every initiative-sensitive Ability or Feature;
- tactical AI;
- Minecraft playback.

The current Java README still states that Python AutoPTU is the oracle while the port is incomplete and lists these broad areas as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- full semantic BattleSpec → BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent Python commits remain Career-focused. No newly inspected Python tactical commit changes the permanent classification below.

Canonical URL:
https://github.com/Teffa14/AutoPTU/commit/e4bb0ca38b7018710af476ce365d515a387de4e7

Python remains the behavioral oracle for slices frozen into Java parity contracts.

## Permanent capability map

The classification stays conservative. One representative Move, status, Ability, item or Feature never promotes the whole family.

| Permanent capability family | Pass 58 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java has dedicated targeting, area, footprint, anchor and LoS coverage. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain movement costs, blockers and fit rules have dedicated coverage. This is not full movement. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement and reactions remain explicitly unfinished. No broad contract verifies interception or displacement. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy primitives, crit probability and several modifiers are implemented as calculation primitives. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, deterministic initiative ordering, authoritative initiative progress and now authoritative combatant-turn advancement are directly evidenced. |
| full turn / round lifecycle | PARTIAL | Round/phase/turn state is increasingly authoritative, but full combat state and all phase-sensitive behavior remain incomplete. |
| full stateful damage pipeline | PARTIAL | Multiple live post-damage and RNG-hook slices exist, while the README still lists full damage resolution as unfinished. |
| status lifecycle | PARTIAL | Several status registries and timing slices exist, but the full controller remains incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Movement costs/weather calculation primitives do not prove runtime terrain/weather/hazard/zone/reaction behavior. |
| move-specific behavior | PARTIAL | Contracts/keywords and selected behavior exist; the complete PTU Move library does not. |
| abilities | PARTIAL | Multiple Abilities run through authoritative hooks. The registry remains incomplete. |
| items | PARTIAL | Selected held/item slices exist. Full item behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered infrastructure and selected Features exist. The complete catalogue remains unfinished. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal action-space generation/filtering is explicitly implemented. |
| AI tactical policy | BLOCKING | AI scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | The repository is still a Java rules core, not the Minecraft adapter. |

## Pass 58-specific implementation boundary

Illicit-network state belongs primarily to the future persistent overworld authority layer.

The battle core should not decide:

- whether property is stolen;
- whether a capture is lawful;
- ownership;
- custody validity;
- guilt;
- whether a shipment is contraband;
- whether an institution is authorized to search or seize anything;
- whether a buyer knew an asset was stolen;
- whether a transfer violates Ouros canon law.

Suggested non-battle blockers:

`OVERWORLD_ASSET_PROVENANCE_AND_CUSTODY = BLOCKING`

`OVERWORLD_TRANSACTION_AND_FLOW_GRAPH = BLOCKING`

`OVERWORLD_LEGALITY_AND_AUTHORIZATION_RULESET = BLOCKING`

These labels do not lower any battle category. They identify authority work that must live outside AutoPTU-Java.

## Why the newest Java initiative slice does not promote lifecycle

The latest commit is meaningful. It gives the runtime an explicit authoritative boundary for advancing initiative into a combatant turn and emits semantic turn-start events.

The remaining lifecycle surface is still larger:

- complete phase-sensitive status behavior;
- all Ability/Feature triggers;
- reaction/interrupt windows;
- delayed effects across every supported mechanic;
- complete semantic transcript coverage;
- end-to-end battle state parity.

`full turn / round lifecycle` therefore remains PARTIAL.

## Encounter dependency review

### Freight Yard Transfer

Full version needs:

- a carrier trying to reach another carrier or exit;
- possible protection of recovered cargo;
- route denial/interception;
- autonomous objective-aware enemies;
- optional terrain/zone behavior in active loading lanes.

Dependency classification:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if used tactically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- overworld provenance/custody — BLOCKING outside battle core.

Reduced version:

Freeze the transfer before battle. Cargo/evidence remain overworld entities. Use a normal static battle if confrontation occurs. Update custody and case state afterward.

### Hidden Nursery Recovery

Full version requires:

- escort/protect or equivalent objective semantics;
- movement/interception;
- actors capable of withdrawal/surrender where applicable;
- objective-aware AI;
- possibly controlled exits/zones;
- Minecraft playback;
- authoritative persistent Pokémon identity/custody.

The full version remains blocked by complete movement, broad reaction/objective support, AI tactical policy and adapter/playback.

Reduced version:

Evacuate uninvolved staff and recovered Pokémon through overworld state before freezing the battle. Only combatants enter AutoPTU. Recovery never becomes a generic battle reward.

### Harbor Transfer Disruption

Full version may require:

- a timed transfer window;
- multiple exits;
- INTERCEPT / BREAK_THROUGH / WITHDRAW objective state;
- moving carriers;
- dock/weather hazards only if explicitly active under PTU rules;
- tactical AI;
- Minecraft playback.

Reduced version:

World-state time determines whether the transfer occurred before combat. AutoPTU handles only the static battle that follows. The overworld authority applies transaction/custody consequences afterward.

## PTU/Caelo caution

Pass 58 does not infer legality from PTU mechanical success.

Examples:

- a successful Capture Roll does not prove lawful ownership;
- a Guile or Stealth success does not define criminal status;
- a Pokémon movement capability does not authorize transport through a protected area;
- a legal battle result does not authorize confiscation;
- possession of an item does not establish title/ownership;
- an institutional credential does not prove authority outside its authored scope.

The project-supplied primary Caelo PDFs were not reliably recoverable in this runtime. No new Caelo-specific search/seizure, poaching, ownership, capture or enforcement rule is asserted.

## Evidence required for richer Pass 58 encounters

Battle-side:

- verified objective-state contracts for INTERCEPT / PROTECT / BREAK_THROUGH / WITHDRAW or equivalent;
- complete forced movement/interception semantics;
- broad zone/reaction contracts where route denial is tactical;
- tactical AI that understands goals beyond damage maximization;
- authoritative semantic playback to Minecraft.

Overworld-side:

- persistent item/Pokémon identity across custody changes;
- versioned provenance and asset-flow records;
- server-owned transaction state;
- explicit authorization/legal-status rules authored per institution/region;
- case/evidence integration;
- privacy and actor-specific knowledge;
- recovery/disposition workflow;
- transport-service integration;
- audit-safe writeback from battle outcomes.

## Snapshot conclusion

Pass 58 adds no reason to relax the conservative permanent capability map.

The newest Java work materially strengthens authoritative initiative and combatant-turn progression. It does not provide interception, objective-aware tactical AI, broad reactions or Minecraft playback, which are the main blockers for full smuggling/interdiction scenarios.

The narrative layer can advance now because operations, asset flows, custody, brokers, buyers, front businesses, diversion events and case links are persistent world-state concepts. Reduced encounters can keep cargo, evidence and noncombatant movement outside the tactical grid until the missing battle families are verified.
