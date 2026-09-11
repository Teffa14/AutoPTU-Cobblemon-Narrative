# Global NPC Assistance Counterproposal Terms Contract — Pass 432

Status: ACTIVE IMPLEMENTATION CONTRACT
Date: 2026-09-11

## Purpose

Pass 425 made `COUNTERPROPOSE_ASSISTANCE_REQUEST` a durable responder-owned world action. Passes 426–427 made the response deliverable and able to wake the original requester. The missing boundary was the content of the counterproposal itself.

A counterproposal must be able to say something concrete such as:

- a different time window;
- a different meeting/work location;
- a narrower or changed scope;
- a different suggested course or helper.

`COUNTERPROPOSE != ACCEPT`

Recording those terms does not create a commitment, reserve time, schedule travel, allocate equipment, change a relationship, complete a quest or execute PTU mechanics.

## Executable owner

`tools/global_npc_assistance_counterproposal.py`

Schema:

`OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1`

The durable record binds:

- proposal identity;
- original request action;
- responder-owned counterproposal action;
- requester and responder identities;
- optional proposed start/end;
- optional location reference;
- optional scope reference;
- optional alternative reference;
- optional offer expiry;
- `response_action_id` as provenance root.

At least one concrete term must exist. A bare `COUNTERPROPOSE_ASSISTANCE_REQUEST` with no terms cannot enter this ledger.

## Validation boundary

The original action must remain a `PLANNED REQUEST_ASSISTANCE` with another explicit recipient.

The response must remain a `PLANNED COUNTERPROPOSE_ASSISTANCE_REQUEST` authored by that recipient and targeted back to the requester.

The response must retain the request-delivery replan trigger. A caller cannot attach terms to an unrelated response after the fact.

A proposed end requires a proposed start and may not precede it. A proposed start may not already be in the past at authoring time. An expiry may not already have elapsed when the proposal is authored.

Blank structured references fail closed.

## Persistence and replay

Identical replay of a proposal ID is idempotent. Reusing that ID with different terms fails closed.

Snapshot/restore preserves the exact structured terms and the response action provenance. It does not infer terms from dialogue text or regenerate them from planner output.

## Communication boundary

Pass 432 records terms. It does not yet put those terms into the response envelope.

Existing response dispatch still communicates that a `COUNTERPROPOSE_ASSISTANCE_REQUEST` occurred. A later slice must bind the delivered counterproposal to the structured proposal record so the requester can learn the actual terms without reading global state omnisciently.

Until that seam exists:

`DURABLE_TERMS != REQUESTER_KNOWS_TERMS`

## Worldbuilding use

This supports offers such as:

- “I cannot inspect the crossing now, but I can inspect the instruments at the repair row later.”
- “I cannot escort the whole route, but I can cover the upper junction.”
- “I cannot come personally; ask another qualified actor for a remote evidence check.”

The examples describe structure only. They do not canonize a new incident, obligation, relationship or outcome.

## PTU / Kairos boundary

The project source index remains a routing aid, not a mechanics grant. A counterproposal can describe future work without proving the engine can resolve that work.

If accepted work later requires structured battle resolution, capability admission remains exact and local to the encounter.

Current live evidence posture at this pass:

- targeting / footprints / range / LoS — VERIFIED only inside audited scopes;
- base movement legality — VERIFIED only inside audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only inside audited scopes;
- action economy / initiative — PARTIAL. AutoPTU-Java head `2f72abe6c0e2b58533856484a1cc954f9e6648e8` now wires replacement-initiative insertion into the production switch-entry dispatcher with caller policy, but this does not verify the whole family;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features / perks — individually gated;
- AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized objective actions still require explicit admission;
- AI tactical policy — BLOCKING for specialized rescue/escort/protect/retrieve/extract policies;
- Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

AutoPTU Python remains read-only at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its head is presentation-only and does not change battle rules or outcomes.

## Full and reduced encounter versions

Full version:
A responder proposes a changed time, location or scope for a potentially tactical assistance job. If the requester later accepts and the job reaches structured mechanics, only admitted AutoPTU capabilities may resolve it. Knockback, reactions, dynamic hazards, delayed effects, complex statuses, ability-triggered terrain and Trainer Feature interrupts each remain dependent on their exact capability families.

Reduced version:
The same narrative premise runs entirely in world simulation. The responder proposes a future inspection, meeting, observation or bounded service. The requester can later accept, reject or continue negotiating. No battle is required.

## Next seams

1. Carry structured counterproposal terms through explicit communication to the requester without global-state leakage.
2. Give requester acceptance of a counterproposal its own durable action and commitment owner.
3. Add the counterproposal ledger to a coherent assistance/world checkpoint before relying on restart persistence.
4. Keep route reservation and resource allocation under their existing owners rather than embedding them into negotiation records.
