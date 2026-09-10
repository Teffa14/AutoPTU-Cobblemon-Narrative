from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.autoptu_session_identity import AutoPTUSessionState
from tools.global_npc_autoptu_session_recovery import AutoPTUSessionRecoveryValidation


class AutoPTUEngineAuthorityState(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    UNKNOWN = "UNKNOWN"
    EXPLICITLY_ABANDONED = "EXPLICITLY_ABANDONED"


@dataclass(frozen=True)
class AutoPTUEngineAuthorityReport:
    session_id: str
    engine_session_ref: str
    authority_ref: str
    authority_report_ref: str
    observed_at_minute: int
    state: AutoPTUEngineAuthorityState
    authoritative_result_ref: str | None = None
    abandonment_authorization_ref: str | None = None


@dataclass(frozen=True)
class AutoPTUEngineAuthorityReconciliation:
    active_session_ids: tuple[str, ...]
    completed_results: tuple[tuple[str, str], ...]
    unknown_session_ids: tuple[str, ...]
    explicitly_abandoned: tuple[tuple[str, str], ...]
    reported_session_ids: tuple[str, ...]


def _required(value: str, field: str) -> str:
    cleaned = str(value).strip()
    if not cleaned:
        raise ValueError(f"{field} is required")
    return cleaned


def _validate_report_shape(report: AutoPTUEngineAuthorityReport) -> None:
    _required(report.session_id, "session_id")
    _required(report.engine_session_ref, "engine_session_ref")
    _required(report.authority_ref, "authority_ref")
    _required(report.authority_report_ref, "authority_report_ref")
    if report.observed_at_minute < 0:
        raise ValueError("observed_at_minute cannot be negative")

    if report.state == AutoPTUEngineAuthorityState.COMPLETED:
        _required(report.authoritative_result_ref or "", "authoritative_result_ref")
        if report.abandonment_authorization_ref is not None:
            raise ValueError("completed authority report cannot also carry abandonment authorization")
        return

    if report.state == AutoPTUEngineAuthorityState.EXPLICITLY_ABANDONED:
        _required(report.abandonment_authorization_ref or "", "abandonment_authorization_ref")
        if report.authoritative_result_ref is not None:
            raise ValueError("abandoned authority report cannot also carry an authoritative result")
        return

    if report.authoritative_result_ref is not None:
        raise ValueError(f"{report.state.value} authority report cannot carry an authoritative result")
    if report.abandonment_authorization_ref is not None:
        raise ValueError(f"{report.state.value} authority report cannot carry abandonment authorization")


def reconcile_engine_authority_reports(
    validation: AutoPTUSessionRecoveryValidation,
    reports: Iterable[AutoPTUEngineAuthorityReport],
) -> AutoPTUEngineAuthorityReconciliation:
    """Validate external engine-authority claims against restored Ouros session identity.

    The reports are evidence supplied by a future verified AutoPTU authority adapter.
    This function validates identity/provenance and classifies the claims. It does not
    mutate the Ouros session ledger, release world agents, synthesize battle results,
    or infer tactical state from Minecraft/Cobblemon presentation.
    """
    active: list[str] = []
    completed: list[tuple[str, str]] = []
    unknown: list[str] = []
    abandoned: list[tuple[str, str]] = []
    seen_sessions: set[str] = set()
    seen_report_refs: set[str] = set()

    for report in sorted(reports, key=lambda item: (item.session_id, item.authority_report_ref)):
        _validate_report_shape(report)
        if report.session_id in seen_sessions:
            raise ValueError(f"multiple authority reports supplied for one session: {report.session_id}")
        if report.authority_report_ref in seen_report_refs:
            raise ValueError(f"duplicate authority_report_ref: {report.authority_report_ref}")
        seen_sessions.add(report.session_id)
        seen_report_refs.add(report.authority_report_ref)

        binding = validation.ledger.get(report.session_id)
        if binding.state != AutoPTUSessionState.ENGINE_BOUND:
            raise ValueError(
                f"engine authority reconciliation requires unresolved ENGINE_BOUND session: {report.session_id}"
            )
        if binding.authoritative_result_ref is not None:
            raise ValueError(f"engine-bound session unexpectedly already has a result: {report.session_id}")
        if binding.engine_session_ref != report.engine_session_ref:
            raise ValueError(f"engine_session_ref mismatch for session: {report.session_id}")
        if report.observed_at_minute < binding.requested_at_minute:
            raise ValueError(f"authority report predates session request: {report.session_id}")
        if report.observed_at_minute > validation.semantic_minute:
            raise ValueError(f"authority report is newer than recovery cut: {report.session_id}")

        if report.state == AutoPTUEngineAuthorityState.ACTIVE:
            active.append(report.session_id)
        elif report.state == AutoPTUEngineAuthorityState.COMPLETED:
            completed.append((report.session_id, _required(report.authoritative_result_ref or "", "authoritative_result_ref")))
        elif report.state == AutoPTUEngineAuthorityState.UNKNOWN:
            unknown.append(report.session_id)
        elif report.state == AutoPTUEngineAuthorityState.EXPLICITLY_ABANDONED:
            abandoned.append(
                (
                    report.session_id,
                    _required(report.abandonment_authorization_ref or "", "abandonment_authorization_ref"),
                )
            )
        else:  # pragma: no cover - Enum exhaustiveness guard
            raise ValueError(f"unsupported AutoPTU engine authority state: {report.state}")

    return AutoPTUEngineAuthorityReconciliation(
        active_session_ids=tuple(active),
        completed_results=tuple(completed),
        unknown_session_ids=tuple(unknown),
        explicitly_abandoned=tuple(abandoned),
        reported_session_ids=tuple(sorted(seen_sessions)),
    )
