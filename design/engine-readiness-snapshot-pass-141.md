# Engine Readiness Snapshot — Pass 141

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records the repository inspection, live engine evidence and capability dependencies checked while adding utility service-point, meter-reading and billing continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 141:

`2ec58fd1a360fbe3d9cb6366f8109b1c5a525948`

The complete recursive narrative tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked against:

- Electric Grid Generation & Distribution Continuity;
- Drinking-Water Treatment & Distribution Continuity;
- Infrastructure Outage & Restoration;
- Finance / Sponsorship / Risk;
- Human Identity / Name / Record Continuity;
- Place Name / Address / Location Reference Continuity;
- PTU/Caelo source scan;
- Pass 140 engine-readiness snapshot.

Repository searches did not reveal an existing dedicated owner for utility service-point account continuity, device/meter association, observed versus estimated readings or bill-correction lineage.

The boundary is narrow:

physical utility owners retain supply/topology truth;

Finance retains monetary settlement;

Identity retains actor linkage;

Place Reference retains location/address identity;

this extension retains the administrative/evidentiary chain connecting a persistent service point to observation devices, readings/estimates, billing periods and correction history.

## Public-source relevance to implementation

Public Pokémon and fangame material contributed history/reuse patterns for utility sites rather than new mechanics.

New Mauville demonstrates that a utility site's purpose, operating state, access and later ecological/social use can change independently.

Yureyu Power Plant demonstrates adaptive reuse of former industrial infrastructure as a later gameplay location.

Current Pokopia community discussions show a strong player expectation that visible utility infrastructure and settlement consequences feel coherent while also demonstrating why visual structure alone must not become authoritative service state.

Operational public sources supplied provenance architecture:

- actual/observed readings versus estimates;
- delayed or amended data;
- persistent connection/service-point identity across meter replacement;
- separate meter/device faults and physical outages;
- append-only correction rather than retroactive deletion.

None of those external systems, laws, tariffs or technologies become Ouros canon.

## AutoPTU-Java live evidence

Current head inspected:

`5f8c23950e5689a771b9c9d0772e7cc60e9a8197`

Commit:

`Add server-owned terrain skill-check resolver (#282)`

No newer AutoPTU-Java commit was present during Pass 141.

The inspected live commit adds `TerrainSkillCheckBonusResolver` and parity tests for the reusable terrain-context skill-check bonus involved in the Intercept path. The resolver handles eligible skill labels including Athletics, Acrobatics, Stealth, Perception and Survival under the exact Survivalist/Naturewalk gate represented in that implementation.

This remains meaningful but narrow evidence.

It does not verify the full permanent `terrain/weather/hazards/zones/reactions` capability family.

It also does not establish:

- generalized terrain objects;
- terrain creation/removal;
- all movement consequences of terrain;
- weather lifecycle;
- hazards lifecycle;
- dynamic zones;
- generalized reactions;
- reaction ordering;
- broad Push/Pull/Knockback;
- every forced-movement source;
- escort semantics;
- objective-aware tactical AI;
- semantic utility-state playback;
- any utility account, meter, reading or billing mechanic.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 141.

The commit remains explicitly presentation-only. It synchronizes cached Pixi dimensions after viewport resize and does not change battle rules or outcomes.

It does not establish semantic adapter/playback for utility service points, devices, readings, account relationships, bills, correction episodes, field crews or reconnection state.

## Permanent capability map — Pass 141

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Static reviewed BattleSpecs can rely on current targeting and spatial legality evidence for reduced encounter variants.

`base movement legality`

Baseline movement remains verified for conventional static tactical spaces.

`core calculations`

Previously established parity-backed baseline remains verified.

`action economy/initiative`

Baseline tactical initiative/action economy remains verified. Initiative has no authority over service-account priority, billing periods, readings, field-work scheduling or reconnection requests.

`AI legal-action infrastructure`

Legal action enumeration/validation remains verified. It does not establish objective policy for protecting inspectors, withdrawing civilians or clearing access routes.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Specific Intercept work has strong evidence, including server-owned terrain-context inputs in its covered path. The combined family remains partial. Broad Push, Pull, Knockback, all forced-movement sources, generalized escort movement and all interception/reaction contexts remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Staged inspector withdrawal, synchronized civilian movement and timed objective phases remain unverified as a complete family.

`full stateful damage pipeline`

Substantial implementation exists, but family completeness has not been established.

`status lifecycle`

Use only exact implemented statuses where governing contracts apply. Pass 141 creates no generic `METER_FAULT`, `ACCOUNT_DISPUTED`, `SERVICE_RESTRICTED` or `READING_ESTIMATED` tactical status.

`move-specific behavior`

Representative Moves do not establish family completeness. No Move reads a utility meter, validates billing data, reconnects a service point or settles an account automatically.

`abilities`

Representative Ability coverage remains partial. No Ability creates utility authority, account identity or meter accuracy by inference.

`items`

Items remain partial. A narrative meter, bill, service tag, cabinet or work order is not automatically a PTU combat Item.

`Trainer Features/perks`

The exact Survivalist/Naturewalk terrain-context resolver remains useful localized evidence. The full family is partial. No Feature grants universal utility inspection, billing, reconnection or account authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The permanent category remains blocking. Rich utility-site encounters may want protected corridors, technical work zones, wet/electrical environments, changing obstacles or generalized reactions. Those semantics cannot be inferred from the narrow terrain skill-check helper.

`AI tactical policy`

Rich encounter variants can require PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION or escort-aware decision making. Legal-action infrastructure alone does not provide those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection of service-point identity, device association, reading provenance, account state, bill version, administrative action request or utility-owner handoff.

## Encounter review — Meter Inspection Withdrawal Corridor

Narrative premise:

A utility inspector/reader is investigating a service-point/device mismatch when an independent territorial or hostile threat enters the service alley.

Full intended dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if generalized reactions, dynamic work zones or authored live hazards matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Inspectors and customers withdraw before BattleSpec creation.
2. Private records and interactive utility equipment remain outside the tactical grid.
3. Utility administrative state is frozen.
4. Ouros selects explicit combatants.
5. AutoPTU receives reviewed static alley geometry.
6. Victory may create only `IMMEDIATE_SERVICE_ALLEY_CLEAR`.
7. Inspection and administrative findings resume afterward under the owning systems.

`TACTICAL_VICTORY != DEVICE_ASSOCIATION_VERIFIED`.

`TACTICAL_VICTORY != READING_ACCEPTED`.

`TACTICAL_VICTORY != BILL_CORRECTED`.

## Encounter review — Reconnection Access Perimeter

Narrative premise:

An authorized field action is pending at a service point, while an unrelated tactical threat blocks safe access.

Full version requires the rich families if crew escort, moving work boundaries, generalized reactions or objective-aware behavior are active.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Any administrative authority/prerequisite is resolved before battle.
2. Crew, customers and technical equipment remain outside BattleSpec.
3. Physical utility state is frozen during battle.
4. AutoPTU resolves a conventional encounter on static reviewed geometry.
5. Victory may create `IMMEDIATE_APPROACH_CLEAR` only.
6. The physical utility owner separately performs and verifies technical action.
7. Downstream owners separately determine service readiness.

`APPROACH_CLEAR != SERVICE_RECONNECTED`.

`SERVICE_RECONNECTED != ACCOUNT_RECORD_CORRECT`.

`SERVICE_RECONNECTED != DOWNSTREAM_SERVICE_READY`.

## Encounter review — Temporary Service Point Chokepoint

Narrative premise:

A temporary market, festival, construction or relief utility endpoint exists nearby while territorial conflict blocks an access route.

Full version dependencies:

- complete movement — PARTIAL if escort/interception/forced movement is active;
- full lifecycle — PARTIAL for staged staff movement;
- terrain/weather/hazards/zones/reactions — BLOCKING if temporary cables, water edges, weather or work zones must become tactical semantics;
- AI tactical policy — BLOCKING for route-protection behavior;
- adapter/playback — BLOCKING for semantic temporary-service state.

Reduced version status: READY.

Reduced contract:

1. The endpoint, device and staff remain outside BattleSpec.
2. Utility state does not change during combat.
3. A static neighboring chokepoint hosts the tactical encounter.
4. Victory may create `IMMEDIATE_ACCESS_ROUTE_CLEAR` only.
5. The utility owner separately decides activation, continuation, closure and verification.

`TACTICAL_VICTORY != TEMPORARY_SERVICE_ACTIVATED`.

## PTU / Caelo mechanical guardrails

The reviewed project source scan supports Jobs, Social activity, exploration, battles and location-specific mechanics when an exact governing source establishes them.

It does not establish a universal utility-customer or metering subsystem.

Remain UNKNOWN unless exact source evidence is found:

- generic utility account rules;
- universal meters;
- utility billing periods;
- tariff/consumption calculations;
- meter-reading Skill Checks;
- generic estimate mechanics;
- device calibration mechanics;
- meter-tampering detection;
- generic disconnection/reconnection mechanics;
- utility debt rules;
- meter or cabinet HP/DR;
- generic electrical/water work hazards;
- utility authority from Technology Education, General Education, Command, Perception or Survival;
- utility authority from Trainer Class or Feature;
- utility competence from Pokémon species or Type;
- battle victory resolving a bill or account dispute.

The server-owned terrain resolver must not be stretched into a utility inspection mechanic. Its exact Survivalist/Naturewalk terrain-context behavior does not imply that Perception, Survival or another Skill can verify meter data, account identity or technical safety.

## Minecraft / Cobblemon guardrails

Minecraft may present:

- old/new meter props;
- utility boxes and cabinets;
- labels and inspection tags;
- utility counters;
- barriers and work crews;
- inactive historical infrastructure;
- static cables/pipes;
- NPC routines;
- Pokémon workers/companions already authored by Ouros;
- UI derived from authoritative utility records.

Presentation does not create the records.

A redstone state does not prove physical utility availability.

A dial texture does not produce a reading.

A renamed block does not change service-point identity.

A scoreboard/objective value does not become an account number.

A Minecraft item stack does not create an issued bill or payment.

An open utility cabinet does not authorize reconnection.

Cobblemon BattleState remains non-authoritative for combatant selection, legality, HP/status, tactical position and all narrative utility consequences.

## Canon questions remaining open

- Which Ouros regions use customer-level utility accounts?
- Which utilities use individual meters, shared measurement, communal allocation or no measurement?
- Which operators and customer-service institutions exist?
- What service-point scale is used: building, household, shop, parcel, facility, district or another authored unit?
- What device technologies exist?
- Is remote metering present anywhere?
- Are estimates used?
- What information is private?
- Who can inspect/correct records?
- Which administrative events can request restriction or reconnection?
- Which financial pricing/subsidy models exist, if any?
- Which historical utility sites and old devices are canon?
- Which temporary utility connections exist for events, construction or crises?
- Which named Pokémon, if any, participate in utility field work?

All remain UNKNOWN/PROPOSED until canon work establishes them.

## Pass 141 conclusion

The new narrative layer is implementation-light at its core because its authority is world-state continuity and provenance rather than tactical rules.

The reduced encounters can run with currently verified targeting, base movement, calculations, initiative and legal-action infrastructure after all noncombat utility facts are resolved outside BattleSpec.

Mechanically rich variants continue to expose the same real blockers: complete movement remains partial; full lifecycle remains partial; terrain/weather/hazards/zones/reactions remains blocking as a combined family; tactical AI policy remains blocking; semantic Minecraft/Cobblemon/Craftics playback remains blocking.

No representative Intercept or terrain-helper implementation was treated as proof of family completeness.