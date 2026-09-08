# Global NPC resource handoff attempt and replanning contract — Pass 344

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

Purpose

Close the failed-fulfillment seam after Pass 343. Record an attempted authorized handoff that did not produce custody transfer, then wake the actors whose plans depend on that failure.

Target chain

accepted request -> handoff authorization -> attempted meeting -> success routes to Pass 343 custody transfer OR failure record -> selective replanning

Core boundaries

`HANDOFF_AUTHORIZED != HANDOFF_ATTEMPTED`

`HANDOFF_ATTEMPTED != RESOURCE_TRANSFERRED`

`NO_SHOW != REFUSAL`

`RESOURCE_ABSENT != RESOURCE_LOST`

`FAILED_ATTEMPT != AUTHORIZATION_DELETED`

`REFUSAL != OWNERSHIP_CHANGE`

`REPLAN_TRIGGERED != NEW_PLAN_SUCCEEDED`

Executable primitive

`tools/global_npc_resource_handoff_attempts.py` adds an append-only attempt ledger and an explicit bridge to the existing Pass 284 replanning queue.

`ResourceHandoffAttempt` records a stable attempt ID, authorization, observing/acting participant, authored handoff location, semantic time, failure outcome and optional observation provenance.

Supported V1 outcomes are provider absent, recipient absent, resource absent, provider refused, recipient refused and location blocked.

Validation

An attempt is accepted only when the referenced Pass 343 authorization exists, has not already produced a custody transfer, is within its valid window, occurs at the authored location and is recorded by an authorized participant.

Explicit provider or recipient refusal must be attributed to the corresponding role. A bystander cannot manufacture a refusal event.

Authorization state

`authorization_state()` derives `SCHEDULED`, `ACTIVE`, `REFUSED`, `COMPLETED` or `EXPIRED` without rewriting the authorization.

Ordinary absence does not consume the authorization. Another attempt may remain possible while the valid window is open.

Explicit refusal terminates the current authorization semantically. A later handoff requires a new agreement/authorization even though the old record remains queryable.

Replanning

`schedule_handoff_attempt_replans()` creates deterministic `EXTERNAL_EVENT` triggers for the provider, receiving actor and accountable requester, deduplicated by actor ID.

This wake-up does not choose the recovery action. Existing agenda, travel, communication and resource systems retain authority over the next plan.

Custody boundary

Pass 344 never mutates `WorldResource`, never changes holder identity and never creates a transfer. Successful physical exchange remains owned by Pass 343.

Narrative use

A worker can arrive and find the desk empty, discover that the provider moved the instrument, refuse a handoff because the underlying job changed, or encounter a temporarily blocked meeting place. Those facts can alter schedules and relationships later without being rewritten as theft, incompetence or deception.

Reduced version

The reduced scene needs no AutoPTU. It uses semantic time, handoff authorization, attempt provenance, communication, travel and event-driven replanning.

Rich version capability dependencies

A later encounter that physically blocks a courier or pickup site may add structured mechanics only when verified.

Targeting / footprints / range / LoS: required for exact tactical perception and target selection around a carrier or handoff point.

Base movement legality: required for ordinary tactical movement.

Complete movement: required for interception, carrying constraints, rescue, push/pull, knockback or forced displacement.

Core calculations: required for deterministic PTU arithmetic.

Action economy / initiative: required for tactical pickup, drop, handoff, guard or use actions.

Full turn / round lifecycle: required for round-bound deadlines, delayed arrival or staged objective changes.

Full stateful damage pipeline: required if actors or equipment can take authoritative damage.

Status lifecycle: required for persistent conditions affecting participants.

Terrain / weather / hazards / zones / reactions: required when site conditions dynamically block or alter the meeting.

Move-specific behavior: each exact Move individually gated.

Abilities: each exact Ability individually gated.

Items: each exact PTU Item effect individually gated.

Trainer Features/perks: each exact Feature individually gated.

AI legal-action infrastructure: required for any new tactical handoff/protection action.

AI tactical policy: required for choosing between delivery, protection, retreat, pursuit and defeat-oriented objectives.

Minecraft/Cobblemon/Craftics adapter/playback: presentation only. Proximity, animation or despawn cannot create an attempt, refusal or custody event.

Current live engine evidence

AutoPTU-Java head inspected: `b85fe17319d16e54402a5a45fb6acccd6b388553`, merge of PR #397, `Freeze Python Arena Trap target eligibility`.

This strengthens a narrow Arena Trap target-eligibility contract. It does not prove stateful application, complete movement, status lifecycle or the full Ability family.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit explicitly states presentation-only behavior.

Capability assessment

- targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts;
- base movement legality: VERIFIED for previously audited ordinary contracts;
- core calculations: VERIFIED for previously audited deterministic arithmetic;
- action economy / initiative: VERIFIED for current audited primitives;
- AI legal-action infrastructure: VERIFIED for its current ordinary scope;
- complete movement: PARTIAL;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL and individually gated;
- abilities: PARTIAL and individually gated;
- items: PARTIAL and individually gated;
- Trainer Features/perks: PARTIAL and individually gated;
- AI tactical policy: BLOCKING for delivery/protection/retreat objective policy;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

Acceptance cases

1. Unknown authorizations fail closed.
2. Completed authorizations cannot record later failed attempts.
3. Attempts must occur at the authored location and inside the valid window.
4. Only provider, receiving actor or accountable requester can record an attempt.
5. Provider/recipient refusal must come from the corresponding actor.
6. No-show and resource-absent attempts preserve authorization while its window remains active.
7. Refusal derives a terminal `REFUSED` state without deleting history.
8. Failed attempts never mutate resource custody.
9. Attempt history is deterministic and append-only.
10. Failed attempts can schedule selective event-driven replans for affected actors.
11. Replanning does not imply that a recovery action succeeded.
12. No attempt creates `REQUEST_AUTOPTU` or authorizes a PTU Item effect.

Deferred work

- communication-aware appointment confirmation and cancellation;
- explicit no-show expiry coordinator;
- failed-attempt trust/relationship policy where canon warrants it;
- travel-aware arrival evidence;
- return/overdue obligations already scoped by the older shared-equipment owner;
- checkpoint persistence for resource request/handoff/attempt ledgers;
- player inventory binding;
- Minecraft acknowledgement/UI;
- PTU/Caelo validation for mechanically active Items.
