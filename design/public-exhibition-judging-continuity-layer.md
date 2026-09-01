# Public Exhibition and Judging Continuity Layer

Status: DESIGN PROPOSAL. NOT CANON.
Date: 2026-09-01
Pass: 188

## Purpose

This layer models public demonstrations, exhibitions, judged events and Contest-adjacent activities as persistent world processes.

It does not create a replacement for PTU Contest mechanics. When an event invokes a real PTU Contest, Appeal Rolls, Contest Effects, Coordinator Features, move interactions and other mechanical rules remain authoritative source/engine responsibilities.

The layer owns event identity, schedule, entry records, published procedure, attributed observations, adjudication provenance, public presentation and later correction.

## Reuse before invention

Use existing repository systems wherever possible:

- server calendar/schedules own event timing;
- battle institutions own challenge contracts and audited battle formats;
- public memory owns later commemoration;
- archives own durable records and provenance;
- communications own notices and invitations;
- institutional authority owns delegation and approval;
- relationships own interpersonal consequences when separately justified;
- Minecraft projection owns visible boards, stages, signs and spectators only as presentation.

This layer does not add a new questline type. Existing `COMPETITIVE`, `SERVER_EVENT`, `SETTLEMENT`, `CHARACTER`, `RELATIONSHIP`, `CLASS`, `POKEMON`, `ITEM` and `SECONDARY` surfaces are sufficient.

## Core records

### public_exhibition_event

Suggested fields:

- `event_id`
- `event_kind`
- `host_institution_id`
- `venue_id`
- `scheduled_window`
- `status`
- `published_procedure_revision_id`
- `registration_policy_ref`
- `mechanical_ruleset_ref`
- `organizer_actor_ids`
- `evaluator_role_ids`
- `audience_access_policy_ref`
- `source_provenance`

Suggested `event_kind` values are descriptive, not exhaustive mechanics:

- `DEMONSTRATION`
- `EXHIBITION`
- `FORMAL_CONTEST`
- `AUDITED_BATTLE_EXHIBITION`
- `SKILL_PRESENTATION`
- `PUBLIC_REVIEW`

An event kind cannot imply a PTU ruleset. `FORMAL_CONTEST` must point to an approved mechanical ruleset before mechanical resolution is allowed.

### exhibition_entry

Suggested fields:

- `entry_id`
- `event_id`
- `participant_actor_ids`
- `pokemon_actor_ids`
- `submitted_at`
- `eligibility_status`
- `slot_or_order`
- `withdrawal_status`
- `mechanical_loadout_snapshot_ref` when legitimately required
- `notes`

Entry acceptance records participation authority only. It does not prove attendance, completion or placement.

### procedure_revision

Suggested fields:

- `procedure_revision_id`
- `event_id`
- `revision_number`
- `effective_from`
- `published_at`
- `issuer_role_id`
- `format_summary`
- `criteria_refs`
- `mechanical_ruleset_ref`
- `supersedes_revision_id`
- `reason_for_change`

If printed boards or handbills show an old revision, preserve that discrepancy as world evidence. Do not silently rewrite every projection.

### evaluation_criterion

This record is for institutional/social procedure only unless an approved PTU rule explicitly maps to it.

Suggested fields:

- `criterion_id`
- `event_id`
- `name`
- `description`
- `evidence_expected`
- `evaluator_role_id`
- `weight_or_precedence` if the institution explicitly uses one
- `mechanical_source_ref` if mechanically governed

Do not invent generic numerical scores merely to make a UI easy.

### performance_observation

Suggested fields:

- `observation_id`
- `event_id`
- `entry_id`
- `observer_actor_or_role_id`
- `observed_at`
- `observation_type`
- `statement`
- `source_context`
- `confidence` where appropriate

Possible observation types include audience response, procedural compliance, visible execution, equipment issue or interruption.

Observation is evidence, not verdict.

### adjudication_record

Suggested fields:

- `adjudication_id`
- `event_id`
- `entry_id`
- `decision_authority_role_id`
- `recorded_at`
- `basis_refs`
- `mechanical_result_ref` when an engine supplied the mechanical outcome
- `formal_result`
- `publication_status`
- `revision_id`

A mechanically governed result must preserve the engine/source result rather than reconstruct it from visual playback.

### audience_response_record

Suggested fields:

- `response_id`
- `event_id`
- `entry_id` when attributable
- `collection_method`
- `observed_at`
- `response_summary`
- `sample_scope`
- `provenance`

Crowd response can be qualitative. It should not automatically create a popularity stat.

### result_correction

Suggested fields:

- `correction_id`
- `target_record_id`
- `issued_at`
- `issuer_role_id`
- `reason`
- `prior_value_ref`
- `corrected_value`
- `evidence_refs`

Corrections preserve history. They do not erase that an earlier publication was visible.

## Event lifecycle

Recommended lifecycle:

`PROPOSED -> SCHEDULED -> REGISTRATION_OPEN -> REGISTRATION_CLOSED -> READY -> IN_PROGRESS -> ADJUDICATION_PENDING -> COMPLETE`

Additional legitimate states:

- `POSTPONED`
- `CANCELLED`
- `INTERRUPTED`
- `RESULT_UNDER_REVIEW`
- `CORRECTED`

A cancelled or interrupted event remains a real historical event record if people prepared, traveled, posted notices or attended.

## Mechanical authority boundary

### Nonmechanical public demonstration

Narrative/world systems may own:

- scheduling;
- attendance;
- ordinary equipment presence;
- presentation order;
- spoken/posted instructions;
- attributed observations;
- nonmechanical institutional review;
- archive/public display.

They may not grant PTU bonuses, Features, Contest Stats, Move effects or battle outcomes.

### PTU Contest

An actual PTU Contest must depend on exact source-backed mechanics, including all relevant:

- Appeal Rolls;
- Contest Types;
- Contest Effects;
- Contest Stats/conditions if applicable to the project source;
- turn/round procedure for the Contest;
- Coordinator Features;
- move-specific Contest behavior;
- any items or preparation rules actually authorized by the source set.

Until a dedicated engine implementation is audited, Narrative records the intent and leaves resolution blocked or externally authoritative. It must not approximate the result with battle AI or a generic narrative roll.

### Audited battle exhibition

If the public event is a battle, AutoPTU remains tactical authority. Narrative can provide the challenge contract and later consume only approved battle handoffs.

Formal placement, applause and social consequences remain separate from battle outcome unless the published event procedure explicitly maps the mechanical result to placement.

## Evaluation integrity

A valid adjudication should identify:

- which procedure revision governed the event;
- who had authority to evaluate;
- what evidence was considered;
- whether mechanical results came from AutoPTU/PTU Contest authority or world procedure;
- whether the result was provisional or final;
- whether later correction occurred.

Do not infer authority from proximity. A spectator standing beside the judging table is still a spectator unless a role assignment says otherwise.

## Conflict and recusal

A future institution may define conflict or recusal rules. This layer can store them, but does not invent a universal Ouros ethics code.

If a named evaluator cannot act, the event may:

- use an already-authorized substitute;
- postpone adjudication;
- proceed with fewer evaluators only if the governing procedure permits it;
- mark the result provisional.

A relationship with a participant cannot silently create or nullify authority.

## Audience and public memory

Audience response can persist through:

- witness statements;
- attendance counts where genuinely recorded;
- posted comments or notices;
- photographs;
- archive clippings;
- invitations to later events;
- ordinary NPC conversation memories.

Do not convert those signals into a hidden universal fame meter unless a future canon system explicitly defines one.

A public display is a projection of records. Destroying a Minecraft plaque or unloading the venue cannot delete the event record.

## Pokémon agency boundary

A Pokémon can participate, refuse an instruction where the broader simulation supports that behavior, become unavailable, or produce an observed performance.

Do not infer:

- consent to indefinite future performances;
- personality change from one outcome;
- humiliation from losing;
- pride from applause;
- a relationship change with the Trainer;
- learned Moves or Features from visual choreography.

Those require their own authoritative evidence.

## Persistent consequences

Useful consequences that do not require invented mechanics:

- a posted result remains visible for a period;
- Tideglass receives a dated copy;
- an incorrect caption is visibly corrected later;
- a scheduled slot becomes empty after withdrawal;
- a future invitation references a prior completed event;
- an event format is revised after an operational problem;
- spectators remember having attended;
- a venue changes ordinary dressing after the event;
- an exhibitor becomes busy preparing for a later date through normal schedule state.

## Minecraft/Cobblemon projection

Safe projections include:

- registration desk;
- stage/court markers;
- result board;
- dated posters;
- spectator NPCs;
- participant queue positions;
- photographs or trophy/display objects;
- ordinary animations and particles clearly treated as presentation.

Hard boundaries:

- particles cannot produce Appeal Points;
- animation timing cannot decide PTU success;
- a scoreboard block cannot author the authoritative result;
- NPC despawn cannot withdraw an entry;
- client-side applause cannot grant relationship state;
- Cobblemon battle state cannot replace AutoPTU authority;
- visual Contest choreography cannot stand in for an unimplemented PTU Contest resolver.

## Design test

Before shipping any public exhibition, answer:

1. What kind of event is this?
2. Which existing institution hosts it?
3. What procedure revision governs it?
4. Is it mechanically a PTU Contest, a battle, or a nonmechanical demonstration?
5. Which system owns the result?
6. What can spectators observe without becoming judges?
7. What records persist afterward?
8. Can a correction occur without deleting history?
9. What changes in the world beyond a single reward screen?
10. Which engine capability families are exact dependencies?

If these answers are unclear, the event is not implementation-ready.