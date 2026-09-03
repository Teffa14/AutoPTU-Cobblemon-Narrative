# Marea Sendero forage-window compression event — Pass 241

Status: PROPOSED CONTENT / IMPLEMENTATION FIXTURE
Date: 2026-09-03
Canon effect: NONE

## Intent

Turn the ecology work from Passes 235–240 into one replayable world event that can exist independently of player presence, become known imperfectly, accept multiple interventions and leave persistent consequences.

The event uses existing canon only:

- Sendero del Vidrio lower shelf and seasonal crossing;
- the approved wild Fletchling population;
- existing Marea institutions and residents as possible observers/communicators.

It does not create a new species, population count, resource species, NPC, map anchor or rules-profile change.

## Premise

A normally broader forage opportunity becomes compressed into a shorter window. Existing Fletchling shift activity into that narrower period and space. The seasonal crossing overlaps with the concentration, raising human disturbance and avoidance pressure.

The visible symptom is “more Fletchling than usual in one place/time.” The hidden cause is not population growth.

## Why this is a useful first event

It simultaneously exercises:

- temporal ecology;
- activity vs abundance;
- disturbance/habituation;
- population conservation;
- projection leases;
- field observation;
- NPC knowledge divergence;
- intervention and delayed re-evaluation.

The event can therefore validate several previously separate contracts without requiring new canon content.

## Full state flow

```text
forage window compresses
-> activity becomes temporally concentrated
-> human route overlap rises
-> disturbance increases
-> Fletchling route/visibility pressure changes
-> observations and reports accumulate
-> institutions/players choose intervention or no action
-> overlap/disturbance/resource pressure changes
-> event re-evaluates
-> stabilizes, escalates or transforms
```

## Discovery

No omniscient quest marker is required.

Possible evidence channels from existing systems:

- repeated lower-shelf sightings;
- timing differences in Estación Mirador field notes;
- route-user reports from the seasonal crossing;
- direct resource-use observations;
- archived comparison showing that the activity window is unusually compressed.

Pass 240 determines what each holder actually knows.

A report saying “outbreak” is allowed as an NPC belief but must not become the world-system event type or population truth.

## Player-facing loop

A player can participate without fighting or catching anything.

Useful actions include observing the lower shelf at different times, comparing reports, helping communicate a temporary warning, assisting with route management, moving intrusive field equipment or simply leaving the area undisturbed and returning later to verify consequences.

The event remains group-compatible because several players can work on different evidence or intervention lanes at once.

## Consequence paths

### No intervention

If overlap remains high while the resource window contracts, disturbance can escalate. Possible state consequences include greater avoidance pressure, changed route use and poorer observation reliability because the population shifts away from the easiest viewing corridor.

This does not automatically cause mortality or emigration.

### Reduced traffic

A temporary access change lowers human overlap and disturbance. The event then enters stabilization only if subsequent evaluations satisfy clear conditions.

The route change can create a service/travel cost elsewhere. That trade-off can become a later settlement consequence without requiring the ecology system to declare the intervention morally “good.”

### Observation-only response

If the actual pressures remain safe, doing nothing except observing can be a valid result. The system should not force intervention merely because a quest exists.

### Late response

If the intervention happens after activity has already shifted, the event may resolve while leaving a changed route-use pattern. That can become a `TRANSFORMED` result rather than returning to the exact baseline.

## Reduced implementation version

The reduced version is entirely world-state driven:

- evaluate persistent variables;
- open one event instance;
- modify projection/activity weighting;
- emit observable symptoms;
- feed evidence into Pass 240;
- apply authorized world-service intervention deltas;
- re-evaluate with hysteresis;
- retain event history.

No AutoPTU battle is required.

This version should be implemented first.

## Rich structured encounter variant

If later content adds an active defense/escort/pursuit sequence near the crossing, Ouros must explicitly select combatants/objectives and hand them to AutoPTU.

Possible authored objective: keep a temporary passage corridor open while avoiding unnecessary engagement with wildlife.

Required capability families depend on the authored mechanics:

- targeting/footprints/range/LoS for structured visibility/targeting;
- base movement legality for movement;
- complete movement if interception, forced displacement, push/pull/knockback or corridor control is used;
- action economy/initiative for structured turns;
- full turn/round lifecycle for timed phases;
- stateful damage/status families if combat can damage or inflict statuses;
- terrain/weather/hazards/zones/reactions if the encounter uses them mechanically;
- exact Move/Ability/Item/Trainer Feature support for every selected record;
- AI legal-action infrastructure for legal choices;
- AI tactical policy for wildlife prioritizing flee/guard/corridor behavior;
- adapter/playback for end-to-end Minecraft presentation.

The reduced event does not wait on those blockers.

## Validation hooks

The companion implementation fixture `implementation/marea-sendero-ecology-world-event-fixture-v1.json` tests:

- trigger conjunctions;
- imperfect knowledge;
- non-authoritative rumors;
- escalation without intervention;
- pressure mutation through intervention;
- hysteresis;
- persistent post-resolution state;
- population conservation;
- Pass 239 lease requirements;
- explicit AutoPTU handoff.

## Canon questions deliberately left open

- What resource causes the forage window?
- What exact seasonal/calendar window is normal?
- Which resident or institution has authority to restrict traffic?
- What local service cost results from a closure?
- What numeric thresholds are suitable in production?
- Does the first production event end `RESOLVED` or `TRANSFORMED` under late intervention?

These should be answered by later evidence or implementation tuning rather than silently fixed here.