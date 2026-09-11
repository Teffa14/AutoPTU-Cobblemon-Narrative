from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.autoptu_engine_authority_report import AutoPTUEngineAuthorityReconciliation


class AutoPTUAuthorityTransitionKind(str, Enum):
    HOLD_ENGINE_BOUND = "HOLD_ENGINE_BOUND"
    RECORD_ADMITTED_RESULT = "RECORD_ADMITTED_RESULT"
    HOLD_PENDING_RESULT_ADMISSION = "HOLD_PENDING_RESULT_ADMISSION"
    QUARANTINE_FOR_ENGINE_UNKNOWN = "QUARANTINE_FOR_ENGINE_UNKNOWN"
    HOLD_PENDING_ABANDONMENT_POLICY = "HOLD_PENDING_ABANDONMENT_POLICY"


@dataclass(frozen=True)
class AutoPTUAuthorityTransitionIntent:
    session_id: str
    kind: AutoPTUAuthorityTransitionKind
    evidence_ref: str | None = None


@dataclass(frozen=True)
class AutoPTUAuthorityTransitionPlan:
    intents: tuple[AutoPTUAuthorityTransitionIntent, ...]

    def for_session(self, session_id: str) -> AutoPTUAuthorityTransitionIntent:
        matches = tuple(intent for intent in self.intents if intent.session_id == session_id)
        if len(matches) != 1:
            raise ValueError(f"expected exactly one transition intent for session: {session_id}")
        return matches[0]


def _normalized_refs(values: Iterable[str]) -> set[str]:
    result: set[str] = set()
    for value in values:
        cleaned = str(value).strip()
        if not cleaned:
            raise ValueError("admitted result references cannot be blank")
        result.add(cleaned)
    return result


def plan_engine_authority_followup(
    reconciliation: AutoPTUEngineAuthorityReconciliation,
    *,
    admitted_result_refs: Iterable[str] = (),
) -> AutoPTUAuthorityTransitionPlan:
    """Plan conservative post-report handling without mutating the session ledger.

    A COMPLETED engine claim may advance only when its exact result reference has
    already passed the separate semantic-result admission boundary. ACTIVE stays
    engine-bound. UNKNOWN is isolated for review. Explicit abandonment remains a
    policy question and cannot be translated into a battle result or retirement.
    """
    admitted = _normalized_refs(admitted_result_refs)
    intents: list[AutoPTUAuthorityTransitionIntent] = []
    seen: set[str] = set()

    def add(intent: AutoPTUAuthorityTransitionIntent) -> None:
        if intent.session_id in seen:
            raise ValueError(f"multiple transition intents for one session: {intent.session_id}")
        seen.add(intent.session_id)
        intents.append(intent)

    for session_id in reconciliation.active_session_ids:
        add(AutoPTUAuthorityTransitionIntent(session_id, AutoPTUAuthorityTransitionKind.HOLD_ENGINE_BOUND))

    for session_id, result_ref in reconciliation.completed_results:
        if result_ref in admitted:
            add(
                AutoPTUAuthorityTransitionIntent(
                    session_id,
                    AutoPTUAuthorityTransitionKind.RECORD_ADMITTED_RESULT,
                    evidence_ref=result_ref,
                )
            )
        else:
            add(
                AutoPTUAuthorityTransitionIntent(
                    session_id,
                    AutoPTUAuthorityTransitionKind.HOLD_PENDING_RESULT_ADMISSION,
                    evidence_ref=result_ref,
                )
            )

    for session_id in reconciliation.unknown_session_ids:
        add(
            AutoPTUAuthorityTransitionIntent(
                session_id,
                AutoPTUAuthorityTransitionKind.QUARANTINE_FOR_ENGINE_UNKNOWN,
            )
        )

    for session_id, authorization_ref in reconciliation.explicitly_abandoned:
        add(
            AutoPTUAuthorityTransitionIntent(
                session_id,
                AutoPTUAuthorityTransitionKind.HOLD_PENDING_ABANDONMENT_POLICY,
                evidence_ref=authorization_ref,
            )
        )

    reported = set(reconciliation.reported_session_ids)
    if seen != reported:
        missing = sorted(reported - seen)
        unexpected = sorted(seen - reported)
        raise ValueError(
            f"authority transition plan does not cover reconciliation exactly; missing={missing}, unexpected={unexpected}"
        )

    return AutoPTUAuthorityTransitionPlan(tuple(sorted(intents, key=lambda item: item.session_id)))
