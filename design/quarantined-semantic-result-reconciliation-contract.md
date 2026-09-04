# Quarantined semantic-result reconciliation contract

Status: PROPOSED integration contract. No canon or PTU rules change.

## Purpose

Define what happens after Pass 262/263 retains a semantic result because subject lineage, rules-profile compatibility or exact capability admission is insufficient for persistent Ouros mutation.

The contract prevents three failure modes: silently dropping a potentially valid authoritative result, repeatedly retrying until a result accidentally passes, and using player/Minecraft observations to manufacture the missing PTU authority.

## Core invariant

A quarantine record stores an immutable semantic-result receipt plus a changing review state.

The original `OUROS_AUTOPTU_SEMANTIC_RESULT_V1` envelope is never edited to repair admission.

Reconciliation can change disposition only because independently versioned evidence changed.

## `SEMANTIC_RESULT_QUARANTINE_V1`

Minimum private record:

- `producer_id`
- `result_id`
- `result_type`
- immutable envelope hash/ref
- `battle_session_id`
- `battle_subject_ref`
- preserved private lineage-proof ref when available
- `rules_profile_id`
- `producer_revision`
- `original_quarantine_reason`
- `current_quarantine_reason`
- `required_capabilities[]`
- `original_admission_evidence_refs[]`
- `current_review_evidence_refs[]`
- `review_generation`
- `quarantine_state`
- `created_at_clock`
- `last_reviewed_at_clock`
- `provenance_root`

The record is internal. Player payloads cannot expose result IDs, subject refs, lineage refs, engine test names, capability gates or private review metadata.

## Lifecycle

Initial semantic ingress may create `QUARANTINED_OPEN` for an otherwise valid envelope that cannot currently mutate persistent state.

A transport retry with the same semantic identity remains `REVIEW_BLOCKED_NO_CHANGE`. Retry count, server restart, chunk reload, elapsed world ticks, new Minecraft entity UUID or repeated playback are not review evidence.

A record becomes `RECONCILIATION_ELIGIBLE` only when at least one relevant external evidence generation changes. Allowed candidate triggers are:

- a new exact `SEMANTIC_RESULT_ADMISSION_V1` matching the same result type, producer revision, rules profile and producing path;
- a previously unresolved stable subject lineage becoming provable through the existing Pass 258/259 path without changing the original battle subject;
- an explicit compatibility decision for the exact rules profile/revision;
- an operator/audit decision that resolves an irreparable schema/provenance problem to rejection/archive, never to mechanical admission.

Reconciliation enters `RECONCILING`, re-runs all current gates against the immutable original envelope and produces one atomic outcome.

Successful admission becomes `ADMITTED_COMMITTED` and invokes exactly one registered consequence mapper. Failure returns to `QUARANTINED_OPEN` with a new reason snapshot, or becomes `PERMANENTLY_REJECTED` / `ARCHIVED_UNRESOLVED` when policy says the record can never be admitted.

## Evidence generations

Every review stores the admission-policy generation and lineage-policy generation it evaluated.

If those generations are unchanged, a new review request is an idempotent no-op.

A broad family promotion is not sufficient by itself. Capability admission still uses Pass 263's exact tuple:

`result_type + producer_revision + rules_profile + producing_path + required_capabilities + exact_contract_tests`

A representative mechanic elsewhere cannot release the quarantine.

## Subject reconciliation

A subject-lineage quarantine can be repaired only if the preserved battle binding proves that the original `battle_subject_ref` refers to the stable Ouros subject now being resolved.

Species, site, nickname, model, Minecraft/Cobblemon UUID, observation similarity and player testimony remain inadmissible identity repairs.

A retired battle binding may still provide immutable historical correlation if the binding ledger preserved it at finalization. Reconciliation does not reactivate combat or create a new battle session.

If the original anonymous source never obtains admissible lineage, a durable mechanical consequence cannot be assigned to another member of the population. The record remains quarantined or is archived unresolved.

## Capability reconciliation

A result quarantined for an unverified capability path may be admitted later only when an exact admission record covers the producing path represented in the original immutable result.

Upgrading AutoPTU-Java globally does not retroactively validate historical results from an older producer revision unless compatibility/admission explicitly includes that revision and path.

A fixture-only admission never releases production quarantine.

## Knowledge and observation boundary

Player and NPC field observations may continue during quarantine. Examples include visible guarding, altered site use, reduced movement, resting, unusual feeding or an apparent limp.

These observations belong to the knowledge pipeline. They can raise or lower confidence in a narrative interpretation and can produce field-research quests.

They cannot satisfy a missing stateful damage pipeline, status lifecycle, Move behavior, Ability, item, Trainer Feature, terrain/reaction or tactical-policy gate.

The UI may say that an observed individual appears impaired if the observation contract supports that wording. It cannot expose “1 Injury” unless an admitted authoritative result and a presentation policy explicitly permit it.

## Replay and mutation safety

`producer_id + result_id` remains the semantic identity established in Pass 262.

If a quarantined result is later admitted, its receipt identity is reused. No replacement result is fabricated.

The consequence mapper records the quarantine receipt/reconciliation transaction as its provenance parent. Replaying the original result after admission produces `IDEMPOTENT_NO_OP`.

A conflicting replay remains `REJECT_CONFLICTING_REPLAY` and cannot reopen review.

No review failure may leave HP, Injury, status, population, ownership or other partial mutations.

## Restart and rollback

Quarantine state survives restart.

Pass 261 clock rollback detection applies. Rollback never releases, rejects, expires or reopens a quarantine automatically.

Quarantine retention is audit retention, not an ecological semantic horizon. Archive policy must be explicit and may retain the immutable receipt even after active review ends.

## Marea/Sendero reduced fixture

Pass 264 uses the canon Fletchling population total of twelve and the existing persistent Fletchling subject. All battle/result IDs are fixture-only.

The reduced trace demonstrates:

- an Injury-shaped result starts quarantined because the exact producing path is not admitted;
- identical retry does not change the disposition;
- a player observation of apparent limping adds knowledge only;
- a broad engine family label change without an exact admission record cannot release the result;
- an exact fixture-only admission generation can make the synthetic record reconciliation-eligible for contract testing while explicitly claiming no production readiness;
- one atomic fixture-only mapper application occurs;
- replay after reconciliation remains idempotent;
- a separate status-shaped record remains quarantined because status lifecycle is still partial;
- restart restores both committed reconciliation provenance and unresolved quarantine exactly once.

No canon Injury/status is created.

## Full encounter version

A future production aftermath version requires an actual AutoPTU-Java public semantic-result export, an authenticated/verified transport boundary as selected by the project, stable subject binding, and exact admission records tied to Java tests/contracts.

A real persistent Injury requires the full stateful damage pipeline and full turn/round lifecycle for the exact producer path, plus every materially participating capability family.

A persistent status adds status lifecycle. Move-, Ability-, item-, Trainer Feature-, terrain/reaction- or forced-movement-authored results add those exact families. Autonomous tactical causation adds AI tactical policy.

## Open questions

- Persistent storage/index and operational review tooling for quarantine records.
- Exact Java semantic-result export/API and producer path IDs.
- How admission-evidence generation changes are published to Ouros.
- Archive/retention policy for records whose producing engine revision can never be certified.
- Player-facing language for observed aftermath when mechanical truth remains unresolved.
