from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Mapping

from tools.autoptu_session_identity import AutoPTUSessionLedger, AutoPTUSessionState


@dataclass(frozen=True)
class WorldConsequenceMapper:
    mapper_id: str
    result_type: str
    consequence_kind: str
    required_payload_fields: tuple[str, ...]
    allowed_payload_fields: tuple[str, ...]


@dataclass(frozen=True)
class AdmittedSemanticResult:
    result_ref: str
    result_type: str
    provenance_ref: str
    semantic_payload: Mapping[str, object]


@dataclass(frozen=True)
class WorldConsequenceTransaction:
    transaction_id: str
    session_id: str
    result_ref: str
    mapper_id: str
    consequence_kind: str
    provenance_ref: str
    projected_payload: tuple[tuple[str, object], ...]


class WorldConsequenceTransactionLedger:
    """Durable-style idempotency seam for admitted AutoPTU world consequences.

    This ledger records an explicitly mapped world consequence transaction. It
    does not reconstruct tactical state and does not mutate world state itself.
    A later owner-specific executor may consume a committed transaction.
    """

    def __init__(self) -> None:
        self._transactions: dict[str, WorldConsequenceTransaction] = {}

    def get(self, transaction_id: str) -> WorldConsequenceTransaction:
        try:
            return self._transactions[transaction_id]
        except KeyError as exc:
            raise KeyError(f"unknown world consequence transaction: {transaction_id}") from exc

    def all(self) -> tuple[WorldConsequenceTransaction, ...]:
        return tuple(self._transactions[key] for key in sorted(self._transactions))

    def commit(
        self,
        *,
        session_ledger: AutoPTUSessionLedger,
        session_id: str,
        result: AdmittedSemanticResult,
        mapper: WorldConsequenceMapper,
    ) -> tuple[WorldConsequenceTransaction, bool]:
        session = session_ledger.get(session_id)
        if session.state not in (AutoPTUSessionState.RESULT_RECORDED, AutoPTUSessionState.RETIRED):
            raise ValueError("world consequence requires RESULT_RECORDED or RETIRED session")

        result_ref = str(result.result_ref).strip()
        if not result_ref or session.authoritative_result_ref != result_ref:
            raise ValueError("semantic result does not match durable AutoPTU session result")

        if not str(result.provenance_ref).strip():
            raise ValueError("semantic result provenance_ref is required")
        if result.result_type != mapper.result_type:
            raise ValueError("semantic result type is not admitted by mapper")
        if not mapper.mapper_id.strip() or not mapper.consequence_kind.strip():
            raise ValueError("mapper identity and consequence kind are required")

        allowed = set(mapper.allowed_payload_fields)
        required = set(mapper.required_payload_fields)
        if not required.issubset(allowed):
            raise ValueError("mapper required fields must be a subset of allowed fields")

        supplied = set(result.semantic_payload)
        missing = required - supplied
        unknown = supplied - allowed
        if missing:
            raise ValueError(f"semantic payload missing required fields: {sorted(missing)}")
        if unknown:
            raise ValueError(f"semantic payload contains unmapped fields: {sorted(unknown)}")

        projected = tuple(sorted((key, result.semantic_payload[key]) for key in supplied))
        identity = "|".join((session_id, result_ref, mapper.mapper_id))
        transaction_id = "ouros.world-consequence." + sha256(identity.encode("utf-8")).hexdigest()[:24]
        candidate = WorldConsequenceTransaction(
            transaction_id=transaction_id,
            session_id=session_id,
            result_ref=result_ref,
            mapper_id=mapper.mapper_id,
            consequence_kind=mapper.consequence_kind,
            provenance_ref=result.provenance_ref,
            projected_payload=projected,
        )

        existing = self._transactions.get(transaction_id)
        if existing is not None:
            if existing != candidate:
                raise ValueError("conflicting replay for world consequence transaction")
            return existing, False

        self._transactions[transaction_id] = candidate
        return candidate, True
