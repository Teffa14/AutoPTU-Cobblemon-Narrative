# Battle subject binding contract

Status: PROPOSED integration contract. Canon ecology and PTU authority boundaries remain unchanged.

## Purpose

Carry one stable Ouros ecological subject through a temporary battle conversation without exposing the persistent ecological key to AutoPTU, Minecraft, Cobblemon, Craftics or player-facing payloads.

## Binding record

`BATTLE_SUBJECT_BINDING_V1` contains:

- `battle_session_id`: opaque battle conversation identity.
- `battle_subject_ref`: opaque, session-scoped correlation reference.
- `ouros_subject_ref`: private stable ecological subject; never leaves the Ouros authority boundary.
- `lineage_proof_ref`: private proof that the subject is already persistent or was promoted from a counted source through Pass 258/259.
- `rules_profile_id`: selected PTU rules profile for the battle.
- `created_at_clock`: monotonic Ouros clock checkpoint.
- `binding_state`: `ACTIVE`, `FINALIZING`, `RETIRED`, or `QUARANTINED`.
- `provenance_root` and `transaction_id`.

## Admission invariants

A result can resolve to persistent ecological state only when `battle_session_id` and `battle_subject_ref` identify exactly one ACTIVE binding and the returned rules profile agrees with the handoff.

`battle_subject_ref` is not an actor ID. The same ecological subject can have different refs in different battle sessions. A ref cannot be moved between subjects or sessions.

Minecraft UUID, Cobblemon entity ID, species, nickname, sprite/model, coordinates, site recurrence, attack target, visible name or observational similarity cannot create or repair a binding.

A player-facing event cannot contain `ouros_subject_ref`, lineage proof, source slot, projection lease, internal transaction ID or private binding metadata.

## Counted unresolved sources

If the encounter candidate is still an `UNRESOLVED_POOL_SLOT` and the battle is allowed to have durable aftermath, Ouros must first establish admissible internal continuity and use the Pass 259 → Pass 258 promotion path. This changes representation only: anonymous source -1, persistent source +1, population total +0.

When continuity is insufficient, the encounter may still use a reduced mode in which presentation and non-durable battle playback occur, but persistent PTU-derived ecology cannot be attached to that anonymous source. The result is `STABLE_SUBJECT_REQUIRED_FOR_DURABLE_AFTERMATH`.

## Result resolution order

1. Validate semantic-result envelope schema and producer authority under Pass 262.
2. Validate `battle_session_id`.
3. Resolve the opaque `battle_subject_ref` in the private binding ledger.
4. Validate ACTIVE state, lineage and rules-profile agreement.
5. Apply Pass 263 capability admission for the exact `result_type` and producing path.
6. If admitted, invoke one explicit mapper to Ouros persistent state.
7. Record receipt/idempotency before transport acknowledgement.

A wrong-session reference returns `REJECT_SUBJECT_SESSION_MISMATCH`. A retired reference returns `REJECT_RETIRED_BATTLE_SUBJECT`. Multiple matches or missing lineage produce quarantine rather than guesswork.

## Restart and finalization

Active bindings and accepted ingress receipts must survive ordinary restart so late/retried results can be reconciled idempotently. Finalization retires the battle ref after all expected results are either accepted, rejected/quarantined with durable receipts, or explicitly abandoned by an authoritative recovery action.

Rollback detection follows the Pass 261 clock/epoch contract; clock rollback never silently reactivates a retired binding or expires an active one.

## Adapter boundary

Craftics/Minecraft may receive a presentation correlation token sufficient to render the correct combatant. That token is not accepted by the semantic ingress path as ecological identity. The adapter must return authoritative AutoPTU results through the battle-session channel rather than reverse-engineering consequences from animations/entities.

## Full and reduced encounter versions

Full version: a persistent ecological actor enters battle, receives an opaque session binding, AutoPTU resolves the encounter, typed results return, and only admitted result types become durable aftermath.

Reduced version: the same narrative encounter can run with presentation correlation and a completion receipt while all unverified durable result types remain quarantined. The story premise remains intact without making Minecraft reproduce missing PTU rules.
