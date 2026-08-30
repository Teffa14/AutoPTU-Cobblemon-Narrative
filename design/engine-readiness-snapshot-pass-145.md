# Engine Readiness Snapshot — Pass 145

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-30

This snapshot records repository inspection, live engine evidence and permanent capability dependencies checked while adding proposed measurement-instrument, calibration and traceability continuity.

AutoPTU-Java and AutoPTU were inspected read-only. Pass 145 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 145:

`c3c057e6356eb12f6f99ce374c370f3522ff0c8a`

The complete recursive narrative tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked against the existing Science layer, Air Quality monitoring, Wildlife monitoring/telemetry, Weather, Seismic, Volcanic, Astronomy, Utilities, Material Culture, Shared Equipment, Facility Maintenance, Digital Systems, encounter implementation boundaries, PTU/Caelo source scan and Pass 144 readiness state.

Science already records `instrument_id`, method, unit/category and uncertainty on a measurement. Several domain layers already preserve monitoring sites, gaps and domain interpretation. Material Culture can preserve physical item identity. No dedicated layer before Pass 145 preserved instrument succession, configuration, calibration versus verification versus adjustment, bounded reference-chain provenance, drift review and result correction lineage.

Repository search for `calibration calibrated instrument sensor drift metrology traceability` returned no dedicated implementation before Pass 145.

## Research relevance

Public Pokémon material supplies a narrow sensing-device pattern through Silph Scope and Devon Scope: purpose-built devices can mediate identification or detection without creating the underlying phenomenon or granting universal knowledge.

Public PTU community material supports research/scientist NPCs and field/lab activity as campaign hooks while also illustrating that scientist identity should not be reduced to one mandatory mechanical class. Community posts are inspiration only and do not override PTU rules.

Public measurement-science sources supply provenance architecture:

- NIST: metrological traceability belongs to a bounded measurement result and requires a documented chain; a calibrated instrument alone does not make later results traceable or fit for every purpose.
- BIPM/JCGM VIM: calibration and adjustment are separate operations; adjustment generally requires recalibration.
- USGS: preserve pre/post calibration evidence, calibration verification, drift, fouling and maintenance history.
- NOAA: monitoring-station continuity can persist through routine sensor replacement and verification.
- EPA: collocation, maintenance, automated QC flags, correction and data review are distinguishable events.

No external unit system, calibration interval, regulatory threshold, laboratory accreditation model, instrument standard or technical procedure becomes Ouros canon.

## PTU/Caelo guardrail

Internal source-scan evidence supports campaign plots, Jobs, sandbox activities, mechanically meaningful locations and exact skill/Feature/Move/Ability interactions when governing sources define them.

No reviewed source establishes a universal calibration or metrology subsystem.

Remain UNKNOWN until exact source/tests/contracts establish them:

- universal calibration mechanics;
- universal verification mechanics;
- generic instrument-adjustment actions;
- universal measurement uncertainty rules;
- universal units or reference standards;
- generic instrument precision or drift;
- generic calibration intervals;
- generic calibration/verification/repair Skill Check DCs;
- Technology Education as universal instrument authority;
- General Education as universal scientific-validation authority;
- Perception as automatic instrument diagnosis;
- Survival as universal field-instrument competence;
- Focus as a generic precision bonus;
- Researcher or another class as universal metrology authority;
- Trainer Features/perks as automatic scientific validation;
- species/Type/Move/Ability as automatic sensor, calibrated reference or measurement standard;
- Pokédex as a universally calibrated precision instrument;
- generic instrument HP/Armor/DR or item durability;
- battle victory as calibration, validation or scientific proof.

No narrative scene may invent these mechanics.

## AutoPTU-Java live evidence

Current head inspected:

`3b860c37f45afde559533393f8ac78a24cf7df5f`

Commit:

`Own Intercept check distance in PTU geometry (#285)`

This is newer than the `60e2357c4be960cab53215cf81476839be4038b5` head observed during the incomplete pre-Pass-145 research run.

The live patch adds server-owned calculation of Intercept check distance using PTU footprint geometry. `InterceptGeometryResolution.checkDistance` computes footprint distance from the interceptor to the chosen intercept position and floors overlap to distance one. `RuntimeInterceptCheckInputFactory` now derives that distance from authoritative runtime combatant position/size and the intercept position rather than accepting a rule-critical distance input from an adapter. Tests freeze footprint-distance, Medium-anchor and floor-one behavior.

This is meaningful new evidence for one exact Intercept path and for server ownership of a geometry-derived rule input.

It strengthens:

- the localized Intercept geometry contract;
- use of authoritative combatant footprint/position data;
- adapter-boundary discipline for a rule-critical distance input.

It does not establish:

- all Intercept cases;
- broad Push/Pull/Knockback;
- all forced-movement sources;
- escort movement;
- object pickup/carry/drop movement;
- moving platforms;
- generalized reaction ordering;
- generalized terrain lifecycle;
- weather lifecycle;
- hazards;
- dynamic zones;
- tactical AI policy;
- measurement or calibration mechanics;
- instrument durability;
- Minecraft/Cobblemon/Craftics semantic measurement playback.

No permanent capability family is promoted from this single representative path.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 145.

The change remains presentation-only. It synchronizes cached Pixi screen dimensions after viewport resize and explicitly does not change battle rules or outcomes.

It provides no semantic support for instrument identity, calibration, measurement points, traceability, drift review, corrections or scientific claims.

## Permanent capability map — Pass 145

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

The spatial baseline remains verified. The new AutoPTU-Java evidence strengthens one footprint-distance input inside Intercept but does not turn scientific equipment into tactical targets or prove moving-object semantics.

`base movement legality`

Conventional static movement remains verified. This does not establish escort movement, moving instruments, fragile-equipment lanes or restricted calibration perimeters.

`core calculations`

Parity-backed conventional calculations remain verified. This does not provide measurement uncertainty, calibration equations, drift correction, scientific precision or instrument performance formulas.

`action economy/initiative`

Conventional combatant action economy remains verified. This does not define calibration timing, staged technical work or instrument-handoff procedures.

`AI legal-action infrastructure`

Legal-action enumeration/validation remains verified. It does not supply `WITHDRAW`, `PROTECT_EXIT`, `AVOID_EQUIPMENT`, `HOLD_PERIMETER` or escort-aware tactical policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The new server-owned Intercept check-distance geometry strengthens a specific covered Intercept path. Previous terrain/Naturewalk and Intercept evidence also remains relevant. The complete family stays partial because broad Push/Pull/Knockback, every forced-movement source, every Intercept case, escort movement and object-carry movement remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Staged technician withdrawal, timed handoff windows, phased field operations and delayed environmental changes are not verified as a complete family.

`full stateful damage pipeline`

Substantial implementation exists, but completeness remains unproven. It must not be repurposed as generic instrument damage, calibration loss, sensor drift or laboratory-equipment durability.

`status lifecycle`

Only exact implemented combat statuses are usable. Pass 145 does not create combat statuses such as `CALIBRATED`, `OUT_OF_TOLERANCE`, `UNDER_REVIEW`, `TRACEABLE`, `DRIFTING` or `REFERENCE_VALID`.

`move-specific behavior`

Representative coverage remains partial. No Move gains a measurement, calibration, sensing or scientific-validation effect unless exact governing rules establish it.

`abilities`

Representative Ability coverage remains partial. No Ability automatically calibrates an instrument, validates a result, detects drift or acts as a reference standard.

`items`

Mechanical Item coverage remains partial. A scientific instrument, calibration tag, reference artifact, field notebook or sensor is not automatically a PTU combat Item.

`Trainer Features/perks`

Localized server-owned terrain/Naturewalk/Intercept evidence does not establish generic research, metrology, calibration or instrument authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich field-science encounters may require weather phases, protected work zones, environmental hazards, generalized reactions or dynamic access. Existing localized terrain evidence does not complete this family.

`AI tactical policy`

Rich variants may require withdrawal, protection, perimeter holding, equipment avoidance or escort-aware behavior. Legal-action infrastructure alone does not supply these policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection of measurement-point identity, instrument succession, calibration state, verification state, drift review, result correction or traceability. The adapter remains presentation for facts already decided by Ouros.

## Encounter review — Monitoring Station Withdrawal Corridor

Narrative premise:

A field crew pauses monitoring and withdraws from a station while an unrelated tactical threat occupies the safe route.

Full dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active zones/environment are used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Monitoring pauses before combat.
2. Technicians, researchers, private records and instruments leave BattleSpec.
3. Measurement-point assignments and technical state freeze.
4. Ouros explicitly selects combatants.
5. AutoPTU receives static reviewed geometry.
6. No equipment damage, pickup, theft, calibration or sensing mechanics are invented.
7. Victory creates only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or `IMMEDIATE_STATION_APPROACH_CLEAR`.
8. Existing domain and measurement owners resume afterward.

`TACTICAL_VICTORY != INSTRUMENT_SERVICEABLE`.

`TACTICAL_VICTORY != MEASUREMENT_VALIDATED`.

`TACTICAL_VICTORY != MONITORING_RESUMED`.

## Encounter review — Reference Instrument Handoff Chokepoint

Narrative premise:

A reference/comparison instrument waits for a controlled handoff while a separate tactical threat blocks the approach.

Rich semantics remain dependent on the same PARTIAL/BLOCKING movement, lifecycle, terrain/reaction, tactical-policy and adapter families if moving custody, escort, timed exchange or reactive zones are part of the intended design.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Instrument and custodians remain outside BattleSpec.
2. Custody state freezes before combat.
3. AutoPTU resolves a static nearby encounter.
4. Victory creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only.
5. Existing owners perform later custody, comparison and calibration/verification events.

`APPROACH_CLEAR != CUSTODY_TRANSFERRED`.

`CUSTODY_TRANSFERRED != CALIBRATION_COMPLETED`.

`CALIBRATION_COMPLETED != RESULT_FIT_FOR_PURPOSE`.

## Encounter review — Field Calibration Perimeter

Narrative premise:

A bounded field calibration or verification operation is paused when a separate tactical threat reaches the work perimeter.

If the intended full version uses weather phases, active hazards, changing zones, generalized reactions, timed technical windows, Intercept or forced displacement, those exact capability families remain required.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Calibration/verification pauses before BattleSpec.
2. Instruments, references and technical records remain outside combat.
3. Pre-operation technical state stays frozen.
4. AutoPTU receives explicit combatants and static geometry.
5. Victory creates `IMMEDIATE_FIELD_WORK_PERIMETER_CLEAR` only.
6. The technical procedure restarts afterward under world-state ownership and may still be inconclusive or fail its authored criterion.

`PERIMETER_CLEAR != CALIBRATION_SUCCESS`.

`PERIMETER_CLEAR != ADJUSTMENT_PERFORMED`.

`PERIMETER_CLEAR != RESULT_TRACEABLE`.

## Reduced-version implementation rule

Pass 145 can advance before rich tactical support because its primary state is provenance continuity.

Before battle, world owners resolve or freeze:

- instrument identity;
- instrument custody;
- measurement-point identity;
- assignment and configuration;
- service/maintenance state;
- calibration and verification state;
- reference identity and provenance;
- Science measurement records;
- quality-review/correction state;
- private evidence visibility;
- noncombatants.

Battle receives explicit combatants and static reviewed geometry.

Battle returns only a narrow physical-access fact.

World-state owners resume afterward.

## Minecraft/Cobblemon/Craftics boundary

Presentation may display authored consequences such as sensor towers, monitoring huts, equipment cases, reference objects, technicians, old/new device models, maintenance tags, calibration records, mounting changes and retired instruments.

It may not infer:

- calibration from item proximity;
- scientific validity from a UI light;
- traceability from a label;
- instrument identity from entity UUID alone;
- monitoring-point identity from block coordinates alone;
- sensor replacement from despawn/spawn alone;
- a domain phenomenon from redstone or particles;
- instrument failure from a damaged cosmetic model;
- battle combatants from proximity.

Minecraft physics cannot become PTU instrument durability, measurement, calibration or scientific authority.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## Canon questions left open

Pass 145 deliberately does not decide:

- which Ouros regions or institutions perform formal calibration;
- whether standardized unit systems exist;
- whether dedicated reference laboratories or metrology institutions exist;
- what instruments exist in any region;
- which monitoring networks are canon;
- reference hierarchies;
- calibration/verification frequency;
- acceptable uncertainty/performance thresholds;
- fit-for-purpose rules;
- who may perform technical work;
- record retention or public access;
- community/citizen monitoring practices;
- named technicians, laboratories, observatories or field stations;
- Pokémon roles in instrument work;
- exact PTU/Caelo mechanics for measurement-related actions.

## Pass 145 conclusion

The narrative repository can safely add measurement-instrument continuity as an orchestration/provenance layer because Science and domain systems already own the actual observations and conclusions.

AutoPTU-Java gained one real piece of live evidence: server ownership of Intercept check distance through PTU footprint geometry. That strengthens a localized Intercept path but remains insufficient to promote the complete movement family or any other permanent category.

AutoPTU remains unchanged and presentation-only at its current head.

Rich field-science tactical variants remain blocked by exact movement, lifecycle, terrain/reaction, tactical-policy and adapter families. Reduced static variants are READY and keep calibration, measurement and scientific semantics outside BattleSpec.