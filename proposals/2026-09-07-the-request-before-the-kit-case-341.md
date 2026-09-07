# The Request Before the Kit — Pass 341

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A field team has a valid obligation and a narrow observation window, but the required instrument is not physically available at their location.

The instrument exists. It is operationally ready. Another named worker currently holds it for a legitimate task.

The blocked team knows who has it.

The adventure begins with the request, not with a magically transferred object.

## Why this belongs in Ouros

Persistent work should generate friction from the actual state of people, tools, schedules and routes. A needed instrument being elsewhere can create a meaningful short arc without inventing sabotage, theft or a villain.

The incident can expose:

- different obligations with competing urgency;
- incomplete knowledge about who still needs the instrument;
- communication latency;
- a provider who may agree, refuse or offer a later window;
- travel time between institutions;
- the cost of changing the order of work;
- relationship consequences from how the request is handled;
- a later record showing why one task was delayed.

## Proposed setup

Use an existing Marea Interior institution only as a regression site. Do not promote any new local equipment pool, job assignment or NPC ownership fact into canon without separate review.

A recurring NPC has a scheduled field observation that requires a capability such as `FIELD_METER`.

Pass 338 blocks the task because no matching resource is locally available.

The resource ledger shows one viable instrument currently held by another named actor at a different work site.

Pass 341 derives `REQUEST_RESOURCE` addressed to that holder.

Nothing else happens automatically.

## Possible branches

### Holder agrees

The holder may already be finished, may be able to release the instrument early or may offer a later handoff.

Agreement should create a new explicit state transition in a future provider-consent/transfer owner. It does not teleport the instrument.

The requester or another actor may then need to travel.

### Holder still needs it

The holder may refuse because their own obligation remains active.

The requester can:

- reschedule part of the field work;
- perform observations that do not need the instrument;
- search for another legitimate source;
- escalate through an institution if authority exists;
- wait for release;
- abandon the narrow window and record why.

Refusal alone is not hostility.

### Request arrives late

The communication may be delayed. The holder may finish before receiving it, or the field window may close first.

The world should preserve both facts rather than rewriting the request as pointless or never sent.

### Instrument is offered but remote

A later accepted transfer may require pickup through the existing travel graph.

If the requester has a reservation for the instrument at a remote location, Pass 341 can already derive travel to that reserved resource.

Actual travel remains owned by the global travel runtime.

### Another actor has the reservation

The blocked worker may see the physical instrument but still have no current claim to it.

The reduced system can derive `WAIT_FOR_RESOURCE` instead of stealing or silently cancelling another person's booking.

## Player-facing loop

A player can become involved because they are already present, have a relationship with one of the actors or are carrying another obligation between the same locations.

Useful actions can include:

- deliver a message when the normal channel is slow;
- ask the holder for a release window;
- carry a replacement after explicit authorization;
- help reorder the field team's non-instrument work;
- investigate whether another valid source exists;
- document the reason a time-sensitive observation was missed.

The player should never receive an invisible success flag simply for speaking to the correct NPC. The resource still needs a legitimate lifecycle transition.

## Reduced implementation

The reduced version uses only world-agent systems:

- semantic time;
- schedules/obligations;
- Pass 338 resource gating;
- Pass 339 reservation state when relevant;
- Pass 340 readiness projection;
- Pass 341 recovery-option derivation;
- communication delivery;
- travel planning;
- memory/belief;
- replanning.

No battle is required.

## Rich implementation

A later full version can place the eventual field observation inside a changing environmental scene. The instrument arrives, but the observation window overlaps with wild Pokémon activity or a hazard.

The narrative objective remains to complete or safely abandon the field task while preserving the instrument and subjects of observation.

### Exact mechanical dependency families

Targeting / footprints / range / LoS:
Required if the instrument or observation uses exact tactical targets or sight lines.

Base movement legality:
Required for ordinary tactical repositioning around the work site.

Complete movement:
Required for carrying, interception, rescue, forced movement, dragging or protecting the instrument during displacement.

Core calculations:
Required only for exact PTU arithmetic invoked by the encounter.

Action economy / initiative:
Required if handoff, deployment, activation or protection consumes structured actions.

Full turn / round lifecycle:
Required for observation windows, delayed setup, phase changes or timed environmental effects.

Full stateful damage pipeline:
Required if actors or equipment can take mechanically resolved damage.

Status lifecycle:
Required for persistent tactical conditions.

Terrain / weather / hazards / zones / reactions:
Required for any mechanically active storm, unsafe ground, observation zone or reaction-driven hazard.

Move-specific behavior:
Each exact Move remains individually gated.

Abilities:
Each exact Ability remains individually gated.

Items:
The world instrument does not gain a PTU Item effect unless that exact Item contract is verified.

Trainer Features/perks:
Each exact Feature remains individually gated.

AI legal-action infrastructure:
Needed for any new structured pickup, handoff, instrument-use or protect-object action.

AI tactical policy:
Needed for objectives such as protect the instrument, complete observation, withdraw safely or avoid harming the observed Pokémon.

Minecraft/Cobblemon/Craftics adapter/playback:
Needed only for presentation, local interaction and authoritative result playback.

## Consequences

A successful recovery can leave:

- a completed observation with traceable resource provenance;
- a delayed secondary job;
- gratitude or irritation between workers;
- a new reason to improve institutional equipment sharing;
- a future reservation made earlier because this delay is remembered.

A failed recovery can leave:

- a missed observation window;
- a truthful record that the work was blocked by equipment availability;
- no scientific result where none was collected;
- a follow-up commitment for another day;
- changed expectations between the actors.

Neither branch requires a villain.

## Canon questions

Before promotion, decide:

- which existing institution owns or administers the instrument;
- which named actors have the relevant jobs;
- whether the resource is mundane equipment or eventually maps to a PTU/Caelo Item;
- which communication channels connect the actors;
- what field observation is being attempted;
- whether the observation window is weather, tide, migration, schedule or another authored cause;
- whether player delivery is allowed by the owning institution;
- whether any rich variant needs structured combat at all.
