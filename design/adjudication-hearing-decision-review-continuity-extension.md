# Adjudication, Hearing, Decision & Review Continuity Extension

Status: PROPOSED ARCHITECTURE. Non-canon until reviewed. This layer defines continuity semantics for canon-approved institutions that make formal or semi-formal decisions. It does not create courts, legal rights, offenses, penalties or universal appeal systems.

Date: 2026-08-30

## Purpose

Ouros needs to preserve what happens after a matter is submitted to an institution without collapsing investigation, evidence, institutional authority, hearing procedure, decision, later review and implementation into one status flag.

The layer is designed for many possible settings: battle-league protests, contest decisions, conservation access, civic allocation, guild recognition, club eligibility, route-service disputes, permit-like approvals, archive access, disciplinary review or other institution-specific processes. A use becomes valid only when the governing institution exists in canon and defines the procedure it actually supports.

## Ownership boundary

Case/Authority owns investigations, allegations, evidence, authority scope and custody.

Agreements/Mediation owns negotiated agreement and consensual repair.

Civic Governance and Civic Office own institutions, public mandates and office continuity.

Credentials owns credentials and authorization state.

Battle Institutions owns challenge contracts and formal battle history.

Organization Lineage owns institutional identity through rename, branch, split, merger, dissolution and succession.

This extension owns only the lifecycle of a submitted matter and the decision events produced by the responsible institution.

## Core records

### `decision_matter`

Suggested fields:

- `decision_matter_id`
- `institution_ref`
- `institution_identity_version_ref`
- `matter_type`
- `subject_refs[]`
- `related_case_refs[]`
- `related_agreement_refs[]`
- `related_credential_refs[]`
- `related_battle_event_refs[]`
- `opened_at`
- `closed_at?`
- `current_procedural_state`
- `public_visibility`
- `canon_status`

The record does not contain a free-floating truth verdict. Any factual findings must point to the evidence or authoritative event that supports them.

### `decision_process_event`

Suggested event types:

- `REFERRED`
- `FILED`
- `RECEIVED`
- `RETURNED_FOR_CLARIFICATION`
- `ACCEPTED_FOR_DECISION`
- `DECLINED`
- `NOTICE_CREATED`
- `NOTICE_SENT`
- `NOTICE_RECEIPT_RECORDED`
- `RECORD_REQUESTED`
- `RECORD_RECEIVED`
- `HEARING_SCHEDULED`
- `HEARING_RESCHEDULED`
- `HEARING_CANCELLED`
- `HEARING_OPENED`
- `HEARING_CLOSED`
- `RECORD_CLOSED`
- `DECISION_ISSUED`
- `DECISION_EFFECTIVE`
- `IMPLEMENTATION_STARTED`
- `IMPLEMENTATION_COMPLETED`
- `REVIEW_REQUESTED`
- `REVIEW_PERMISSION_GRANTED`
- `REVIEW_PERMISSION_REFUSED`
- `REVIEW_OPENED`
- `STAY_ISSUED`
- `STAY_LIFTED`
- `DECISION_AFFIRMED`
- `DECISION_AMENDED`
- `DECISION_REVERSED`
- `MATTER_REMANDED`
- `SUPERSEDING_DECISION_ISSUED`
- `MATTER_CLOSED`
- `MATTER_REOPENED`

Not every institution supports every event. Its canon procedure defines the permitted subset.

### `institutional_decision`

Suggested fields:

- `decision_id`
- `decision_matter_id`
- `issuing_body_ref`
- `issuing_actor_refs[]`
- `issued_at`
- `effective_at?`
- `decision_kind`
- `scope`
- `disposition`
- `finding_refs[]`
- `reason_record_ref?`
- `source_record_refs[]`
- `supersedes_decision_id?`
- `superseded_by_decision_id?`
- `implementation_requirement_refs[]`
- `review_state`
- `public_visibility`

A decision may contain an institution's finding. That finding remains a historical institutional fact and must not silently overwrite canonical truth, evidence history or private knowledge.

### `decision_review`

Suggested fields:

- `review_id`
- `original_decision_id`
- `reviewing_body_ref`
- `requested_at`
- `accepted_at?`
- `review_scope`
- `review_basis_refs[]`
- `stay_state`
- `record_refs[]`
- `hearing_ref?`
- `result`
- `result_decision_id?`
- `closed_at?`

Possible results are institution-specific. Generic continuity values may include `NO_REVIEW`, `PERMISSION_REFUSED`, `AFFIRMED`, `AMENDED`, `REVERSED`, `REMANDED`, `SUPERSEDED`, `WITHDRAWN`, `ACCEPTED_AMBIGUITY`.

### `decision_implementation`

Suggested fields:

- `implementation_id`
- `decision_id`
- `responsible_actor_or_org_ref`
- `required_world_change_refs[]`
- `started_at?`
- `completed_at?`
- `verification_refs[]`
- `status`

The world changes only through the subsystem that owns each consequence. A decision requiring a credential update asks Credentials to change that state. A facility restriction asks the relevant facility/service owner. A competition advancement consumes an authoritative battle or event record. The decision record itself does not directly mutate every subsystem.

## Required semantic separations

`MATTER_FILED != MATTER_ACCEPTED_FOR_DECISION`

`MATTER_ACCEPTED != JURISDICTION_OR_SCOPE_PROVEN_UNIVERSALLY`

`NOTICE_SENT != NOTICE_RECEIVED`

`HEARING_SCHEDULED != HEARING_HELD`

`HEARING_HELD != DECISION_ISSUED`

`NO_HEARING != NO_VALID_PROCESS` when the governing institution supports record-only decisions.

`DECISION_ISSUED != DECISION_EFFECTIVE`

`DECISION_EFFECTIVE != IMPLEMENTATION_COMPLETE`

`INSTITUTIONAL_FINDING != CANONICAL_TRUTH`

`REVIEW_REQUESTED != REVIEW_ACCEPTED`

`REVIEW_ACCEPTED != DECISION_STAYED`

`DECISION_STAYED != DECISION_REVERSED`

`REMANDED != ORIGINAL_DECISION_AUTOMATICALLY_REVERSED` unless the governing procedure says so.

`AMENDED != ORIGINAL_RECORD_DELETED`

`SUPERSEDED != HISTORICALLY_ERASED`

`MATTER_CLOSED != ALL_DOWNSTREAM_CONSEQUENCES_COMPLETE`

`PUBLIC_DISAGREEMENT != PROCEDURAL_INVALIDITY`

## Findings and truth

An institutional body may legitimately record `FINDING_SUPPORTED`, `FINDING_NOT_SUPPORTED`, `ELIGIBLE`, `INELIGIBLE`, `RESULT_CONFIRMED`, `RESULT_CHANGED`, `ACCESS_GRANTED` or another canon-approved disposition.

Ouros should preserve at least three separate layers:

1. the actual underlying world fact, where known by the simulation;
2. the evidence and record available to the institution at decision time;
3. what the institution decided based on its procedure.

This supports honest mistakes, incomplete records, later discoveries, differing competent interpretations and historical controversy without making every official decision secretly corrupt or every disagreement evidence of conspiracy.

## Notice and absence

Notice is an event chain. A created notice may fail to send. A sent message may fail delivery. A delivered notice may not be read. The communication layer owns delivery evidence.

Absence from a hearing does not by itself prove anything about notice, guilt, legitimacy or intent. The governing institution decides what procedural consequence, if any, follows.

## Review and supersession

A review should point to the exact decision under examination. Later decisions should preserve predecessor links rather than editing the original record in place.

A remand returns a defined issue or matter for further work. It does not itself tell Ouros what the new answer will be.

A superseding decision becomes the current recognized decision for its scope while the previous one remains visible as history subject to privacy rules.

## Institutional memory

Decision archives can create public memory, professional practice and rumors. A historical decision may be cited by an NPC, discussed by media, taught in a guild or remembered incorrectly by a community. None of those derivative states automatically modify the governing procedure.

## Battle integration boundary

Battle may provide an authoritative event input when the matter concerns an actual sanctioned match. AutoPTU decides the combat result. The institution may consume that result according to its rules.

Combat must never directly author:

- whether a filing is accepted;
- whether notice was valid;
- whether a hearing occurred;
- institutional findings outside the battle result;
- review permission;
- affirmation, amendment, reversal or remand;
- credential suspension or restoration;
- organizational authority;
- archive custody;
- compensation;
- guilt, liability or legal status;
- implementation completion outside a narrow battle-caused physical state.

## Minecraft/Cobblemon/Craftics boundary

The adapter may render already-decided facts: hearing rooms, queues, posted schedules, public decision boards, sealed archive rooms, badges, permits, NPC attendance, old notices, changed signage or physical consequences.

It cannot infer procedural state from NPC position, scoreboard team, entity despawn, inventory, block state, nametag, chat message, combat victory or Cobblemon BattleState. AutoPTU/Ouros remains authoritative for combatants and tactical facts; Ouros systems remain authoritative for institutional state.

## Compression rules

Routine uncontested processes should compress. A player does not need to manually attend every administrative step.

Expand a process when at least one meaningful choice exists: evidence is missing, the institution's scope is disputed, a key actor cannot attend, public pressure matters, implementation conflicts with another world system, review introduces new evidence, a record has ambiguous provenance or a decision changes access to future play.

## Canon gate

Before any concrete Ouros institution uses this layer, canon review must specify:

- institution identity and mandate;
- matters it may decide;
- who may submit or participate;
- available process modes;
- notice expectations;
- what records it may consider;
- possible decision types;
- whether review exists and by whom;
- when decisions become effective;
- which subsystem implements consequences;
- public/private record rules.

Anything absent remains UNKNOWN rather than filled by real-world assumptions.