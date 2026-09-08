# Global NPC resource handoff reschedule admission contract — Pass 347

Status: IMPLEMENTED GLOBAL CONTRACT

This layer screens a proposed successor handoff window against the existing indivisible-resource reservation ledger before downstream policy treats the new window as operationally clear.

It does not replace Pass 339 reservations, Pass 343 custody, Pass 345 communications or Pass 346 successor authorization.

## Authority boundary

Inputs:
- `ResourceHandoffRescheduleLedger`
- `ResourceHandoffLedger`
- `ReservationLedger`
- one stable proposal ID

Output:
- one deterministic `RescheduleAdmissionAssessment`

The layer does not:
- accept or reject a proposal on behalf of an NPC;
- cancel or create reservations;
- transfer custody;
- choose institutional priority;
- alter relationship state;
- fabricate alternate resources;
- initiate AutoPTU.

## Required distinctions

`RESCHEDULE_ACCEPTED != RESOURCE_WINDOW_CLEAR`

`RESOURCE_WINDOW_CONFLICT != ACTOR_FAULT`

`SAME_RESOURCE != SAME_PURPOSE`

`CANCELLED_RESERVATION_HISTORY != ACTIVE_CONFLICT`

`CONFLICT_FREE_WORLD_RESOURCE != PTU_ITEM_EFFECT_IMPLEMENTED`

## Admission states

`CLEAR`
The finite proposed window has no unrelated active reservation overlap for the same resource ID.

`CONFLICT`
At least one unrelated active reservation for the same resource overlaps the proposed window.

`UNKNOWN_PROPOSAL`
The referenced proposal does not exist in the reschedule ledger.

`UNKNOWN_AUTHORIZATION`
The proposal references an authorization absent from the handoff ledger.

`UNBOUNDED_WINDOW`
The successor handoff has no finite end tick. V1 does not claim conflict-free admission when it cannot compare a bounded interval.

## Same-purpose evidence

An overlapping active reservation is treated as evidence for the same work only when its `purpose_ref` explicitly matches one of:
- original handoff authorization ID;
- original resource request ID;
- current reschedule proposal ID.

Actor identity alone is insufficient. A reservation held by the same person for a different purpose can still conflict.

This avoids converting social identity into hidden allocation authority.

## Determinism

Conflicting reservation IDs and matched same-purpose reservation IDs are returned in stable reservation-ID order.

The assessment is a pure read model. Identical ledgers and proposal ID return identical results.

## Planner integration

The preferred future decision chain is:

reschedule request delivered
→ proposal authored
→ resource-window admission assessed
→ responder policy decides accept/reject/alternate
→ accepted proposal may materialize a successor authorization
→ successor still does not transfer custody

Pass 347 implements the assessment seam only. Pass 346 remains the low-level successor materialization owner.

## Encounter dependency contract

The reduced narrative use of this layer requires no tactical battle capability. It can run with semantic time, reservations, communications, handoff state, travel and replanning.

A rich field version may become tactical only after the resource is physically moving or a field objective is interrupted.

Current capability classification for such a rich version:
- targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts;
- base movement legality: VERIFIED within previously audited ordinary contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within previously audited ordinary contracts;
- action economy/initiative: VERIFIED for audited primitives; exact handoff/equip/drop actions remain individually gated;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for the ordinary audited action-generation scope;
- AI tactical policy: BLOCKING for delivery-first, escort, protect-carrier, disengage-after-objective and similar non-defeat objectives;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No representative mechanic promotes a whole category.
