import hashlib
import json

import pytest

from tests.test_global_npc_world_resource_reschedule_checkpoint import _fixture
from tools.global_npc_resource_handoff_reschedule_admission import RescheduleAdmissionAssessment, RescheduleAdmissionState
from tools.global_npc_resource_handoff_reschedule_admission_history import (
    ResourceRescheduleAdmissionLedger,
    record_reschedule_admission,
)
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation
from tools.global_npc_world_resource_checkpoint import build_world_resource_checkpoint
from tools.global_npc_world_resource_admission_checkpoint import (
    WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA,
    build_world_resource_admission_checkpoint,
    restore_world_resource_admission_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _state():
    coordinator, channels, _, requests, handoffs, attempts, appointments, reschedules = _fixture(deliver=True)
    reservations = ReservationLedger((
        ResourceReservation(
            "reservation:other", "meter:field:7", "ori", 95, 110, purpose_ref="survey:marsh"
        ),
    ))
    assessment = RescheduleAdmissionAssessment(
        state=RescheduleAdmissionState.CONFLICT,
        proposal_id="proposal:later",
        resource_id="meter:field:7",
        conflicting_reservation_ids=("reservation:other",),
    )
    admissions = record_reschedule_admission(
        ResourceRescheduleAdmissionLedger(),
        assessment,
        record_id="admission:world:1",
        assessed_tick=49,
    )
    return coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, admissions


def test_v11_round_trip_binds_historical_conflict_to_same_world_instant() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, admissions = _state()
    checkpoint = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
        admission_ledger=admissions,
    )

    assert checkpoint["schema"] == WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V6"
    restored = restore_world_resource_admission_checkpoint(checkpoint, channels=channels)
    assert restored.admission_ledger == admissions
    assert restored.world_resource.reservation_ledger == reservations
    assert restored.world_resource.reschedule_ledger == reschedules
    assert restored.world_resource.world.coordinator.information_queue.envelope_provenance("delivery:reschedule") is not None


def test_v11_global_digest_covers_admission_evidence() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, admissions = _state()
    checkpoint = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
        admission_ledger=admissions,
    )
    checkpoint["resource_state"]["reschedule_admission_records"][0]["state"] = "CLEAR"

    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_resource_admission_checkpoint(checkpoint, channels=channels)


def test_v11_rejects_admission_from_after_restored_world_time() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, admissions = _state()
    checkpoint = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
        admission_ledger=admissions,
    )
    checkpoint["semantic_minute"] = 48
    checkpoint["sha256"] = _digest({key: value for key, value in checkpoint.items() if key != "sha256"})

    with pytest.raises(ValueError, match="assessment comes from the future"):
        restore_world_resource_admission_checkpoint(checkpoint, channels=channels)


def test_v10_migration_keeps_admission_history_empty() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, _ = _state()
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
    )

    restored = restore_world_resource_admission_checkpoint(checkpoint, channels=channels)
    assert restored.world_resource.reschedule_ledger == reschedules
    assert restored.admission_ledger == ResourceRescheduleAdmissionLedger()


def test_v11_rejects_conflict_evidence_removed_from_same_checkpoint() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules, admissions = _state()
    checkpoint = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
        admission_ledger=admissions,
    )
    checkpoint["resource_state"]["reservations"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="missing conflict reservation"):
        restore_world_resource_admission_checkpoint(checkpoint, channels=channels)
