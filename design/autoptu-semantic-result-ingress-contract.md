# AutoPTU semantic-result ingress contract

Status: PROPOSED DESIGN CONTRACT. Does not change established species canon or PTU rules.

## Purpose

Pass 260 proves that Minecraft presentation cannot author PTU consequences. Pass 261 requires a typed authoritative result before battle-authored state can enter ecological retention. This contract defines the minimum fail-closed ingress boundary between AutoPTU adjudication and Ouros persistent ecology.

## Authority boundary

AutoPTU owns semantic battle results for the adopted PTU rules path.

Ouros owns persistent ecological population, actor lineage, retention and public-knowledge records.

Minecraft/Cobblemon/Craftics owns world presentation and playback. Presentation events may be retained as observations but cannot author HP, Injury, status, Move, Ability, item, ownership, capture or battle truth.

The ingress adapter may transport an AutoPTU result. It cannot reinterpret or upgrade that result.

## Envelope

A proposed `OUROS_AUTOPTU_SEMANTIC_RESULT_V1` contains at minimum:

`schema_version`

`result_id`

`result_type`

`producer_id`

`producer_revision`

`rules_profile_id`

`battle_session_id`

`causation_id`

`correlation_id`

`subject_binding`

`semantic_payload`

`capability_provenance`

`occurred_at`

`imported_at`

`provenance_root`

`replay_policy`

`public_payload = NONE` unless another contract explicitly exposes a derived observation

`population_effect = NONE` unless a separately authorized ecology/demography transaction exists

The envelope pattern is inspired by event-identity and provenance standards, but this contract does not claim CloudEvents or W3C PROV conformance.

## Result identity and replay

`producer_id + result_id` identifies one semantic result.

The first valid import commits an immutable ingress receipt.

Replaying the same producer/result identity with byte-equivalent semantic identity is `IDEMPOTENT_NO_OP`.

Reusing the same identity with a conflicting payload, subject, rules profile or provenance is `REJECT_CONFLICTING_REPLAY`.

Transport retry never creates a second Injury, status transition, retained consequence or ecology transaction.

## Producer authority

The accepted producer must belong to an explicitly configured AutoPTU authority profile.

Required checks include producer identity, compatible producer revision, adopted rules profile and expected battle session lineage.

Pass 262 does not define cryptographic signing. If production transport later requires signatures, tokens, process identity or authenticated IPC, that becomes an adapter/security contract. Absence of such a verified mechanism must not be papered over by a `signed: true` fixture field.

## Subject binding

The subject is bound using the stable Ouros source/actor reference that was handed into the authoritative battle session.

A Minecraft UUID, Cobblemon entity UUID, display name, species, coordinates or visual similarity is never sufficient subject identity.

Ingress requires that the battle-session handoff ledger proves:

`battle subject binding -> same active/retired Ouros lineage expected by result`

If the binding cannot be proven, outcome is `QUARANTINE_SUBJECT_LINEAGE_UNRESOLVED`.

Quarantined results cannot mutate aggregate population state or another candidate individual.

## Typed semantic payload

Every `result_type` has its own schema and allowed Ouros mappings.

Example proposed type:

`PTU_INJURY_APPLIED`

Minimum semantic payload candidate:

`injury_event_id`

`injury_delta`

`post_result_injury_count` when the authoritative engine exposes it

`owning_battle_transition_ref`

The importer never calculates the Injury from raw damage, HP, animation or Minecraft state. It only consumes the already-adjudicated semantic result.

A future status result must use a separate status schema. A future battle-end result must use its own schema. Unknown types return `REJECT_UNKNOWN_RESULT_TYPE`.

## Capability provenance gate

Each result type declares the capability families its authoritative production path depends on.

The envelope records the exact families used by the producing path and a reference to the tested engine contract/revision that supports them. Ouros compares this with the current engine-readiness policy.

Pass 262 does not promote a family because an envelope names it.

A persistent Injury import requires at minimum the full stateful damage pipeline to be verified for the exact producing path, plus full turn/round lifecycle and any move-specific behavior, status, Ability, item, Trainer Feature, terrain/reaction or movement family actually involved in producing that result.

If the required path is not currently admitted for production persistence, result outcome is `QUARANTINE_CAPABILITY_PATH_UNVERIFIED`. The original result/provenance can remain auditable, but no persistent PTU consequence is committed into Ouros.

## Ingress transaction

The ordered validation pipeline is:

1. Validate envelope/schema version.
2. Validate producer authority and rules profile.
3. Validate result identity/replay semantics.
4. Validate battle-session provenance.
5. Resolve stable Ouros subject lineage.
6. Validate result-type payload.
7. Validate exact capability provenance against current admission policy.
8. Commit immutable ingress receipt.
9. Invoke only the explicitly registered Ouros consequence mapper.
10. Record the resulting retained/ecological transaction separately.

No later validation failure may leave a partial state mutation.

## Result states

`ACCEPTED_COMMITTED`

`IDEMPOTENT_NO_OP`

`REJECT_SCHEMA`

`REJECT_PRODUCER_AUTHORITY`

`REJECT_RULES_PROFILE`

`REJECT_CONFLICTING_REPLAY`

`REJECT_UNKNOWN_RESULT_TYPE`

`REJECT_PAYLOAD`

`QUARANTINE_SUBJECT_LINEAGE_UNRESOLVED`

`QUARANTINE_CAPABILITY_PATH_UNVERIFIED`

Quarantine is internal. It cannot become player-visible certainty or an aggregate ecological effect.

## Interaction with retention and semantic horizons

An accepted result can open or close only a registered semantic state/horizon whose mapping explicitly names that result type.

For example, an accepted future `PTU_INJURY_APPLIED` may open an `AUTHORITATIVE_ONE_TIME_TRANSITION` record and any separately adopted healing/recovery horizon. The horizon layer cannot change the original adjudication.

A rejected or quarantined result cannot create retained PTU state.

## Marea/Sendero fixture policy

Pass 262 uses the existing population total of twelve Fletchling and fixture-only source/result identifiers.

The fixture includes:

- one synthetically prevalidated AutoPTU semantic result that demonstrates the accepted ingress shape without asserting the current Java damage family is production-complete;
- a replay of that same result that becomes an idempotent no-op;
- a conflicting replay that is rejected;
- a Minecraft-only damage signal that is rejected as PTU authority;
- a result whose subject binding does not match the battle handoff and is quarantined;
- a status-shaped result whose capability path is currently unverified and is quarantined;
- restart with the accepted ingress receipt restored exactly once.

All consequence payloads are NON_CANON fixtures. No Fletchling acquires a canon Injury or status.

## Engine capability boundary

The reduced fixture tests only ingress bookkeeping. It uses no tactical AutoPTU mechanics and makes no claim that the synthetic result was produced by the live engine. Production transport/presentation depends on Minecraft/Cobblemon/Craftics adapter/playback support.

The full persistent-Injury version depends on full turn/round lifecycle and the full stateful damage pipeline, plus every additional family actually exercised by the producing battle path. Current readiness remains insufficient for a blanket Injury-import claim.

A persistent status additionally depends on status lifecycle. A Move-specific consequence adds move-specific behavior. Ability-, item-, Trainer Feature- or terrain/reaction-authored consequences add those exact families. Autonomous battle choice adds AI tactical policy.

## Open questions

- Concrete production transport and authentication boundary between AutoPTU and Ouros.
- Stable battle-session subject-binding format shared by Java and the Minecraft/Craftics adapter.
- Exact rules-profile/revision identifiers and compatibility policy.
- Which semantic result types AutoPTU-Java currently emits directly versus which require a future event/result API.
- Per-result capability admission matrix tied to verified tests/contracts rather than broad family labels.
- Persistence store for ingress receipts and quarantined records.
