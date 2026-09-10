# Global NPC Holder Mutation Callsite Audit Contract — Pass 402

Status: IMPLEMENTED / GLOBAL NPC RESOURCE SEAM
Canon effect: NONE

## Purpose

Pass 401 closed the known rescheduled-handoff bypass, but the lower-level holder-mutating functions remain available for compatibility and isolated tests. Future production code could accidentally call one directly and silently create a `WorldResource.holder_actor_id` change without a matching `ResourceHolderTransition`.

Pass 402 makes that risk executable in CI.

## Protected mutation boundary

The production tool layer currently has three low-level functions that can change holder state:

- `checkout_reserved_resource()`
- `return_resource()`
- `execute_authorized_handoff()`

Within `tools/`, the only admitted caller of those functions is `tools/global_npc_resource_holder_transitions.py`.

Higher-level runtimes must call the journal-aware operations exposed from that module or wrappers that eventually route through it.

## Executable audit

`tools/global_npc_holder_mutation_callsite_audit.py` parses every Python module under `tools/` with `ast` and reports calls to the three low-level mutators outside the admitted boundary.

The detector covers direct calls and module-qualified attribute calls.

`tests/test_global_npc_holder_mutation_callsite_audit.py` runs the audit against the repository and must remain empty. A synthetic regression proves that direct and module-qualified bypasses are detected.

## What this proves

For the repository revision under test, no production Python tool module currently calls the known holder-mutating primitives outside the journal-aware boundary.

This strengthens the holder-history coverage argument and protects it from future accidental bypasses.

## What this does not prove

It does not prove that the holder journal is complete before the journal system existed.

It does not prove that a mutation implemented through a new function name will be detected automatically. A future holder-mutating primitive must be added to this audit in the same change that introduces it.

It does not convert every existing resource into `complete_holder_history_resource_ids`. A complete interval still needs an authoritative baseline plus journal continuity through the recovery cut.

It does not give Minecraft, Cobblemon or Craftics authority to mutate holder state.

## Next seam

Add an authoritative holder-history coverage baseline for individual resources. Combine that baseline with this CI-enforced mutation boundary and the recovered holder-transition ledger. Only then derive complete holder-history coverage automatically for a bounded semantic interval.
