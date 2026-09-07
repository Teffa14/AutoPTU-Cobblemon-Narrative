# Operational readiness, calibration and field-equipment scan — Pass 340

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Repository-fit check

The recursive narrative repository tree was enumerated before writing. The relevant existing owners were then read directly.

`design/shared-equipment-lending-issued-assets-extension.md` already owns temporary entitlement, reservation, checkout, assignment and return for shared assets. It explicitly says Maintenance owns readiness work and already includes `readiness_record_ref`, `INSPECTION_PENDING` and `MAINTENANCE` states.

`design/facility-maintenance-repair-inspection-extension.md` already owns condition observations, faults, assessments, work orders, repair, verification and reopening. It also separates physical condition from operational state and states that a repair can require verification before return to use.

Pass 338 added the executable generic resource-availability gate. Pass 339 added temporal reservations, checkout and return, and explicitly left inspection/repair/calibration as a later integration seam.

Therefore Pass 340 must not create another maintenance or calibration lifecycle. The useful missing layer is a read-only bridge by which authoritative readiness records can prevent the global NPC planner from treating a physically available resource as operationally usable.

## Public sources

### USGS Hydrologic Instrumentation Facility

Source: https://www.usgs.gov/labs/hydrologic-instrumentation-facility/about-hif

USGS describes a facility that provides quality-assured hydrologic equipment together with training, repairs, calibrations and testing. The stated purpose of calibration/testing is to verify measurement accuracy and whether instruments perform to required criteria before their field measurements are relied upon.

Reusable structure for Ouros:

An instrument can exist, be owned, be booked and be physically present while still requiring a separate readiness determination. Technical work and the planning decision that consumes its result should remain different records.

Excluded:

No USGS organizational hierarchy, procedures, calibration values, instrument models or legal standards become Ouros canon.

### USGS National Field Manual — multiparameter instruments

Source: https://www.usgs.gov/publications/use-multiparameter-instruments-routine-field-measurements

The 2023 USGS manual chapter explicitly groups storage, maintenance, calibration, troubleshooting, measurement and reporting as related but distinct parts of routine field-instrument use.

Reusable structure:

`stored` does not imply `ready`; `calibrated at some earlier time` does not by itself imply `valid for every later use`; troubleshooting and maintenance can interrupt otherwise ordinary fieldwork without implying sabotage or operator incompetence.

### USGS Idaho National Laboratory QA plan, 2026

Source: https://pubs.usgs.gov/publication/ofr20261008/full

The current 2026 plan describes recurring calibration and subsequent calibration checks during field campaigns. Its narrative value is temporal: a device can have passed earlier checks and still require later verification under an established quality process.

Reusable structure:

Readiness has semantic time. A prior successful record remains historical evidence but need not authorize current work after its validity window ends.

### NIST metrological traceability guidance

Sources:

https://www.nist.gov/metrology/metrological-traceability
https://www.nist.gov/calibrations/traceability

NIST distinguishes a calibration result for a particular device at a particular time from a blanket guarantee of future measurements. It further explains that traceability belongs to measurement results and depends on a documented chain rather than merely possessing an instrument that was once calibrated.

Reusable structures:

- `CALIBRATION_RECORD_EXISTS != CURRENT_USE_READY`
- `INSTRUMENT_CALIBRATED != EVERY_RESULT_VALID`
- a source record should retain identity and time rather than collapse into a permanent boolean flag;
- downstream systems should consume a narrow readiness conclusion while preserving the source reference that supports it.

Excluded:

No SI traceability requirement, laboratory accreditation requirement, uncertainty calculation or NIST policy is imposed on Ouros.

## Pokémon / PTU community scan

### Pokémon Tabletop United community variant — Pokémon: World Tour / PTU: VVV

Public source: https://www.reddit.com/r/PokemonTabletop/comments/1m6zdes

A 2025 community post describes a long-running PTU-derived campaign whose creator substantially modified the automated sheet and system into a named personal variant.

Reusable project lesson:

Public PTU campaign material is valuable for encounter and campaign structure, but community implementations may deliberately alter base mechanics. Research notes must therefore preserve the distinction between narrative inspiration and mechanical authority. A field-equipment story discovered in a campaign cannot establish an Ouros/PTU rule unless the project's PTU/Caelo source boundary independently supports it.

No variant mechanic, automated-sheet behavior, character, region or plot is adopted here.

## Original Ouros synthesis

The useful global chain is:

`persistent resource identity -> reservation / holder / location -> owner-supplied technical readiness record -> planner-only readiness projection -> Pass 338 resource gate -> ordinary global NPC intent scoring -> optional AutoPTU handoff`

The readiness bridge should know only enough to answer whether the resource may satisfy the current ordinary world prerequisite. It should retain `source_record_ref` and semantic validity time. It must never diagnose a fault, perform calibration, complete a work order or declare a repair successful.

Suggested bridge outcomes are intentionally coarse:

- `READY_FOR_AUTHORED_USE`
- `LIMITED`
- `INSPECTION_PENDING`
- `MAINTENANCE`
- `OUT_OF_SERVICE`
- `UNKNOWN`

In executable V1, only explicit `READY_FOR_AUTHORED_USE` is accepted when an intent requires an explicit readiness record. `LIMITED` remains conservative because the generic global planner does not know which limitation is acceptable for a domain-specific task.

## Narrative patterns enabled

A field team can reserve a meter, collect it on time and discover that an authoritative pre-use check has not cleared it. The blocked work can produce a narrow reschedule, request for another instrument, reduced observation-only task or later return after verification. Nothing about that sequence requires theft, negligence, sabotage or a villain.

A replacement device can be physically available but lack a current readiness record. The player may locate the object without thereby authoring technical permission to use it.

A prior successful verification can remain historically true after it expires. NPCs who only remember the earlier result can therefore make understandable but outdated plans, connecting resource readiness to the existing memory, belief and communication architecture.

## Mechanics boundary

This research does not define PTU Item effects, calibration checks, Education/Technology rolls, skill DCs, repair actions, equipment damage, measurement bonuses or Pokémon-assisted instrumentation.

If a resource later maps to a mechanical PTU Item, its world readiness and its tactical legality/effect support remain separate gates.
