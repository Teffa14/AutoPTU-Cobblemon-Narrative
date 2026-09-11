# Global NPC world action intent contract — Pass 422

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

A successful information delivery may cause one named world agent to replan. The selected agenda decision still must not be treated as a completed world action.

This contract introduces a durable boundary between those two facts.

Implemented owner

`tools/global_npc_world_action_intent.py`

Schema

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1`

A `WorldActionIntentRecord` preserves:

- one durable `action_id`;
- the deciding `agent_id`;
- the selected `intent_id` and `intent_kind`;
- the selected target reference, if any;
- the semantic minute at which the action intent was recorded;
- the exact replan trigger IDs that caused reconsideration;
- the coordinator reason codes;
- the agenda source type and source reference;
- `status: PLANNED`.

Permanent boundary

`PLANNED` means that one actor selected an ordinary world action. It does not mean that the action started, succeeded, reached its target, changed another person's agenda, delivered a message, created an obligation or resolved a PTU mechanic.

A request for assistance therefore records only the requester's selected intention. The requested specialist remains an independent world agent. Any effect on that specialist requires a later communication/delivery event and then the specialist's own eligibility/replanning path.

AutoPTU ownership

A decision whose handoff is not `NONE` cannot enter this ledger. `REQUEST_AUTOPTU` and an existing AutoPTU binding use their own ownership contracts. Pass 422 does not reinterpret tactical handoff as an ordinary world action.

Validation and replay

The action owner requires:

- a non-empty action ID;
- a non-negative semantic minute;
- at least one causal replan trigger;
- matching outer and inner agent identity;
- a selected intent ID;
- ordinary world ownership (`Handoff.NONE`);
- an action-bearing decision rather than idle/no-eligible/hold state.

An exact replay of the same action ID and content is idempotent. Reusing the action ID for different content fails closed.

Snapshot/restore

The V1 ledger snapshot is deterministic and carries the same causal fields. Unknown schemas, malformed rows and conflicting duplicate action IDs fail closed.

Pass 422 does not yet connect this ledger to the global persistent-world checkpoint family. That remains a follow-up integration step.

Narrative consequence

This boundary supports stories where a warning changes one person's plan without silently commanding someone else. A coordinator may decide to ask a technician for help, but the technician can still be unavailable, refuse, accept later, request clarification or prioritize another obligation after the request actually reaches them.

Regression

`tests/test_global_npc_world_action_intent.py` covers ordinary recording, explicit target preservation, exact replay, conflicting replay, AutoPTU rejection, idle rejection, missing trigger rejection, agent identity mismatch and snapshot round-trip.
