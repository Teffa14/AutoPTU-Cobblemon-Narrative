# The Instrument That Was Ready Yesterday — Pass 340

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A field team has a legitimate booking for a shared measurement instrument. The correct NPC checks it out on time. The device is physically present, complete and apparently ordinary.

A current readiness check has not cleared it for the planned work.

The previous successful record is real. It is simply older than the current authored validity window.

No sabotage, theft or incompetence is required.

## Narrative purpose

This case tests the distinction between possession, reservation, technical readiness and evidence quality without making routine maintenance into chore spam.

The interesting decision is what the team does when an ordinary dependency fails shortly before departure.

## Evidence available

Potential evidence objects include:

- the active reservation;
- checkout/holder state;
- the previous readiness record;
- the current inspection or verification state;
- the source record that owns the technical conclusion;
- availability of a second instrument;
- schedule constraints for the field obligation;
- messages showing which actors received the readiness change and when.

Finding the instrument does not solve the problem. Reading the old READY record does not overwrite a later restriction.

## Possible branches

The team may postpone the measurement-dependent portion of the trip, perform only observations that do not require the instrument, request a different currently cleared device, alter the order of planned tasks, return the instrument for owner-controlled verification, or continue another obligation while waiting.

A supervisor may reasonably remember yesterday's successful use and initially believe the device is fine. A technician may reasonably know the current restriction but not know the field team's schedule. A dispatcher may know that a replacement exists but not whether it is reserved. These are different information states rather than contradictions that require a villain.

## Outcome boundaries

A completed repair does not by itself clear the instrument if the relevant owner still requires verification.

A current readiness record can clear ordinary world use but cannot create a PTU Item effect, Trainer Feature or tactical action.

A player physically holding the rendered object in Minecraft cannot override `INSPECTION_PENDING`, `MAINTENANCE`, `OUT_OF_SERVICE` or an explicit-readiness requirement.

## Reduced version

The complete case can run through world-agent state only.

Required systems are Pass 338 resource gating, Pass 339 reservation/checkout, Pass 340 readiness projection, semantic time, communication receipts, memory/belief and ordinary agenda replanning.

There is no battle dependency.

The smallest playable sequence is: collect the booked device; discover the current readiness state; identify the source record; choose a valid alternative; allow the schedule and later NPC knowledge to update from explicit events.

## Rich optional version

A later expedition can use a replacement instrument that is correctly cleared. During fieldwork, an unrelated encounter threatens access to the survey point or safe return route. The narrative premise remains resource-readiness and evidence collection; defeating every opponent is not automatically the success condition.

Exact capability dependencies for that version are visible:

- targeting / footprints / range / LoS: ordinary audited contracts VERIFIED; any instrument-targeting behavior separately gated;
- base movement legality: VERIFIED for ordinary audited movement;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL if carrying, rescue, interception or displacement matters;
- core calculations: VERIFIED for ordinary audited arithmetic;
- action economy / initiative: VERIFIED for ordinary primitives; instrument use during combat needs its own action contract;
- full turn / round lifecycle: PARTIAL for timed observations or environmental phase changes;
- full stateful damage pipeline: PARTIAL if actors or equipment can be damaged through new behavior;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING if field conditions become tactical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL and individually gated;
- Trainer Features / perks: PARTIAL and individually gated;
- AI legal-action infrastructure: VERIFIED for ordinary audited action generation, not invented survey actions;
- AI tactical policy: BLOCKING for protect-instrument, withdraw, escort or observation-over-defeat objectives;
- Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

The reduced version remains preferred until those exact rich dependencies are supported.

## Canon questions

Nothing here establishes a particular Ouros institution, instrument type, calibration interval, technical profession, legal authority, field protocol, Pokémon species, location, penalty or measurement standard.

Those details remain proposed until anchored to canon and the PTU/Caelo boundary where mechanics are involved.
