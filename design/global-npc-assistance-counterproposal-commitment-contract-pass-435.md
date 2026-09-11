# Global NPC Assistance Counterproposal Commitment Contract — Pass 435

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 434 gave the original requester an explicit durable ACCEPT or REJECT decision over one delivered counterproposal. Pass 435 turns only an accepted proposal with a complete future time window into responder-owned scheduled work.

Agreement and execution remain separate. The accepted proposal supplies the window. The requester acceptance supplies the causal provenance. The responder agenda owns the resulting `ScheduledCommitment`.

## Inputs and authority

The bridge consumes:

- `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` for request, responder counterproposal and requester acceptance;
- `OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1` for the exact proposed terms;
- `OUROS_ASSISTANCE_COUNTERPROPOSAL_COMMITMENT_LEDGER_V1` for the durable proposal-to-commitment linkage;
- the existing global NPC agenda for ordinary scheduled work.

No new scheduler is introduced.

## Required causal chain

Before materialization the bridge verifies:

1. the original request remains a PLANNED `REQUEST_ASSISTANCE`;
2. the responder action remains a PLANNED `COUNTERPROPOSE_ASSISTANCE_REQUEST`;
3. proposal provenance still points at that responder action;
4. requester and responder identities match across request, response and proposal;
5. the requester decision is a PLANNED `ACCEPT_ASSISTANCE_COUNTERPROPOSAL`;
6. the requester acceptance targets the responder and names the exact `proposal_id` in `source_ref`;
7. the acceptance does not predate the counterproposal;
8. an expired proposal did not receive a late acceptance;
9. the proposal supplies both `proposed_start_minute` and `proposed_end_minute`;
10. materialization does not reserve a window whose start has already passed.

Pass 434 remains responsible for proving that the acceptance itself came from terminal delivery of the exact structured terms. Pass 435 consumes that durable accepted world action rather than duplicating the communication owner.

## Exact-term rule

The scheduled window is copied directly from the proposal. Callers cannot replace it with a more convenient time.

`location_ref`, `scope_ref` and `alternative_ref` are retained in the commitment linkage record as negotiated provenance. They are not copied into `ScheduledCommitment` because the current agenda type has no authority to make those terms into travel, route, interaction, permission or tactical legality.

This prevents a statement such as “I can inspect it at the field office from 13:30 to 14:00” from becoming “the responder teleports there and may perform any needed mechanic.”

## Non-effects

Materialization does not:

- move either actor;
- reserve a world route;
- allocate tools, inventory or other resources;
- grant access or permissions;
- reinterpret `scope_ref` as an executable verb;
- choose an `alternative_ref` automatically;
- complete the assistance request;
- mutate relationships;
- enter AutoPTU immediately.

A later travel/resource/action owner must satisfy those requirements independently.

## AutoPTU boundary

The resulting scheduled commitment can set `requires_structured_mechanics`. That flag matters only when the ordinary agenda selects the due commitment. At that point the existing planner may emit `REQUEST_AUTOPTU`.

Pass 435 does not treat negotiated agreement as proof that a tactical action is implemented.

Capability posture remains:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized inspect/rescue/escort/protect/retrieve/carry/brace/extract still require explicit admission;
- AI tactical policy — BLOCKING for specialized objective policy;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

## Reduced encounter form

A complete reduced story can run as request -> counterproposal -> delivery -> requester acceptance -> scheduled appointment -> ordinary world-state inspection/report.

No battle is required. The appointment can be missed, superseded or completed through non-tactical evidence handling while preserving the accepted time and scope history.

## Full encounter form

The same accepted appointment can later become a hazardous inspection, retrieval, escort or containment scene. Travel, access, equipment and tactical legality must be established after commitment materialization by their own owners.

If rich mechanics are unavailable, the scene can keep the same premise by resolving environmental closure, evidence collection and withdrawal at world-simulation level instead of emulating missing PTU behavior in Minecraft.

## Persistence and replay

`OUROS_ASSISTANCE_COUNTERPROPOSAL_COMMITMENT_LEDGER_V1` stores the proposal ID, full action chain, accepted terms and requester-decision provenance. Exact replay is idempotent. Reusing a commitment ID with different content fails closed.

Checkpoint integration is still pending. Neither this ledger nor the underlying counterproposal ledger should be trusted across restart until they are incorporated into the coherent assistance checkpoint.

## Regression

`tests/test_global_npc_assistance_counterproposal_commitment.py` covers exact-window copying, responder ownership, provenance, term retention, no implicit movement/permission, delayed AutoPTU handoff, rejection, incomplete windows, elapsed windows, expiry/tamper failure, idempotent replay and snapshot fidelity.
