# Engine Readiness Snapshot — Pass 67

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`57c7c2a9751cf02facf5d176b9d0f95b996a9bd1` — Use effective Accuracy in authoritative move preparation (#230).

Immediately relevant prior evidence:

`8670b4bf2b423c5d9e43cc9e8d6c979e6c832909` — Derive Chronicler Accuracy from authoritative runtime state (#228).

The newest change strengthens one concrete Accuracy path by using the effective Accuracy projection during authoritative move preparation and testing that projection. This is meaningful progress inside the accuracy/Trainer Feature integration boundary.

It does not establish complete Trainer Features/perks, complete move-specific behavior, a complete battle lifecycle or any of the movement/environment/AI/adapter families needed by rich shared-public-space encounters.

The README at `57c7c2a...` reports implemented slices for:

- targeting, areas, footprints, target anchors and LoS;
- Shift movement legality including movement modes, terrain costs, blockers, Wallrunner, sprint and landing-fit boundaries;
- jump movement;
- Damage Base/type tables and calculation primitives;
- stages, accuracy stages, weather DB calculation primitive, crit probability, Burn and modifier primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow and action budget;
- deterministic initiative;
- legal autobattler action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The presence of terrain costs inside base Shift legality does not prove the full `terrain/weather/hazards/zones/reactions` family. The narrative project's permanent category remains BLOCKING because the richer behaviors required by encounter design are still explicitly unfinished.

## Live Python evidence

Newest inspected AutoPTU commit:

`0213ef4fe1d1ecb3cebf8704548a1d664969a0eb` — Career: harden career-book labels.

Recent underlying changes fail closed on malformed persisted labels and rollback decision counters. These improve persistence correctness and presentation authority. They do not add PTU tactical capabilities, public-space rules or Minecraft adapter semantics.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

Pass 67 does not promote any capability category.

## Shared-public-space authority is world state

The new public-space extension may determine:

- which shared-space record a location uses;
- which zones and entrances exist in that record;
- which recurring use patterns are established;
- which cohorts are expected during authored time windows;
- which rule or restriction records are current;
- which external system owns a restriction cause;
- which visible traces remain after events or repairs;
- whether an ordinary-return handoff occurred;
- which zones are narratively available after that handoff.

It does not determine:

- PTU movement costs beyond implemented battle state;
- tactical terrain effects;
- weather effects;
- hazard damage;
- reactions;
- interception;
- forced movement;
- damage or statuses;
- Move, Ability, Item or Feature behavior;
- battle-objective legality;
- AI priorities;
- who legally owns a public place;
- who has authority to set a rule unless canon/world state already establishes that mandate.

## Access-state caution

A world-state path or gate being OPEN does not mean AutoPTU has a tactical objective for reaching or protecting it.

Likewise:

- `CLOSED_TEMPORARILY` is a narrative access condition, not a PTU status;
- a barrier prop in Minecraft is not a reaction/interception mechanic;
- a route around a pond can be blocked in the overworld without creating battle terrain damage;
- an event crowd can be evacuated before battle without claiming that AutoPTU resolved an escort objective.

## Encounter review — Pondside Withdrawal

Narrative premise:

An ordinary shared path passes beside a zone currently used defensively by wild Pokémon. Routine users must leave safely and the affected section is temporarily closed pending ecological review.

Intended full version may require:

- civilians or cohorts withdrawing through legal paths;
- changing safe lanes;
- PROTECT/WITHDRAW/CLEAR_ROUTE objective state;
- interception or forced displacement;
- terrain/weather/hazard mapping when PTU/Caelo establishes it;
- territorial or retreat-oriented tactical AI;
- adapter playback synchronized with the closure and later review.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback support — BLOCKING

Reduced version:

Evacuate ordinary users in world state before the battle. Mark the affected section closed. Run a static reviewed encounter at a safe edge using only supported mechanics. After the authoritative result, Ecology/Conservation and public-space state decide whether the restriction continues, converts to an observation state or can be lifted.

The battle result cannot establish permanent access policy, prove which Pokémon caused prior incidents or create ownership/territory law.

## Encounter review — Plaza Access Break

Narrative premise:

An immediate threat makes one entrance to a familiar plaza unusable while another route remains available. The space matters because it supports daily circulation.

Intended full version may require:

- multiple exits and civilian routes;
- protected fixtures/noncombatant zones;
- dynamic barriers;
- CLEAR_ROUTE/ESCAPE/PROTECT objectives;
- interception or forced movement;
- AI aware of withdrawal and access goals;
- adapter writeback for exact entrance and zone state.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback support — BLOCKING

Reduced version:

Close the plaza to civilians first. Select a static reviewed arena outside protected fixtures. Resolve an ordinary legal battle. Perform a separate access/condition review afterward.

A victory cannot repair a gate, clear a maintenance work order or approve a permanent routing change.

## Noncombat readiness

Pass 67 systems that can advance before new tactical families include:

- public-space identity and zone records;
- entrance state;
- ordinary recurring-use patterns;
- user cohorts as aggregate presence;
- authored use windows/reservations;
- rule provenance and revision history;
- temporary restrictions referencing an owning system;
- shared-use conflicts defined by concrete incompatible uses;
- visible traces and place memory;
- ordinary-return handoffs after events/crises/maintenance;
- multi-clock testimony mysteries;
- civic evidence packets derived from persistent use conflicts;
- guide/signage updates after access changes.

These require persistent narrative/world state and eventual UI/adapter representation, not missing PTU battle rules.

## Adapter implications

Safe future behavior:

- persist only meaningful recurring NPC users; aggregate anonymous cohorts;
- drive routine presence from authoritative schedule/time state;
- close affected entrances/zones without globally despawning the location;
- retain event/repair/ecology traces until an owning-system handoff resolves them;
- synchronize visible barriers and signs with authoritative restriction records;
- preserve access-rule provenance rather than treating text on any sign as universal truth;
- materialize wild Pokémon from actual ecology/spawn logic;
- keep battle and public-space writebacks separate.

Unsafe shortcuts:

- Minecraft presence equals authorization;
- crowd size equals popularity or public support;
- despawning a barrier automatically ends a restriction;
- a battle victory opens all gates;
- a repeated spawn establishes legal territory;
- a familiar NPC becomes steward/operator by proximity;
- visual rain becomes PTU Weather automatically;
- a scripted knockback substitutes for AutoPTU forced movement;
- Cobblemon AI independently decides protect/withdraw objectives while AutoPTU records a different battle.

## Promotion gates for rich public-space encounters

Before full Pondside Withdrawal or Plaza Access Break can become authoritative, implementation needs current evidence for the exact mechanics used, including where applicable:

- objective lifecycle for PROTECT/WITHDRAW/CLEAR_ROUTE/ESCAPE;
- complete forced-movement/interception behavior;
- terrain/weather/hazard mapping;
- lifecycle timing around objectives and environmental effects;
- tactical AI that scores non-KO goals;
- semantic battle events for those state changes;
- adapter playback preserving world entities, access state and battle result without running parallel rules.

Representative helpers are insufficient.

## Unresolved mechanical questions

- Which non-DEFEAT objective profiles will be ported first into authoritative AutoPTU battle state?
- How will protected/noncombatant entities be represented without letting Minecraft become a second combat engine?
- Which exact terrain and weather states can later map from overworld conditions?
- How will interception/reactions interact with civilian withdrawal if those objectives are implemented?
- What transcript events will represent route clearance, withdrawal and objective completion?
- How will territorial/retreat tactical AI be expressed over the legal `BattleChoice` list?

## Unresolved canon questions

- Which Ouros places qualify as shared/public/common spaces?
- Who owns, stewards, operates and maintains each one?
- Which institutions can create or revise access rules?
- Which recurring users have enough narrative importance to persist individually?
- Which Pokémon-use customs are established for shared urban spaces?
- Which spaces overlap conservation or sacred stewardship and therefore require stricter ownership by those systems?
- Which use-window or reservation practices exist regionally?
- What population density can the Cobblemon layer safely and legibly materialize?

Until these are approved, Pass 67 remains systems/proposal material only.