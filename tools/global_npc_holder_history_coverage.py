from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from tools.global_npc_resource_holder_transitions import (
    ResourceHolderTransitionLedger,
    holder_history,
)
from tools.global_npc_resources import WorldResource


@dataclass(frozen=True)
class HolderHistoryCoverageBaseline:
    baseline_id: str
    resource_id: str
    at_tick: int
    holder_actor_id: str | None
    source_ref: str

    def __post_init__(self) -> None:
        if not self.baseline_id.strip():
            raise ValueError("baseline_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if isinstance(self.at_tick, bool) or not isinstance(self.at_tick, int):
            raise ValueError("at_tick must be an integer")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")
        if not self.source_ref.strip():
            raise ValueError("source_ref is required")


def derive_complete_holder_history_resource_ids(
    resources: Iterable[WorldResource],
    baselines: Iterable[HolderHistoryCoverageBaseline],
    holder_transition_ledger: ResourceHolderTransitionLedger,
    *,
    through_tick: int,
) -> frozenset[str]:
    """Derive bounded holder-history coverage from authoritative cut-state baselines.

    A baseline states the authoritative holder immediately after all holder mutations at
    its semantic tick. The current production mutation boundary is expected to journal
    every later accepted holder change. This function verifies that all journaled
    transitions after the baseline remain causally continuous through ``through_tick``.

    It does not compare the derived holder with the current resource catalog. That is
    the reconciliation layer's responsibility.
    """
    if isinstance(through_tick, bool) or not isinstance(through_tick, int):
        raise ValueError("through_tick must be an integer")
    if through_tick < 0:
        raise ValueError("through_tick must be non-negative")

    catalog: dict[str, WorldResource] = {}
    for resource in resources:
        if resource.resource_id in catalog:
            raise ValueError("duplicate world resource id")
        catalog[resource.resource_id] = resource

    by_resource: dict[str, HolderHistoryCoverageBaseline] = {}
    seen_baseline_ids: set[str] = set()
    for baseline in baselines:
        if baseline.baseline_id in seen_baseline_ids:
            raise ValueError("duplicate holder history coverage baseline id")
        seen_baseline_ids.add(baseline.baseline_id)
        if baseline.resource_id in by_resource:
            raise ValueError("multiple holder history coverage baselines for resource")
        if baseline.resource_id not in catalog:
            raise ValueError("holder history coverage baseline references resource absent from current catalog")
        if baseline.at_tick > through_tick:
            raise ValueError("holder history coverage baseline is later than requested coverage cut")
        by_resource[baseline.resource_id] = baseline

    complete: set[str] = set()
    for resource_id, baseline in by_resource.items():
        expected_holder = baseline.holder_actor_id
        transitions = (
            transition
            for transition in holder_history(
                holder_transition_ledger,
                resource_id,
                through_tick=through_tick,
            )
            if transition.at_tick > baseline.at_tick
        )
        for transition in transitions:
            if transition.from_actor_id != expected_holder:
                raise ValueError("holder history coverage baseline conflicts with journal continuity")
            expected_holder = transition.to_actor_id
        complete.add(resource_id)

    return frozenset(complete)
