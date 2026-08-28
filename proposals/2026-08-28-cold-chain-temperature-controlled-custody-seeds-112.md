# Ouros Cold-Chain & Temperature-Controlled Custody Seeds — Pass 112

Status: NON-CANON PROPOSALS. These are reusable situations, NPC/faction patterns, mysteries, encounter concepts and arc seeds. They do not establish regional technology, item requirements or PTU mechanics.
Date: 2026-08-28
Research provenance: `research/2026-08-28-cold-chain-temperature-controlled-custody-scan-112.md`.
Design dependency: `design/cold-chain-temperature-controlled-custody-continuity-extension.md`.

## Generation rule

Only instantiate a temperature-controlled story when at least one subject has an authored condition requirement or when the story concerns the infrastructure/history itself. Never invent a cold requirement merely to create a quest.

The generator must resolve specific actors, facilities, batches, shipments, routes and owners from world state. A proposal becomes canon only through the project's normal approval/world-state process.

## Situation seeds

### The Cold Room Works, the Record Does Not

A storage zone appears operational and current observations are consistent with its authored profile. One monitoring interval is missing from the night before.

Playable question: can the missing interval be reconstructed from independent evidence, or must the affected subjects remain under review?

Consequences can include delayed dispatch, a temporary hold, a supplier dispute, a clinic scheduling problem or a mundane no-fault equipment investigation.

Do not convert the gap into confirmed spoilage or equipment failure.

### The Delivery Arrived Cold, the Handoff Is Incomplete

A shipment physically reaches its destination. The receiving staff observe a condition consistent with the profile, but one transport segment's records have not arrived.

The courier may have completed custody correctly while condition continuity remains `ACCEPTED_WITH_GAP`.

This creates a procedural/social problem without making the courier negligent by default.

### The Power Returned, the Batch Did Not

An outage ends. Refrigeration equipment is repaired or restarted and future storage is verified. Stock associated with the uncertain interval remains under Batch Traceability review.

This seed demonstrates recovery asymmetry: infrastructure can recover before goods are cleared.

### The Temporary Cold Room Became the Morning Market

During a prior disruption, a temporary temperature-controlled site was placed beside a square, station, clinic or depot. Traders and carriers changed their morning routines around it.

After the emergency ends, the temporary site is removed or repurposed, but the route, nickname and social gathering persist.

### Two Goods, One Room, Different Rules

Two controlled subjects share one facility but reference different authored condition profiles or different evidence requirements.

A single observation can be sufficient evidence for one and insufficient for the other. The narrative tension is provenance and scope, not a generic `cold enough` score.

### The Old Warehouse Is Gone, the Bay Numbers Remain

A former refrigerated district has been redeveloped. Older workers, carriers and residents still describe the new location using obsolete bay numbers and loading-door names.

Useful for finding a person, reconstructing a shipment, locating a buried utility route or understanding why an alley has an unusual name.

### The Backup Is Real, the Readiness Is Old

A clinic, restaurant, research station or depot has a backup arrangement documented in its continuity plan. Evidence that the backup currently supports the needed profile is outdated or missing.

The existence of backup equipment does not automatically establish readiness.

### The Container Was Never the Problem

Several people blame an old transport container for a recurring condition gap. The records instead show that every disputed observation occurred during a transfer between two otherwise healthy segments.

The story can redirect attention from a blamed asset to a weak handoff process without requiring sabotage.

### The Pokémon Sleeps by the Door

A specific Pokémon repeatedly rests near the same cold-room entrance at a predictable time.

Possible narrative meanings: habit, companionship with a worker, access to a quiet corner, association with deliveries, attraction to a harmless local feature, or an unknown reason.

Never infer cold immunity, refrigeration ability or early-warning capability from species/Type.

### The Restaurant Has Stock, the Menu Still Changed

Goods physically exist in storage, but part of the inventory remains under condition review after an evidence gap. The restaurant changes its menu temporarily.

Food service state and warehouse presence remain separate.

### The Clinic Received the Shipment, Treatment Still Waits

A medical-supply shipment is delivered and stored. Care cannot yet use the relevant units because the condition evidence has been handed to the appropriate review owner.

No medical effect, potency loss or patient outcome is invented.

### The First Reading Was Correct at the Time

A monitoring device record is later superseded by a better observation or revised interpretation. The old record remains historically valid as what operators knew then.

Use this to support fair investigations where earlier actions were reasonable under incomplete evidence.

### The Night Transfer Everyone Remembers Differently

A disruption forced a one-time transfer of goods through an alternate route. Participants remember different start/end times because they are referring to vehicle departure, custody handoff, arrival at the temporary room or verification completion.

The contradiction can resolve through event identity rather than declaring witnesses dishonest.

## Mystery 1 — Five Temperatures, Three Subjects

Premise: five condition claims appear in records for one disrupted morning, but only three controlled subjects existed.

Resolution structure:

- one value belongs to the storage zone before a transfer;
- one belongs to the transport compartment;
- one belongs to a temporary room;
- one is a repeated report of an earlier observation;
- one is a later interpretation attached to the wrong timestamp in a human summary.

The mystery uses IDs, time, location and provenance. It does not require the narrative engine to calculate whether any numeric value was mechanically harmful.

Possible consequence: the affected-scope hypothesis becomes narrower or broader, then Batch Traceability/Care/Food resolves disposition under its authority.

## Mystery 2 — Four Handovers, Two Custody Changes

Premise: workers say the goods were `handed over` four times, while Courier records only two custody transfers.

Investigation can distinguish:

- physical move from shelf to staging;
- condition-verification interaction;
- carrier custody transfer;
- destination receiving acknowledgement.

All four statements can be truthful while describing different events.

## NPC and institutional archetypes

### The Continuity Coordinator

An actor who understands how storage, transport and downstream services connect. This is a narrative occupation only. It grants no Skill rank, Feature, item effect or authority unless separately authored.

Useful tension: knows the process extremely well but cannot personally clear a held batch.

### The Veteran Bay Worker

Remembers old facilities, loading schedules, temporary routes and renamed spaces. Their memory is valuable provenance but can still be incomplete or timestamp-dependent.

### The Receiving Clerk Who Records Everything

Maintains careful handoff observations. Their records can make a mundane delivery important months later without turning the NPC into an omniscient investigator.

### The Carrier With the Alternate Route

Built local trust during a previous interruption by learning a difficult temporary route. The route can later become useful for rescue, festival logistics or ordinary commerce.

### The Skeptical Reviewer

Refuses to collapse `equipment running` into `subject cleared`. This actor can initially appear obstructive while actually preserving correct authority boundaries.

### The Pokémon With a Work Relationship

An individually authored Pokémon assists a specific worker or facility in a non-mechanical role. Any cooling, sensing, carrying or technical function that relies on PTU capability requires exact validation before execution.

## Faction/institution dynamics

### Clinic versus market space

A disruption creates social pressure over a limited temporary controlled space. The system should not assume legal or moral priority. Local institutions negotiate based on authored culture, agreements and current stakes.

### Small carrier versus regional depot

A regional depot has stronger infrastructure but a small carrier knows the only verified temporary handoff route. This creates interdependence instead of a simple `big institution wins` hierarchy.

### Old workforce versus redevelopment authority

Redevelopment removes a cold-storage facility. Former workers care about names, routines and history; planners care about the new use. The conflict can produce memorialization, archives, wayfinding quirks and social bonds without requiring villainy.

## Exploration concept — The Route Behind the Freezer Wall

NON-CANON premise:

A modern controlled-storage room was built inside an older logistics building. Renovation records, obsolete loading diagrams and maintenance maps disagree about a service corridor that once connected two bays.

Current-capability version:

- investigate old plans and worker testimony;
- reconcile location IDs across renovation eras;
- enter only inspected static corridors;
- recover provenance about the former facility or missing handoff route;
- keep active refrigeration machinery outside BattleSpec.

Full environmental version, future only:

Could include authored cold zones, slippery surfaces, changing access after equipment state changes, timed isolation doors or other hazards. Every such mechanic requires an exact PTU/Caelo rule plus the relevant engine capability family. No native Minecraft ice behavior substitutes for those rules.

## Encounter 1 — Loading-Bay Withdrawal

Narrative premise:

Conflict reaches a loading area during a controlled-goods transfer. Workers and noncombatants need to leave while the goods remain isolated.

Full intended version:

- explicit combatants selected by Ouros;
- withdrawal/protection objective;
- multiple legal routes;
- Intercept/forced movement where legal;
- generalized reaction windows where exact mechanics apply;
- optional static restricted zones around equipment;
- tactical AI understands route protection rather than only damage maximization;
- semantic adapter plays authoritative movement/target/reaction outcomes.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if timed withdrawal matters;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when exact legal effects apply;
- terrain/weather/hazards/zones/reactions — BLOCKING for generalized reactions/restricted operational zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for protection/withdrawal behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

Stop the transfer before BattleSpec creation. Complete worker/civilian evacuation as overworld state. Controlled goods, vehicles and handling/refrigeration equipment remain outside the grid or inert/non-targetable scenery. AutoPTU resolves a static reviewed loading bay with explicit combatants. Victory can set `IMMEDIATE_LOADING_BAY_SECURED`; it cannot complete the transfer, restore condition control or clear goods.

## Encounter 2 — Backup-Room Perimeter

Narrative premise:

A temporary controlled room is prepared during an infrastructure interruption, but hostile actors or wild conflict makes its access perimeter unsafe.

Full intended version:

May require protection routes, Intercept/forced movement, generalized reactions, objective-aware AI and technical/environmental zones if active equipment has tactical meaning.

If cold exposure, condensation, slippery floor, electrical equipment or temperature effects are intended to change battle state, the encounter additionally depends directly on `terrain/weather/hazards/zones/reactions`, the relevant PARTIAL damage/status families and an exact governing PTU/Caelo effect.

Reduced version:

Verify and isolate the temporary room before combat. Keep controlled subjects, technicians and equipment outside BattleSpec. Resolve combat in a dry static corridor/yard. The result can secure access for later work. Facility readiness and subject transfer happen afterward through world-state systems.

## Encounter 3 — Interrupted Courier Diversion

Narrative premise:

A carrier transporting controlled goods cannot use its planned route. A conflict blocks the alternate handoff point.

Full intended version:

Could require protected withdrawal, route-aware tactical policy, Intercept/forced movement, generalized reactions and adapter playback. Active vehicle movement or environmental thermal effects would add exact terrain/hazard and vehicle-rule dependencies that are currently unverified.

Reduced version:

The carrier stops outside the tactical area and custody remains unchanged during combat. The shipment and vehicle do not enter BattleSpec. AutoPTU resolves a static route-junction encounter. Victory only secures the junction. Courier and cold-chain systems decide whether the leg resumes, reroutes or remains held.

## Longer arc — A Town Learns Its Cold Route

Phase 1 establishes ordinary life: a market, clinic, depot, carrier, restaurant, recurring workers, and specific Pokémon with authored relationships.

Phase 2 introduces a localized continuity interruption. Not every subject is affected equally. Some records are complete; others have gaps. A temporary room or alternate route changes daily movement.

Phase 3 creates social consequences rather than a single crisis meter: menu changes, postponed care use, changed dispatch schedules, borrowed space, new morning gatherings and arguments about what records mean.

Phase 4 restores infrastructure in stages. Future segments become verifiable before every earlier subject is cleared. Some temporary arrangements remain useful.

Phase 5 returns later. The original emergency is over, but an old bay name, a carrier route, a monitoring habit, a friendship or a decommissioned facility becomes relevant to a new story.

No `cold_chain_level`, `town_recovery_score` or universal safety number is created.

## Canon and mechanics guardrails

CANON-APPROVED: none of these situations, people, institutions or technologies.

PROPOSED: these templates may be instantiated only against existing world state and approved setting choices.

UNCERTAIN: exact technologies, operators, controlled goods, priorities, condition requirements, backup arrangements and Pokémon roles.

MECHANICALLY BLOCKED/PARTIAL where applicable: cold/slip zones, changing environmental conditions, generalized reactions, forced movement beyond verified slices, timed environmental phases, damage/status from cold, active vehicles/equipment, tactical protection policy and semantic playback.

Do not allow Minecraft ice, biome temperature, powder snow, redstone, frost particles or Cobblemon animations to manufacture these rules.