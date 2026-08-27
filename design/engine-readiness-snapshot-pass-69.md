# Engine Readiness Snapshot — Pass 69

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-27

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`84505214d4bca41610f36f0a178e675ef0ab26ba` — Freeze StatusController phase-envelope ordering (#231).

This commit adds a parity-gated `StatusControllerPhaseOrderingPolicy` derived from the pinned Python oracle. It freezes ordering for the cross-system phase envelope:

- START: held-item start -> food regen -> food-buff start -> combatant phase effects;
- END: combatant phase effects -> held-item end;
- other typed phases: combatant phase effects.

The implementation explicitly states that it owns ordering only. Concrete held-item, food and combatant phase hooks remain separate registries.

This is real progress for lifecycle/status orchestration. It does not establish a complete StatusController, complete item behavior, complete food behavior, complete turn/round lifecycle or full battle transcript parity.

The current Java README still reports implemented slices for:

- targeting, areas, footprints, target anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type tables and calculation primitives;
- stages, Accuracy stages and weather DB primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow and action budget;
- deterministic initiative;
- deterministic legal autobattler action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful Accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic event/full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

No permanent capability category is promoted by Pass 69.

## Live Python evidence

Newest inspected AutoPTU commit:

`2cd5c22f98dbab9524ff65b6bc6a3df6f54baa08` — Career: harden battle quality host signals.

This change validates browser/touch/viewport host signals before choosing battle visual quality. It improves renderer resilience. It does not add a PTU tactical rules family or Minecraft/Cobblemon adapter capability.

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

## Why the new StatusController ordering does not promote lifecycle/status

The frozen phase envelope is a coordinator contract. Category completion still requires the concrete state and behavior that runs inside those slots.

For `full turn / round lifecycle`, unresolved work still includes complete battle-state ownership, phase effects across real combatants, semantic event emission and full transcript parity.

For `status lifecycle`, the README still marks the StatusController itself unfinished. A correct call order does not establish application, persistence, phase behavior, expiry, removal and interactions for the complete status set.

For `items`, the new ordering includes held-item slots, but the README still marks the item hook registry unfinished. The existence of `HELD_ITEM_START` and `HELD_ITEM_END` therefore does not prove arbitrary held items execute correctly.

## Shared-equipment authority boundary

Pass 69 can determine narrative/world state for:

- which approved persistent item instances belong to a shared pool;
- who owns the pool through existing Material Culture/institution state;
- who has an access entitlement;
- which reservation exists;
- which exact item was checked out;
- current narrative custodian;
- assignment/use scope refs;
- physical return;
- observed return condition;
- whether the asset remains INSPECTION_PENDING, MAINTENANCE, IN_TRANSIT or otherwise unavailable;
- reconciliation discrepancies;
- handoffs to adjacent narrative systems.

Pass 69 cannot determine:

- PTU item effects merely because an object is checked out;
- mechanical equivalence between two similar tools;
- Skills, Edges, Features, Moves or Capabilities from possession;
- legal ownership from custody;
- guilt from overdue/missing state;
- repair success or technical safety without the owning system;
- Pokémon ownership, Loyalty or service legality;
- tactical objective rules;
- forced movement, terrain, weather, hazards or reactions;
- tactical AI priorities;
- Minecraft inventory authority.

## Mechanical item execution caution

A persistent world object and a mechanically implemented PTU item are separate concerns.

Safe path for a noncombat loan:

`item_instance` -> shared-pool state -> checkout/custody -> world interaction.

Additional requirements for a battle-relevant loaned item:

`mechanical_item_ref` -> implemented Item registry/hook -> legal timing/target/action semantics -> lifecycle integration -> transcript -> AI handling -> adapter playback.

Because the Item family remains PARTIAL, Pass 69 should keep shared equipment outside tactical resolution unless the exact item slice is independently verified.

## Encounter review — Field Kit Recovery Window

Narrative premise:

A field team has withdrawn from an unsafe area. One exact institutional kit remains at a known position near a territorial battle-capable threat, and another assignment depends on recovering that resource.

Intended full version may require:

- a RECOVER_AND_WITHDRAW or CLEAR_ROUTE objective;
- an exact persistent item location projected into the battlefield/world boundary;
- territorial or withdrawal-aware opponents;
- constrained route choice;
- interception or forced displacement;
- terrain/weather/hazards where governing PTU/Caelo mapping exists;
- semantic objective events;
- synchronized playback and custody writeback.

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
- items — PARTIAL if a tactical item participates; world-state kit alone does not require Item execution
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback support — BLOCKING

Reduced version:

Keep the exact kit outside the tactical grid. Persist its world-state location before the encounter. Run a static reviewed battle using only individually supported mechanics. After the authoritative AutoPTU result, recover the kit through a separate interaction and then update custody.

Battle victory cannot automatically:

- transfer the item;
- mark it returned;
- inspect its condition;
- make it AVAILABLE;
- establish who owns it.

## Encounter review — Depot Access Lockdown

Narrative premise:

A support depot holds resources required for another assignment. Staff have evacuated because the access room is temporarily unsafe due to a battle-capable threat.

Intended full version may require:

- multiple access lanes;
- CLEAR_ROUTE/PROTECT or access-control objectives;
- protected storage fixtures;
- withdrawal behavior;
- interception/forced movement;
- active environmental effects if rules-mapped;
- reactions;
- non-KO tactical priorities;
- synchronized adapter state separating battle outcome from depot reopening.

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

Evacuate all noncombatants in world state. Keep storage and exact loanable assets outside tactical targeting. Freeze a reviewed arena away from operational controls. Resolve a standard encounter. The owning workplace/facility then determines whether access is restored, after which normal checkout/transfer can occur.

A battle result cannot inspect assets, authorize access, change allocation priority or repair a facility.

## Noncombat readiness — Inspection Before Reissue

This scenario can run entirely through narrative state before new tactical capabilities exist.

Useful records:

- exact item-instance identity;
- checkout event;
- issue-condition observation;
- handoff events;
- return event;
- return-condition observation;
- component list;
- repair/maintenance refs;
- workplace schedule;
- current reservation dependencies.

No PTU combat mechanic is required to determine that an item is physically returned yet still awaiting an owning system's verification.

Minecraft materialization remains dependent on adapter/playback if the exact rack, case and interaction state must persist visually.

## Noncombat readiness — Four Checkouts, Three Kits

The reconciliation mystery needs chronology and provenance rather than tactical rules.

Required narrative capabilities:

- stable item IDs;
- stable checkout/return IDs;
- timestamps;
- handoff edges;
- pool membership history;
- location observations;
- independent source provenance;
- separation between current record and historical observation.

It can be prototyped in text/UI now. The final physical depot representation still depends on Minecraft adapter work.

## Item-family caution for future equipment stories

Pass 69 deliberately creates many objects that can remain narratively meaningful without combat effects.

If a future seed uses an issued PTU item during battle, do not promote the whole `items` family because one representative item passes tests. Mark the exact verified slice and leave the category PARTIAL until registry breadth, hooks, lifecycle, transcript and AI integration are complete.

The same rule applies to Trainer Features, Abilities and move-specific behavior.

## Current implementation recommendation

Build shared-equipment narrative persistence before tactical item integration.

The safest near-term vertical slice is:

1. persistent exact item instance already owned by Material Culture;
2. shared-pool membership;
3. reservation;
4. checkout/custody transfer;
5. world use with no invented PTU effect;
6. return;
7. inspection-pending state;
8. final availability update from the owning technical/workplace system.

This produces useful world continuity without waiting for full Item hooks or the Minecraft adapter.

## Unresolved mechanical questions

- Which PTU/Caelo item classes will receive complete Java registry coverage first?
- How will held-item phase hooks connect to the newly frozen StatusController envelope?
- Which item events will appear in the semantic BattleTranscript?
- How will AI value legal item actions once tactical policy exists?
- Which world item instances need one-to-one mapping to battle-state items?
- How will adapter writeback distinguish possession, custody and ownership?
- Can a world-state item remain present near a battle without becoming a legal target?
- What is the authoritative boundary for pickup/recovery objectives?

Until those contracts are proven, reduced encounters keep shared assets outside tactical state.