from __future__ import annotations

from dataclasses import dataclass, field

from tools.autoptu_world_consequence_transaction import WorldConsequenceTransaction


@dataclass(frozen=True)
class WorldObservationRecord:
    transaction_id: str
    session_id: str
    result_ref: str
    objective_ref: str
    outcome: str
    provenance_ref: str
    evidence_ref: str | None = None


@dataclass
class WorldObservationLedger:
    """Consumes committed FIELD_OBSERVATION consequences without re-reading battle state."""

    records: dict[str, WorldObservationRecord] = field(default_factory=dict)

    def apply(self, transaction: WorldConsequenceTransaction) -> tuple[WorldObservationRecord, bool]:
        if transaction.consequence_kind != "FIELD_OBSERVATION":
            raise ValueError("world observation owner accepts FIELD_OBSERVATION only")

        payload = dict(transaction.projected_payload)
        allowed = {"objective_ref", "outcome", "evidence_ref"}
        unknown = set(payload) - allowed
        if unknown:
            raise ValueError(f"world observation payload contains unsupported fields: {sorted(unknown)}")

        objective_ref = str(payload.get("objective_ref", "")).strip()
        outcome = str(payload.get("outcome", "")).strip()
        if not objective_ref or not outcome:
            raise ValueError("world observation requires objective_ref and outcome")

        evidence_value = payload.get("evidence_ref")
        evidence_ref = None if evidence_value is None else str(evidence_value).strip()
        if evidence_value is not None and not evidence_ref:
            raise ValueError("evidence_ref must be non-empty when supplied")

        record = WorldObservationRecord(
            transaction_id=transaction.transaction_id,
            session_id=transaction.session_id,
            result_ref=transaction.result_ref,
            objective_ref=objective_ref,
            outcome=outcome,
            provenance_ref=transaction.provenance_ref,
            evidence_ref=evidence_ref,
        )

        existing = self.records.get(record.transaction_id)
        if existing is not None:
            if existing != record:
                raise ValueError("conflicting replay for world observation transaction")
            return existing, False

        self.records[record.transaction_id] = record
        return record, True

    def get(self, transaction_id: str) -> WorldObservationRecord:
        try:
            return self.records[transaction_id]
        except KeyError as exc:
            raise KeyError(f"unknown world observation transaction: {transaction_id}") from exc

    def all(self) -> tuple[WorldObservationRecord, ...]:
        return tuple(self.records[key] for key in sorted(self.records))
