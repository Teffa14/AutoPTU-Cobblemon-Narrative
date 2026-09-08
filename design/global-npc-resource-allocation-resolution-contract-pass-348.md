# Global NPC resource allocation resolution contract — Pass 348

Status: IMPLEMENTED GLOBAL CONTRACT

## Purpose

Preserve a provenance-backed institutional response when Pass 347 detects that a proposed resource handoff window overlaps unrelated active reservations for the same indivisible resource.

This layer records who was authorized to decide, what conflict set they saw, what course they selected and what evidence/policy they cited.

It does not create a universal priority policy.

## Existing owners retained

- Pass 201 owns identity, credential and delegated-authority semantics.
- Pass 339 owns reservation lifecycle.
- Pass 343 owns physical handoff/custody.
- Pass 346 owns successor handoff authorization.
- Pass 347 owns conflict admission/read assessment.
- Pass 202 may record mutual-aid allocation for relief-specific workflows.

Pass 348 is the global conflict-resolution provenance seam for resource-window conflicts.

## Executable records

`AllocationAuthorityEvidence` is an adapter result representing a prior authority check. It does not derive authority itself.

Required evidence:
- stable authority-check ID;
- exact decision actor;
- action scope `ALLOCATE_RESOURCE_WINDOW`;
- exact resource ID;
- current authority state;
- semantic time window.

`ResourceAllocationResolution` records:
- stable resolution ID;
- source reschedule proposal;
- resource ID;
- decision actor;
- authority-check reference;
- resolution kind;
- decision tick;
- exact conflicting reservation IDs visible to the decision;
- optional selected existing reservation;
- basis/evidence references.

## Supported V1 resolutions

`SELECT_PROPOSED_WINDOW`
The authority holder chooses the proposed successor window as the preferred course. Downstream systems still need to modify/release conflicting reservations and materialize any handoff changes.

`SELECT_EXISTING_RESERVATION`
The authority holder keeps one currently conflicting reservation as the preferred course. The proposed reschedule still needs an explicit rejection, alternative or further negotiation downstream.

`DEFER`
The authority holder records that no allocation decision is made yet. This preserves a valid blocked state.

## Hard boundaries

`RESOURCE_CONFLICT_DETECTED != RESOURCE_CONFLICT_RESOLVED`

`DECISION_ACTOR_PRESENT != DECISION_ACTOR_AUTHORIZED`

`AUTHORIZED_FOR_RESOURCE_A != AUTHORIZED_FOR_RESOURCE_B`

`AUTHORITY_ONCE_VALID != AUTHORITY_CURRENT_NOW`

`ALLOCATION_DECISION != RESERVATION_CANCELLED`

`ALLOCATION_DECISION != SUCCESSOR_HANDOFF_ACCEPTED`

`ALLOCATION_DECISION != RESOURCE_TRANSFERRED`

`ALLOCATION_DECISION != RESOURCE_USED`

`LOCAL_PRIORITY_POLICY != GLOBAL_OUROS_PRIORITY`

`ALLOCATION_PRIORITY != PTU_INITIATIVE`

`RESOURCE_SELECTED != PTU_ITEM_EFFECT_IMPLEMENTED`

## Failure behavior

The executable seam fails closed when:
- there is no actual Pass 347 conflict;
- decision actor and authority evidence actor differ;
- authority action scope differs;
- authority references another resource;
- authority is not established;
- authority is outside its validity window;
- an existing reservation is selected but is absent from the current conflict set;
- a resolution ID is reused.

## Determinism

Conflict reservation IDs are stored in stable order. Ledger entries are stable by resolution ID. The resolution does not mutate the Pass 347 assessment or reservation ledger.

## Narrative use

A scarce instrument can be legitimately promised to two different tasks by different scheduling paths. Once the conflict is detected, a scoped allocator may choose a course using evidence available at that time. Later characters can disagree with the decision without rewriting who made it or what they knew.

Repeated allocation decisions can eventually support institutional worldbuilding such as procurement requests, scheduling reform, maintenance expansion or friction between teams. Those consequences need their own evidence and owners.

## Encounter dependency contract

The reduced version is world-state only. It requires semantic time, resource reservations, authority evidence, communication, replanning and the Pass 347 admission seam. It requires no AutoPTU capability.

A rich version may occur after the selected resource is physically moving or while a time-critical field task is underway.

Current capability classification:
- targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts;
- base movement legality: VERIFIED within previously audited ordinary contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within previously audited ordinary contracts;
- action economy/initiative: VERIFIED for audited primitives; exact pickup/drop/handoff/guard actions remain individually gated;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for ordinary audited action-generation scope;
- AI tactical policy: BLOCKING for delivery-first, protect-carrier, retreat-after-objective and other non-defeat tactical goals;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No representative mechanic promotes an entire capability family.
