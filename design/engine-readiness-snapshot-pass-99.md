# Engine Readiness Snapshot — Pass 99

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`ad43112b12c0bee204502cdea100683104a881c4`

Latest relevant commit:

`Freeze Trainer round-feature lifecycle ordering (#134)`

The commit adds a parity-checked contract for Trainer Feature ordering around round start. The contract freezes ordering/guards such as declared-action clearing, initial send-out placement, initiative rebuild, `round_start` event emission and round-start Feature dispatch.

The implementation comments explicitly state that Trainer Feature execution remains a separate runtime slice. Therefore this evidence strengthens lifecycle/Trainer-Feature infrastructure but does not prove the Feature catalog or all round-start semantics.

The parity workflow for this slice pins Python oracle commit:

`16d228efa63aabecb67fa788959a359aac7f8f03`

That Python commit was fetched successfully. Its visible repository diff is Career-facing; Java's exporter specifically reads the battle `PhaseController.start_round()` contract from the pinned checkout.

The latest AutoPTU main commit returned by the repository's recent-commit search remains:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent visible Python-main work remains Career-oriented and does not justify changing the tactical readiness map.

The AutoPTU-Java README continues to say the Python implementation is authoritative while the port is incomplete. It still lists full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, complete hook registries, transcript parity, tactical AI and the Minecraft/Cobblemon adapter as unfinished work.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static geometry, footprints, range and geometric LoS remain verified.

Pass 99 non-inference:

- a postal route map is not battle LoS;
- a courier being visible in Minecraft is not targeting eligibility;
- a parcel on a shelf is not a combatant target unless an explicit battle contract creates an object-target system;
- tracking information does not reveal tactical position automatically.

`base movement legality`

Base Shift/Jump and established movement-mode legality remain verified.

Pass 99 non-inference:

- a courier assignment does not grant movement Capability;
- Flying type does not prove delivery flight;
- Mountable does not prove cargo capacity;
- a mailbag is not a movement mode;
- a route being postal-service-approved does not bypass normal movement legality.

`core calculations`

Established calculation primitives remain verified.

No postage, parcel weight, carrying capacity, courier bonus, delivery check or package-damage formula is introduced.

`action economy / initiative`

Established action economy/initiative remain verified.

The newer Trainer round-feature ordering contract confirms more ordering around round start, but it does not create postal timing mechanics.

Pass 99 non-inference:

- urgent parcel -> initiative bonus;
- courier role -> Speed bonus;
- delivery deadline -> extra action;
- package possession -> action-economy penalty.

`AI legal-action infrastructure`

Deterministic legal-choice generation remains verified.

This does not prove objective selection for:

- PROTECT_CARRIER;
- INTERCEPT_CARRIER;
- BREAK_THROUGH;
- REACH_HANDOFF_POINT;
- ESCORT;
- WITHDRAW_WITH_ITEM;
- AVOID_DAMAGE_TO_CARGO.

Those depend on tactical policy or objective systems not yet verified.

### PARTIAL

`full turn / round lifecycle`

Representative phase, initiative, delayed-hit, temporary-effect, field-progression, Trainer AP/action-reset and round Trainer Feature ordering contracts now exist.

Still PARTIAL because the complete START/END lifecycle, all duration classes, interrupts, Features, Statuses, Abilities, delayed effects and transcript interactions are not proven.

Pass 99 distinction:

postal deadlines, dispatch windows, service timetables and parcel aging are overworld clocks, not battle rounds.

`full stateful damage pipeline`

Representative authoritative damage paths exist.

Still PARTIAL because the Java README continues to list full damage as unfinished.

No physical package condition should be mapped to battle HP or damage without a dedicated rule contract.

`status lifecycle`

Representative status boundaries exist.

Still PARTIAL.

A parcel being wet, delayed, contaminated-suspected, fragile or sealed does not create a PTU Status.

`move-specific behavior`

Representative Move behavior exists.

Still PARTIAL.

A courier encounter that relies on a particular Move must verify that exact Move behavior.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

Do not infer:

- Pickup = parcel recovery;
- Run Away = delivery withdrawal AI;
- Vital Spirit = unlimited courier endurance;
- Telepathy = postal tracking;
- Flying-related Ability = cargo service.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Physical postal parcels, mailbags, labels, receipts and sealed documents remain overworld objects unless an exact PTU Item definition authorizes mechanics.

`Trainer Features / perks`

Representative Feature infrastructure exists and the current Java head adds a parity-frozen round-start ordering contract.

Still PARTIAL.

The new contract explicitly does not prove Feature execution semantics or catalog completeness.

Sorter, courier, dispatcher, postmaster, route planner and mailroom worker are narrative jobs. They grant no Feature, Skill Rank, Edge, AP, Order or interrupt automatically.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a family.

Pass 99 impact:

- no true carrier interception scenario;
- no forced parcel carrier displacement;
- no moving escort corridor;
- no push/pull around platforms as a delivery objective;
- no autonomous courier withdrawal path inside battle.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 99 impact:

- route weather must remain overworld state unless exact battle Weather is validated;
- train platform, dock, storm, ice or flood context cannot invent battle hazards;
- a secured handoff area does not create a protection zone automatically;
- a fragile parcel does not create reactions when hit.

`AI tactical policy`

Still BLOCKING.

This is the principal blocker for a full delivery/escort battle because legal actions alone do not establish cargo-aware goals.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

There is no verified end-to-end contract for projecting postal-item identity, custody, routing, carrier state or handoff objectives into Minecraft while preserving AutoPTU-Java as rules authority.

## Pass 99 specific overworld blockers

`POSTAL_ITEM_IDENTITY`
One persistent physical item across labels, route legs, depots and representations.

`POSTAL_ADDRESS_AND_FORWARDING`
Versioned destination information with privacy boundaries.

`POSTAL_ROUTING_PLAN`
Planned route derived from Travel/service state without pretending the plan already happened.

`POSTAL_LEG_EXECUTION`
Coarse actual movement through hubs and services.

`POSTAL_HANDOFF_HISTORY`
Append-only custodial transitions.

`POSTAL_DELIVERY_ATTEMPT`
Final-mile attempt, authorized endpoint and exception outcome.

`POSTAL_EXCEPTION_STATE`
Address, routing, damage, delay and missing-item states that preserve uncertainty.

`POSTAL_FLOW_AGGREGATION`
Backlog/volume bands for ordinary mail so the server does not persist every envelope.

`POSTAL_TO_COMMUNICATIONS_HANDOFF`
Physical receipt can inform message-delivery state without implying acknowledgement/read state.

`POSTAL_TO_TRAVEL_HANDOFF`
Travel remains authoritative for whether route legs can run.

`POSTAL_TO_MATERIAL_PROVENANCE_HANDOFF`
Unique delivered objects preserve their existing asset IDs and provenance.

`POSTAL_TO_CASES_HANDOFF`
Missing/damaged/misrouted does not become theft until evidence warrants a case.

`POSTAL_TO_MINECRAFT_PROJECTION`
Bags, crates, mailboxes and courier entities remain projections of server state.

## Encounter dependency summary

### Parcel Transfer at North Junction — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when used:

- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for intended behavior:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions when platform/vehicle state matters;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

REDUCED:
Keep the parcel off-grid under secure custody, resolve a conventional static battle to clear the junction, then perform or postpone the handoff through postal/world state.

### Address Unknown — Last Mile

The investigation is primarily overworld and can advance before the battle engine grows.

Full escort/withdrawal variants would require complete movement and tactical AI.

REDUCED:
Resolve address evidence, privacy, maps and forwarding first. Any confrontation becomes a separate static encounter.

### Storm Backlog Field Dispatch — FULL

BLOCKING for intended dynamic form:

- terrain/weather/hazards/zones/reactions;
- complete movement if routes change during combat;
- AI tactical policy for autonomous couriers;
- Minecraft playback.

REDUCED:
Resolve prioritization, route choice and assignment outside battle. Create independent static encounters only for route incidents that truly require combat.

## Readiness conclusion

Pass 99 adds no reason to promote a permanent category.

The current Java head is meaningful progress for Trainer round lifecycle ordering. It strengthens evidence inside `full turn/round lifecycle` and `Trainer Features/perks`, but both remain PARTIAL because ordering contracts are not equivalent to complete effect execution.

Postal Logistics itself can be implemented largely as server-side overworld state before the missing battle families are complete. The richer escort/interception versions should wait rather than forcing Minecraft to duplicate PTU mechanics.

## Unresolved mechanical questions

- Exact PTU/Caelo carrying and encumbrance rules relevant to physical parcels.
- Exact Mountable/passenger/cargo distinctions if Pokémon carriers are authored.
- Exact Skills/Features that might support courier/navigation work.
- Whether any Items represent bags, containers or protected transport.
- Pursuit, interception, surrender and escort semantics.
- Weather and environmental effects on delivery encounters.
- Object/interactable targeting if parcels ever become tactical objects.

The primary Caelo corpus was not reliably retrieved during this pass. No Caelo-specific courier, carrying, parcel, address or logistics rule is asserted.