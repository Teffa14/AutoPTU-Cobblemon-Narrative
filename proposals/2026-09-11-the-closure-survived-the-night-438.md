# The Closure Survived the Night — Pass 438

Status: PROPOSED / NON-CANON
Canon effect: NONE
Location assignment: UNRESOLVED

## Premise

A specialist has already accepted a narrow inspection appointment for the following morning. Before the appointment, a route or access point is closed on evidence the specialist receives personally.

The server crosses a sleep/restart boundary while the obstruction still exists.

When the world resumes, the appointment remains in the specialist's agenda and the pre-start blocker remains in its append-only viability history. Neither fact is reconstructed from dialogue. Neither one erases the other.

Later, the closure may clear before the promised window. If it does, the restored state becomes a new observation rather than a replacement for the earlier problem.

## Narrative value

This creates a small story with memory and accountability.

The requester can remember that help was promised. The responder can remember why departure was delayed. Another NPC may know only that the route reopened. A player arriving after the restart may see a reopened road without knowing there had been a closure at all.

Those differences can support later conversation, trust, investigation and explanation without requiring a hidden omniscient quest flag.

## Reduced implementation version

The reduced version needs only verified world-simulation infrastructure:

1. an assistance request and negotiated appointment;
2. an accepted responder-owned scheduled commitment;
3. a pre-start `BLOCKED` or `AT_RISK` viability observation with evidence/provenance;
4. one coherent V4 checkpoint and restore;
5. an optional later `RESTORED` observation if evidence shows the constraint cleared;
6. ordinary replanning from current world state.

Possible outcomes include proceeding normally after restoration, communicating the delay, missing the appointment, discovering that the inspection premise is no longer valid, or negotiating different terms.

No combat is required. No route reservation is implied by the commitment or blocker.

## Full field version

If the current world still contains a physical problem when the appointment begins, the same premise can lead to a field survey.

The specialist may need to reach a safe observation point, compare multiple environmental signs, protect another worker during inspection, retrieve a non-combat object, or withdraw if conditions deteriorate.

The objective is evidence and safe completion, not necessarily defeating every Pokémon in the area.

## Capability dependencies for the full version

Targeting/footprints/range/LoS: needed only if observation, protection or hostile actions require spatial targeting. Current status: VERIFIED only in audited scopes.

Base movement legality: needed for ordinary field movement. Current status: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: required if current, unstable footing, Pokémon attacks or protective interception can displace actors. Current status: PARTIAL.

Core calculations: needed for any ordinary PTU calculation used by the chosen scene. Current status: VERIFIED only in audited scopes.

Action economy/initiative: required once the survey becomes structured tactical resolution. Current status: PARTIAL.

Full turn/round lifecycle: required for multi-round tactical objectives, delayed changes or round-boundary effects. Current status: PARTIAL.

Full stateful damage pipeline: required if damage can occur and affect later state. Current status: PARTIAL.

Status lifecycle: required if a status persists, clears, ticks or modifies later behavior. Current status: PARTIAL.

Terrain/weather/hazards/zones/reactions: required for current, unstable terrain, weather phases, hazard zones, reaction movement or environmental interrupts. Current status: MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior: required only for concrete moves selected for the encounter. Current status: individually gated.

Abilities: required only for concrete ability-triggered behavior. Current status: PARTIAL and individually gated.

Items: required if equipment has authoritative mechanical effects rather than world-state labels. Current status: individually gated.

Trainer Features/perks: required if inspection/protection uses Trainer Feature effects or interrupts. Current status: individually gated; current Quick Switch evidence does not generalize.

AI legal-action infrastructure: required for specialized INSPECT, BRACE, ESCORT, PROTECT, RETRIEVE, CARRY or EXTRACT actions. Current status: those specialized actions need explicit admission.

AI tactical policy: required for the engine to choose among specialized objective actions. Current status: BLOCKING for those policies.

Minecraft/Cobblemon/Craftics adapter/playback support: required for specialized objective state, non-KO completion and recovery if a tactical session is projected into Minecraft. Current status: PARTIAL / BLOCKING.

## Reduced fallback for an unready engine

Keep the appointment, closure history, communication and evidence objective unchanged.

Resolve travel through verified world-route semantics. At the inspection site, use ordinary observation/evidence actions outside structured battle. If hostile Pokémon make the area unsafe and the required specialized objective policy is unavailable, end the local attempt as withdrawal/blocked access rather than inventing tactical rules in the adapter.

The narrative premise survives intact: the appointment existed, the closure happened, the world remembered both, and present conditions decide what happens next.

## Canon questions

No named location, NPC, species, institution or regional historical event is approved by this proposal.

If later bound to canon, the author must decide who controls the access point, what evidence can close or reopen it, who is authorized to inspect it and whether the job belongs to an existing questline family. Those decisions must use the relevant canon owner instead of being inferred from this example.
