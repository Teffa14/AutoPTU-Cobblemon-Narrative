# The Kit Booked Twice — Pass 338

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A shared field kit is needed by two valid obligations during overlapping windows. Nobody stole it. Nobody fabricated a request. Both tasks are legitimate and both NPCs can know that the institution owns the kit.

The conflict exists because one physical resource cannot satisfy two simultaneous deployments.

This case is intended as a regression story for the global resource-aware NPC planner. It may be bound to an established settlement or institution only after canon review.

## Story structure

One NPC has a scheduled ecological field visit whose preparation depends on a `FIELD_SAMPLE_KIT` capability.

Another NPC receives a later but more urgent assignment that needs the same capability.

The kit begins at a shared office or storage feature. Both actors know it exists. Both may have permission to use it. Only one can reserve or carry it at a time.

Possible branches include:

- the first reservation stands and the urgent job requests a substitute;
- the first actor voluntarily releases the reservation and reschedules;
- a supervisor reallocates the resource and records the displaced obligation;
- another compatible kit is borrowed through an existing relationship or institution;
- one actor travels to another cache if the route, permission and time actually permit it;
- the urgent task proceeds with a reduced non-mechanical observation plan while the resource-dependent work waits;
- poor communication causes both actors to arrive expecting the same kit, creating a repairable coordination failure without creating theft.

## Evidence and NPC knowledge

Useful persistent facts:

- resource identity;
- capability tags;
- current location;
- current holder;
- reservation holder and time window when that layer exists;
- request/approval messages actually received;
- each actor's schedule and obligation priority;
- whether an alternate resource is known to that actor;
- whether the actor is authorized to request or borrow from another pool.

An NPC who knows another kit exists somewhere in the region still cannot use it until ordinary travel, communication and permission state makes that possible.

## Consequences

The interesting aftermath is operational memory.

The institution may introduce clearer reservations, handoff logs, minimum stock, a borrowing agreement, a second kit purchase request, or a rule that urgent jobs include resource readiness before dispatch.

Those consequences remain proposed until a canon owner adopts them.

## Reduced playable version

The current reduced version can run entirely as world-agent state:

- one stable resource record;
- two resource-aware intents;
- deterministic availability gating;
- ordinary communication and replanning;
- explicit reservation state authored as a world event if needed;
- no combat required.

If both jobs occur at different times, completion of the first can release the resource through an explicit future event. Pass 338 itself does not mutate reservations or returns automatically.

## Mechanically rich version

A later branch can place one assignment in a structured encounter, for example protecting a field worker while equipment is deployed or recovering the kit from a dangerous location.

The narrative premise does not require that richness. If used, dependencies must be declared exactly.

Potential capability dependencies:

- targeting / footprints / range / LoS if equipment requires a tactical target or observation lane;
- base movement legality for reaching the equipment/work point;
- complete movement for carrying, dragging, rescue, interception or forced displacement;
- core calculations only where exact PTU arithmetic is invoked;
- action economy / initiative if transfer, setup or use is a tactical action;
- full turn / round lifecycle for timed setup, delayed activation or phase changes;
- full stateful damage pipeline if equipment can be damaged or protects against damage through verified rules;
- status lifecycle for verified persistent conditions;
- terrain / weather / hazards / zones / reactions for environmental interaction;
- move-specific behavior, abilities, items and Trainer Features/perks only for individually verified content;
- AI legal-action infrastructure for legal tactical action generation;
- AI tactical policy for choices such as protect equipment, share it, withdraw or finish a non-defeat objective;
- Minecraft/Cobblemon/Craftics adapter/playback for visual possession, setup and recipient-correct UI.

## Canon questions

Before binding this case to established Ouros geography, decide:

- which institution owns the resource;
- whether the field kit is a mundane world object or maps to exact PTU equipment;
- who may reserve it;
- how reservation windows are represented;
- whether substitute capability grades exist;
- whether acquisition/borrowing is automated by the NPC planner or authored through ordinary travel/communication intents;
- what persistent consequence, if any, is promoted after the first contention incident.
