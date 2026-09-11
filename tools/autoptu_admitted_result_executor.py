from __future__ import annotations

from dataclasses import dataclass

from tools.autoptu_engine_authority_transition_plan import (
    AutoPTUAuthorityTransitionIntent,
    AutoPTUAuthorityTransitionKind,
)
from tools.autoptu_session_identity import AutoPTUSessionLedger, AutoPTUSessionState


@dataclass(frozen=True)
class AutoPTUAdmittedResultExecution:
    session_id: str
    result_ref: str
    changed: bool
    state: AutoPTUSessionState


def execute_admitted_result_recording(
    ledger: AutoPTUSessionLedger,
    intent: AutoPTUAuthorityTransitionIntent,
) -> AutoPTUAdmittedResultExecution:
    """Record exactly one result that already crossed the admission boundary.

    The executor accepts only RECORD_ADMITTED_RESULT. It records the exact evidence
    reference carried by that intent on the exact durable session identity. It does
    not retire the session, release an AUTOPTU_BOUND world agent, mutate Minecraft
    state, synthesize a result, or handle UNKNOWN/abandonment policy.
    """
    if intent.kind != AutoPTUAuthorityTransitionKind.RECORD_ADMITTED_RESULT:
        raise ValueError("executor accepts only RECORD_ADMITTED_RESULT intents")

    result_ref = "" if intent.evidence_ref is None else str(intent.evidence_ref).strip()
    if not result_ref:
        raise ValueError("RECORD_ADMITTED_RESULT requires an exact result reference")

    before = ledger.get(intent.session_id)
    if before.state not in {AutoPTUSessionState.ENGINE_BOUND, AutoPTUSessionState.RESULT_RECORDED}:
        raise ValueError(
            "admitted result recording requires ENGINE_BOUND or matching RESULT_RECORDED session"
        )
    if before.state == AutoPTUSessionState.RESULT_RECORDED and before.authoritative_result_ref != result_ref:
        raise ValueError("session already records a different authoritative result")

    after = ledger.record_authoritative_result(intent.session_id, result_ref=result_ref)
    return AutoPTUAdmittedResultExecution(
        session_id=after.session_id,
        result_ref=result_ref,
        changed=before.state != AutoPTUSessionState.RESULT_RECORDED,
        state=after.state,
    )
