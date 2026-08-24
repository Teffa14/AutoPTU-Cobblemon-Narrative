# Engine Readiness Snapshot — Pass 153

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs.
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java `main`: `f23f5aebe51f50d8aa32449878f13e5f4c644f1f` — `Freeze generic Status move execution contract (#181)`.

This commit freezes a narrow Python-oracle contract for non-damaging Status moves: the Status branch still uses the ordinary accuracy result, then returns no crit and zero ordinary damage/damage roll. Its own code explicitly states that Status effect application remains a separate concern for the move-special/effect pipeline.

Immediately preceding Java work includes Shell Shield PRE-damage reaction, authoritative PRE-damage follow-up Move execution, Sway and related reaction contracts. These are exact slices, not proof of a generic complete reaction system.

AutoPTU Python `main`: `03321a2eba42437180fddf5c4b2570c50ba429a6` — Career sponsor-history renewal-market behavior. Recent Python changes remain Career/presentation/persistence oriented and do not promote battle capability families.

Java still states that Python AutoPTU remains authoritative while the port is incomplete. The live README continues to list core battle state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, AI scoring/policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 153 status | Evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README marks range, areas, footprints, anchors and LoS implemented. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Narrow reaction/push slices exist, but forced movement remains explicitly incomplete. |
| core calculations | VERIFIED | DB/type/stage/accuracy/weather/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed action budgets and deterministic initiative/order variants are implemented. |
| full turn / round lifecycle | PARTIAL | Multiple lifecycle slices exist; complete battle-state/transcript parity does not. |
| full stateful damage pipeline | PARTIAL | Normal/delayed/multi-target/reaction slices exist; full damage remains incomplete. |
| status lifecycle | PARTIAL | Status branch execution and selected application/prevention contracts exist; full status controller is incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Exact PRE-damage reactions exist, but the family remains explicitly incomplete. |
| move-specific behavior | PARTIAL | More representative Move paths exist, including Status execution; catalog/effect parity is incomplete. |
| abilities | PARTIAL | Selected Abilities/reactions have parity evidence; full registry parity does not. |
| items | PARTIAL | Selected item behavior exists; complete registry/hook parity does not. |
| Trainer Features / perks | PARTIAL | Generic gates/effects and selected interactions exist; catalog parity is incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action space is documented as implemented. |
| AI tactical policy | BLOCKING | Java README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java remains a standalone rules library; adapter integration is pending. |

## New Java evidence — Status Move execution does not promote Status lifecycle

`f23f5aeb` freezes only the boundary for a non-damaging Status-category Move before its special/effect semantics are applied.

Verified within that contract:

- ordinary accuracy still determines whether the Status Move hits;
- the Status branch does not crit;
- ordinary damage and damage roll are zero.

Not verified by that contract:

- the complete catalog of Status Moves;
- each Move's special effect;
- all target scopes;
- duration/stacking/removal for every Status;
- all Ability/Item/Feature interactions;
- terrain or Weather creation;
- generic reaction handling.

Therefore `status lifecycle` and `move-specific behavior` remain PARTIAL.

## Pass 153 encounter dependency mapping

### Gym Transition Exhibition — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if the approved exhibition uses moving objectives, interception or full forced movement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if Status Moves/effects are used;
- terrain/weather/hazards/zones/reactions — BLOCKING as a family; only exact supported reaction contracts may be relied upon;
- move-specific behavior — PARTIAL, exact Moves must be validated;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING if the format requires objective-aware exhibition behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: use an already-approved conventional static challenge contract. Candidate status, spectators and succession procedure remain outside the grid. AutoPTU returns the authoritative battle result; the succession layer records it only as the procedure-defined input.

### Handoff During Station Evacuation — FULL

Required:

- targeting/LoS and base movement — VERIFIED for ordinary combat;
- complete movement — BLOCKING for mobile staff, escorted records/equipment, dynamic withdrawal or interception;
- core calculations/action economy — VERIFIED;
- lifecycle/damage/status/move/ability/item/Feature families — PARTIAL as invoked by combatants;
- terrain/weather/hazards/zones/reactions — BLOCKING if the incident itself has tactical environmental consequences;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `EVACUATE`, `PROTECT_HOLDER`, `CLEAR_ROUTE`, `REACH_EXIT`;
- adapter/playback — BLOCKING.

REDUCED: Emergency Services secures people and records first. Freeze a safe static arena only if an independent hostile encounter remains. Authority/credential/knowledge handoffs stay world state and resolve separately afterward.

### Acting Leader Challenge Day — FULL

The acting office itself adds no battle mechanic. Dependencies come only from the already-approved challenge contract.

If that contract is a normal static battle, the encounter may use the VERIFIED targeting/base movement/core/action-economy foundations while exact lifecycle/damage/status/Move/Ability/Item/Feature behavior remains PARTIAL as used.

If the challenge needs dynamic objectives, forced movement, generic reactions or environment effects, the corresponding BLOCKING families remain required.

REDUCED: reuse a previously approved static challenge contract with authority validated before battle. No new battle rule is introduced by acting status.

### Two Procedure Versions

No battle capability is inherently required. Governance, Archives, Identity and Institutional Review may leave the result unresolved.

## Pass 153 world-state blockers

These belong outside AutoPTU-Java:

- persistent institutional-office identity;
- officeholding-term history;
- vacancy/absence state;
- acting-authority scope;
- succession-procedure versioning;
- candidacy/nomination/withdrawal state;
- selection event;
- assumption-of-office event;
- authority handoff;
- operational knowledge handoff;
- downstream credential/access reconciliation;
- public transition notices;
- former-officeholder relationship to the institution;
- transition disputes;
- continuity review and process learning;
- institution state -> Minecraft presentation;
- succession state -> battle-contract selection.

## Mechanical non-inferences

Pass 153 does not authorize:

- office title as a Trainer Class;
- officeholding as a Skill rank;
- leadership as extra actions/initiative;
- successor training as a Trainer Feature;
- family connection as appointment eligibility;
- public popularity as authority;
- acting status as full permanent authority;
- keys/account access as proof of officeholding;
- battle victory as appointment unless an authored procedure explicitly uses the result;
- a succession ceremony as a buff/status/healing effect;
- former leader status as Mentor mechanics;
- Minecraft NPC/nameplate changes as institutional truth;
- the new generic Status Move contract as full Status behavior;
- narrow PRE-damage reaction support as complete reactions or complete movement.

## PTU / project evidence

The narrative repository's mechanical-source rules still require PTU/Caelo and the actual engines to govern battle behavior. Succession is institutional world state, not a PTU subsystem.

If a candidate battle uses a Status Move, the new Java contract proves only that the generic Status-category branch uses accuracy and skips ordinary damage arithmetic. Its effect still requires exact evidence.

No reliable primary Caelo source defining Gym succession, appointment, acting authority, institutional officeholding or leadership transfer was recovered in this run.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.

## Open mechanical/canon questions

- Which Ouros offices exist at campaign start?
- Which battle institutions require a current officeholder to run formal challenges?
- Does any authored succession procedure include a battle, exam or other PTU-governed test?
- Which acting roles can authorize challenges, spending, access, releases, transfers or emergency decisions?
- How do credential and Digital Systems changes propagate after assumption of office?
- Can a former Gym Leader temporarily substitute after retirement, and under which institutional rule?
- Which transition records are public, private or restricted?
- Can player-founded institutions write their own succession procedures?
- What happens to a scheduled formal battle if the office becomes vacant before its start?
- Which exact PTU/Caelo rules apply if an appointment procedure uses a formal battle rather than a purely institutional decision?