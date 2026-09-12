# Global NPC Assistance Renegotiation Proposal Contract — Pass 445

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Permit the original responder to author concrete replacement terms only after the requester explicitly accepted reopening and that acceptance actually reached the responder through the ordinary information network.

Owner

`OUROS_ASSISTANCE_RENEGOTIATION_PROPOSAL_LEDGER_V1` owns replacement-offer records. It does not own the old negotiated commitment, communication transport, acceptance of the new offer, scheduling, travel, access, resources, relationships or PTU resolution.

Required causal chain

A negotiated assistance commitment exists. Its responder requested renegotiation. The requester received that request and recorded `ACCEPT_RENEGOTIATION_REQUEST`. Pass 444 carried that answer back through `InformationEventQueue`. Only after the reply event reaches terminal `DELIVERED` and the responder has the matching REPORT claim may replacement terms be authored.

A requester decision stored in a ledger is insufficient by itself. A queued, failed or otherwise undelivered reply cannot authorize replacement terms.

Lineage

Every replacement proposal stores the old commitment id, old proposal id, requester decision id, decision-reply event id and decision provenance root. The new proposal begins a new provenance root at its own `proposal_id` because formulating replacement terms is a new responder-authored act.

The decision lineage remains preserved separately so later systems can establish why the responder was authorized to reopen terms.

Term rules

A replacement proposal has a complete start and end minute, optional location/scope/alternative references, optional expiry, and an authoring semantic minute. The proposed start cannot be in the past relative to authoring. The offer must differ from the accepted terms in at least one tracked term.

The old commitment remains unchanged while the new offer exists. The new offer has no scheduling force until a later explicit acceptance path creates a replacement obligation.

Explicit non-effects

Creating replacement terms does not cancel, rewrite, satisfy or mark missed the old commitment. It does not create a new `ScheduledCommitment`, reserve a route, grant a permission, allocate a resource, move either actor, send the new offer, change trust/reputation, infer blame, or invoke AutoPTU.

The proposal must later travel through explicit communication and receive its own decision. That future cycle may create a new commitment only after concrete terms are received and accepted.

Failure posture

Actor mismatches, rejection decisions, absent delivery, missing responder knowledge, tampered payload/provenance, past-dated replacement windows, identical fake replacements and identity collisions fail closed.

AutoPTU boundary

Pass 445 is non-tactical. If accepted replacement terms later lead to travel, inspection, escort, retrieval, protection, containment or extraction, those actions remain subject to world-state owners, legal-action admission and `REQUEST_AUTOPTU` where structured mechanics are required.

Open seam

The new offer still needs an explicit responder-to-requester dispatch path. Delivery must remain separate from acceptance. A later acceptance owner can then decide whether and how to create a replacement commitment while preserving the superseded promise as historical fact.