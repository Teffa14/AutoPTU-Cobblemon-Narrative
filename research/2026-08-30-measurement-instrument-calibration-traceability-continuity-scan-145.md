# Ouros Narrative Research — Measurement Instrument, Calibration & Traceability Continuity — Pass 145

Status: RESEARCH / PROVENANCE ONLY. This file does not establish Ouros canon.
Date: 2026-08-30

## Research objective

Pass 145 investigates a gap between existing Science measurements and the physical, historical life of the instruments that produce them.

The existing Science layer already records a measurement with `instrument_id`, method, unit/category, uncertainty and provenance. Air Quality, Weather, Wildlife Monitoring, Seismic, Volcanic, Astronomy, Utilities and other systems can already own domain observations and operational monitoring state. Material Culture can preserve a story-significant physical item instance.

What was missing before this pass was a neutral continuity layer that can answer questions such as:

- which physical instrument or measuring system produced a result;
- where that instrument was assigned at that moment;
- which configuration was active;
- which reference or comparison supported its calibration or verification;
- whether an operation was calibration, adjustment, cleaning, maintenance, repair or verification;
- when drift or an out-of-tolerance condition was discovered;
- which historical measurements are candidates for later review;
- whether a sensor replacement changed the monitoring point;
- whether a corrected result supersedes an earlier result without erasing the original record;
- whether a traceability claim applies to one measurement result rather than globally to an instrument.

The proposed layer is therefore about measurement provenance and instrument lifecycle. It must not become a universal science rules engine, a PTU Skill subsystem, a weather simulator, a laboratory simulator or a source of invented numeric precision.

## Narrative repository inspection

The complete recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected before writing. The tree returned `truncated: false` at head `c3c057e6356eb12f6f99ce374c370f3522ff0c8a`.

Relevant existing owners reviewed before selecting this gap include:

- `design/science-research-discovery-layer.md`;
- `design/air-quality-monitoring-airborne-condition-continuity-extension.md`;
- `design/wildlife-monitoring-tagging-telemetry-extension.md`;
- weather, seismic, volcanic and astronomy continuity files identified in the complete tree;
- utility service-point/meter continuity;
- Material Culture / Crafting;
- encounter implementation contracts and the latest engine-readiness snapshot;
- `research/2026-08-18-source-scan.md` for internal PTU/Caelo guardrails.

Repository search for `calibration calibrated instrument sensor drift metrology traceability` returned no dedicated implementation before Pass 145.

The gap therefore does not replace Science. Science owns research questions, methods, datasets, hypotheses, analyses, claims, replication and publication. Domain systems own what the measured phenomenon means. Material Culture owns the physical object where an individual instrument needs item provenance. Pass 145 proposes the continuity among instrument identity, assignment, reference, calibration/verification, indication, measurement result and later quality review.

## Public Pokémon material

### Silph Scope

Source: https://bulbapedia.bulbagarden.net/wiki/Silph_Scope

The Silph Scope changes what the player can identify in Pokémon Tower. The reusable pattern is epistemic rather than mechanical: a device can mediate observation or identification without creating the underlying subject.

Ouros transformation:

- a measuring or observing device can make a phenomenon observable under a bounded method;
- device output must remain separate from world truth;
- having the device does not make the operator omniscient;
- an observation made without sufficient method/equipment can remain unresolved rather than being converted into a false answer;
- the exact Silph Scope, ghosts, story gating and battle rules are not transferred.

### Devon Scope

Source: https://bulbapedia.bulbagarden.net/wiki/Devon_Scope

The Devon Scope signals otherwise unseen Pokémon and changes traversal possibilities in specific game contexts.

Reusable lesson:

A purpose-built instrument can answer a narrow observational question. Its success at that question does not imply general sensing authority.

Ouros transformation:

A field instrument may be validated for one variable, range, method or environmental condition while remaining unsuitable for another. A specialized detection method must not turn into a universal scanner.

No Devon Corporation lore, Kecleon encounter placement, item gating or exact game effect is imported.

## Public Pokémon Tabletop community material

### Researcher identity remains broader than one class label

Source: https://www.reddit.com/r/PokemonTabletop/comments/1dowl9g

A public PTU discussion explicitly notes that a player can portray a scientist through Skills and roleplay without treating one class label as mandatory flavor. The post is community interpretation, not rules authority.

Reusable lesson:

Scientific identity, institutional role and instrument competence should remain distinct from mechanical class names. Ouros should never infer that a person can calibrate, repair or interpret every instrument because their narrative role says `scientist`, nor should it require a single PTU class to participate in research fiction.

### Research missions as world hooks

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/rpj1n3
- https://www.reddit.com/r/PokemonTabletop/comments/116vkgr

Public anecdotes show scientist NPCs and research locations functioning as quest generators, information brokers and continuity anchors. They also show how laboratory discoveries can become intertwined with larger faction plots.

Reusable lesson:

The interesting story object is often the provenance and consequence of a result rather than a laboratory minigame. A field station, disputed dataset, damaged instrument or questionable result can create a mission whose resolution feeds a larger arc.

No original NPC, villain, prototype, dialogue or plot from those posts is copied.

## Metrology and measurement-science research

### NIST — metrological traceability belongs to the result

Source: https://www.nist.gov/metrology/metrological-traceability

NIST describes metrological traceability as a property of a measurement result connected to a specified reference through a documented chain of calibrations, with uncertainty contributed through the chain. NIST also states that simply using an instrument that was calibrated by NIST does not make every later result traceable.

Reusable architecture for Ouros:

- traceability claims attach to bounded measurement results or result sets;
- a calibration record is one part of the evidence chain;
- instrument identity, method, references, timing and measurement assurance all matter;
- old results must retain the chain that was available when they were produced;
- `INSTRUMENT_CALIBRATED != EVERY_RESULT_TRACEABLE`;
- `TRACEABILITY_DOCUMENTED != FIT_FOR_PURPOSE`.

No SI requirement, national metrology institution, accreditation model or real-world certification regime becomes Ouros canon.

### BIPM/JCGM VIM — calibration and adjustment are separate operations

Sources:
- https://jcgm.bipm.org/vim/en/2.39.html
- https://jcgm.bipm.org/vim/en/3.11.html

The VIM distinguishes calibration from adjustment. Calibration establishes relations used to obtain measurement results from indications under specified conditions. Adjustment changes the measuring system so that it produces prescribed indications; the VIM notes that adjustment should not be confused with calibration and usually requires recalibration afterward.

Reusable architecture:

- preserve calibration and adjustment as different event types;
- an adjustment cannot silently rewrite the calibration that preceded it;
- post-adjustment measurements need their own valid chain;
- a record can say an instrument was adjusted without claiming that the resulting measurements are automatically valid;
- cleaning, maintenance and repair also remain separate events.

The vocabulary is used as design provenance only. Ouros need not reproduce VIM terminology diegetically.

### USGS — preserve pre/post calibration and drift evidence

Sources:
- https://pubs.usgs.gov/publication/ofr20261008/full
- https://pubs.usgs.gov/publication/tm1D11/full
- https://pubs.usgs.gov/twri/twri9a6/twri9a67/twri9a_Section6.7_v2.1.pdf

USGS field guidance records readings before and after calibration, separates calibration verification from recalibration, and treats drift, fouling, sensor damage, operators and protocols as possible contributors to bias. Guidance for field fluorometers recommends verification before/after use or deployment at bounded intervals so later record processing can account for instrument performance.

Reusable architecture:

- preserve a pre-service or pre-adjustment check rather than overwriting it;
- preserve post-service verification separately;
- drift discovery opens a review question about a time interval rather than declaring every previous measurement false;
- cleaning can alter an instrument response and therefore should be a recorded maintenance event, not mislabeled as calibration;
- comparison with a reference can be evidence of performance without necessarily changing the instrument;
- the system should be able to represent `OUT_OF_TOLERANCE_DISCOVERED_AT_T2` while leaving the exact start of the problem uncertain.

No USGS tolerances, calibration frequencies, chemical standards or equipment specifications become Ouros canon.

### NOAA — station continuity can outlive individual sensors

Sources:
- https://www.ncei.noaa.gov/access/crn/instruments.html
- https://www.ncei.noaa.gov/access/crn/measurements.html
- https://ncc.nesdis.noaa.gov/about.php

NOAA climate-network documentation describes ongoing station measurements, recurring instrument calibration/verification, monitoring of instrument performance and routine replacement of aging sensors. Calibration centers also use reference observations to inter-calibrate instruments.

Reusable architecture:

A monitoring location or program can persist while individual sensors are repaired, replaced or reconfigured. Longitudinal continuity therefore needs separate identities for observation point, instrument instance and measurement stream.

`SENSOR_REPLACED != MONITORING_POINT_REPLACED`.

`STATION_CONTINUED != SAME_INSTRUMENT_CONTINUED`.

No NOAA network design, annual schedule, satellite procedure or climate standard is imported.

### EPA — collocation, correction and quality review

Sources:
- https://www.epa.gov/air-sensor-toolbox/air-sensor-collocation-instruction-guide
- https://www.epa.gov/air-sensor-toolbox/quality-assurance-air-sensors
- https://www.epa.gov/air-sensor-toolbox/air-sensor-collocation

EPA material distinguishes sensor maintenance, QC review, collocation against a reference monitor and correction of data. It warns that automated checks can miss subtle problems or flag genuine events, and describes collocation as simultaneous operation for comparison rather than proof that all later results are equivalent.

Reusable architecture:

- a comparison episode can involve two instruments at one place/time without merging their identities;
- a correction model can produce a derived/corrected result while preserving raw input;
- an automatic quality flag remains a flag, not a domain conclusion;
- a suspected outlier can survive review as a genuine event;
- comparison evidence can be method- and interval-specific;
- maintenance history and data-quality review belong in provenance.

No regulatory monitor class, pollution threshold, correction equation or legal standard becomes Ouros canon.

## High-level reusable structures

### 1. Instrument succession

A monitoring point or research program can use several instrument instances over time.

Narrative opportunities:

- old and new sensors overlap briefly for comparison;
- an instrument is removed for repair while a temporary unit fills the gap;
- two archives refer to the station by instrument serial rather than location;
- a famous long-running dataset crosses several hardware generations;
- an old instrument later becomes a museum or teaching object while its historical records remain active evidence.

### 2. Calibration chain as provenance graph

A result can refer to:

`result -> method/configuration -> instrument -> calibration/verification -> reference -> prior reference chain`

The graph can be incomplete without becoming false. Older institutions may preserve only partial records. A mystery can therefore end in bounded uncertainty.

### 3. Drift interval review

When performance falls outside an accepted authored condition, the system should create a review interval:

- earliest evidence known-good;
- latest evidence known-good;
- first evidence suspect;
- discovery time;
- candidate affected measurements;
- reviewed measurements;
- corrected/superseded outputs;
- unaffected records;
- unresolved interval.

The generator may not infer an exact failure start solely from discovery time.

### 4. Raw, corrected and interpreted values

Preserve layers:

`instrument indication -> raw record -> method-derived measurement result -> corrected/reprocessed result -> domain interpretation -> scientific/public claim`

A later correction should not erase the original. A public conclusion may remain historically important even after its supporting measurement is revised.

### 5. Fit for purpose

One result can be adequate for one decision and inadequate for another.

Examples:

- enough precision to confirm broad seasonal change but not a small local difference;
- adequate for equipment diagnostics but not a public scientific claim;
- useful as a field screening observation while requiring a reference method for stronger conclusions.

These are authored method/scope decisions. Pass 145 creates no universal numerical thresholds.

## Quest and mystery patterns extracted

### The Station That Never Moved

Three records seem to contradict one another because they list three sensor identifiers. Investigation shows the monitoring point remained stable while instruments were successively replaced.

Reusable pattern: identity disagreement caused by different object granularity.

### The Reading Before the Cleaning

A field log preserves an odd value before an instrument was cleaned. The later reading returns toward baseline. The interesting question becomes whether fouling, a genuine transient phenomenon or both contributed.

Reusable pattern: preserve pre-maintenance evidence and avoid automatic invalidation.

### The Reference Arrived Late

A remote team collected observations before the reference instrument reached the site. Some results remain useful at a lower evidence tier; later collocation cannot retroactively pretend the earlier comparison happened.

Reusable pattern: provenance constraints create partial usability rather than binary truth.

### The Famous Number Was Corrected

A public report quoted a value later superseded after drift review. The historical article remains an authentic record of what the institution believed at the time.

Reusable pattern: correction changes current interpretation while preserving public memory.

### The Sensor That Became a Landmark

A temporary monitoring deployment stays so long that residents name the corner after it. The sensor is eventually removed, but the local place-name survives.

Reusable pattern: technical infrastructure can leave social history after its technical role ends.

## Encounter-design implications

Measurement continuity is mostly overworld/world-state logic. A battle should rarely resolve scientific truth.

Mechanically rich versions may involve withdrawal corridors, fragile equipment areas, timed field operations or environmental conditions. Those concepts must expose exact engine dependencies instead of smuggling technical work into combat.

Candidate encounters prepared for Pass 145:

### Monitoring Station Withdrawal Corridor

Full premise: a field crew withdraws from a monitoring site while a tactical threat occupies the safe route. A rich version may use protected equipment lanes, Intercept, displacement, staged withdrawal or environmental zones.

Potential capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle only for exact chosen combatants/effects;
- terrain/weather/hazards/zones/reactions when the scene actually uses them;
- move-specific behavior;
- abilities;
- items only for exact PTU battle Items;
- Trainer Features/perks only for exact legal participation;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version: crew and instruments leave BattleSpec first; measurement state freezes; AutoPTU receives explicit combatants and static geometry; victory creates only `IMMEDIATE_STATION_APPROACH_CLEAR` or `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR`.

### Reference Instrument Handoff Chokepoint

Full premise: a reference instrument or comparison device is being moved between teams while a separate tactical threat blocks the approach.

Reduced version: the instrument and custodians remain outside BattleSpec. Battle resolves access to the handoff area, never calibration, custody transfer or measurement validity.

### Field Calibration Perimeter

Full premise: a team is preparing or conducting a bounded field calibration/verification when a threat reaches the perimeter. A rich version with timing windows, environmental zones or reactive movement remains dependent on those exact capability families.

Reduced version: the calibration pauses before BattleSpec. Technical state remains frozen. Victory clears the immediate perimeter. Calibration/verification restarts afterward under the world-state owner.

## PTU/Caelo cross-check

Internal project source evidence supports campaign plots, Jobs, sandbox activities, mechanically meaningful locations and exact skill/Feature/Move/Ability interactions where a governing source defines them.

The reviewed project evidence does not establish a universal metrology subsystem.

Remain UNKNOWN unless an exact PTU/Caelo source, test or implementation contract proves them:

- universal calibration rules;
- generic instrument-accuracy bonuses;
- universal sensor precision or drift rates;
- generic calibration intervals;
- universal uncertainty calculations;
- generic laboratory or field reference standards;
- universal Skill Check DCs for calibration, verification, adjustment or instrument repair;
- Technology Education as automatic calibration authority;
- General Education as automatic scientific-validation authority;
- Perception as automatic instrument diagnosis;
- Survival as automatic field-instrument competence;
- Focus as automatic precision bonus;
- Researcher or another class as universal instrument authority;
- Trainer Features/perks that automatically validate scientific results;
- species, Type, Move or Ability as universal sensor, calibration reference or measurement standard;
- Pokédex as a universally precise calibrated instrument;
- battle victory as measurement validation;
- generic instrument HP/Armor/DR or tactical durability.

If a future concept needs one of those mechanics, it must cite the governing source and the current engine capability evidence separately.

## Canon status

Nothing in this scan establishes that Ouros has:

- a centralized metrology institute;
- SI units or any particular unit system;
- mandatory calibration law;
- certification/accreditation;
- specific sensor technologies;
- standardized laboratories;
- universal measurement practices;
- regulatory air monitors;
- satellite calibration systems;
- named observatories or research institutions;
- numeric accuracy thresholds.

Those remain explicit canon decisions.

## Research conclusion

The strongest reusable lesson is that measurement continuity becomes narratively valuable when the project preserves the chain from physical instrument and bounded method to result, later quality review and downstream interpretation.

A broken, replaced or adjusted instrument can create history without erasing prior observations. A disagreement between records can arise from timing, configuration, reference scope, drift, correction or different intended uses instead of fraud. This gives Ouros scientific mysteries, field jobs, institutional memory and environmental storytelling while keeping PTU mechanics and domain conclusions under their existing authorities.