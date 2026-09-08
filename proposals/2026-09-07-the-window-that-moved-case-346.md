# The Window That Moved — Pass 346

Status: PROPOSED / NON-CANON
Date: 2026-09-07

Purpose

Exercise successor handoff authorization without adding a villain, fabrication, teleportation or mandatory combat.

Approved anchors reused

This proposal derives only from already established Marea facts:

- Teo Lark maintains field instruments at Puerto Bruma repair row;
- Dr. Nerea Sol works from Estación Mirador;
- Ema Rey performs equipment checks and field work under Nerea's project protocols;
- Puerto Bruma, Sendero del Vidrio and Estación Mirador are persistent authored places.

Everything about this specific scheduling incident remains non-canon.

Premise

Ema is authorized to collect a field instrument from Teo during a late-morning pickup window in Puerto Bruma. Before she leaves, another obligation moves her departure later than planned.

Ema sends a reschedule request proposing a later pickup at the Puerto Bruma Field Office instead of repair row because Teo expects to be there for an unrelated service call.

The request reaches Teo. He accepts the replacement.

The original authorization remains part of history. A new authorization becomes the operative one.

Why the distinction matters

Nerea may still be looking at the earlier schedule.

A coworker can truthfully say that Ema had permission to collect the instrument at repair row, because that was true when the first authorization was created.

Teo can truthfully say the pickup was moved.

Ema can know the request was sent while still not knowing whether Nerea received the updated plan.

No actor needs to be wrong about the fact they personally observed. Their records can simply refer to different points in the authorization lineage.

Player-facing investigation / assistance loop

The player can reconstruct:

- the original handoff authorization;
- the RESCHEDULE_REQUEST notice;
- whether Teo actually received it;
- Teo's ACCEPT or REJECT decision;
- the successor authorization ID;
- the new place and time window;
- which participants learned about the change;
- whether Ema departed according to old or new information;
- whether the resource itself actually moved.

Potential resolutions include carrying the updated message to Nerea, helping Ema reorganize another obligation, verifying the later pickup location, or simply letting the new arrangement proceed while recording the change correctly.

Reduced implementation version

Run entirely in world-agent state:

- semantic time;
- Pass 343 handoff authorization;
- Pass 345 reschedule request delivery;
- Pass 346 acceptance/rejection and successor authorization;
- ordinary travel and communication;
- belief/memory divergence between actors;
- event-driven replanning.

No AutoPTU handoff is required.

Mechanically rich version

A later field interruption may occur after Ema physically collects the instrument. The narrative objective would be to preserve the delivery or reach Mirador, rather than automatically defeat every opposing Pokémon.

Capability dependencies for that variant:

- targeting / footprints / range / LoS: exact tactical geometry if interception occurs;
- base movement legality: ordinary movement during the encounter;
- complete movement: carrying restrictions, interception, rescue, push/pull, knockback or forced movement;
- core calculations: ordinary PTU arithmetic;
- action economy / initiative: tactical pickup/drop/handoff/guard interactions;
- full turn / round lifecycle: round-bound objective windows or delayed updates;
- full stateful damage pipeline: authoritative damage to actors or equipment;
- status lifecycle: persistent conditions;
- terrain / weather / hazards / zones / reactions: only if the authored site uses them;
- move-specific behavior, abilities, items and Trainer Features/perks: each exact mechanic individually gated;
- AI legal-action infrastructure: needed for any new objective interaction action;
- AI tactical policy: currently blocking for delivery/protection/retreat goals that differ from simple defeat;
- Minecraft/Cobblemon/Craftics adapter/playback: presentation only and still partial/blocking end-to-end.

Narrative premise preservation

If the rich tactical version cannot run yet, the same story survives unchanged. The later interruption can remain an off-screen route delay, a blocked path, or a communication problem. The reschedule lineage and world consequences still function.

Canon questions

- whether Teo routinely performs service calls from the Puerto Bruma Field Office;
- whether Ema has standing authority to request location changes for this class of equipment;
- whether Nerea must explicitly approve schedule changes or only be informed;
- whether the institution requires the old authorization to be formally cancelled in addition to being superseded;
- whether any future trust consequence should attach to missed updates.

Until reviewed, none of those points becomes canon.
