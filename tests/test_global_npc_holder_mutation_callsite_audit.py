from __future__ import annotations

from pathlib import Path

from tools.global_npc_holder_mutation_callsite_audit import (
    HolderMutationCallsiteFinding,
    find_unjournaled_holder_mutation_calls,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_production_tools_have_no_unjournaled_holder_mutation_callers() -> None:
    assert find_unjournaled_holder_mutation_calls(REPO_ROOT) == ()


def test_audit_detects_direct_and_module_qualified_bypasses(tmp_path: Path) -> None:
    tools = tmp_path / "tools"
    tools.mkdir()
    (tools / "bad_direct.py").write_text(
        "def run(resource, ledger):\n"
        "    return checkout_reserved_resource(resource, ledger, 'actor', 1)\n",
        encoding="utf-8",
    )
    (tools / "bad_qualified.py").write_text(
        "def run(module, ledger, resource, transfer):\n"
        "    return module.execute_authorized_handoff(ledger, resource, transfer)\n",
        encoding="utf-8",
    )

    assert find_unjournaled_holder_mutation_calls(tmp_path) == (
        HolderMutationCallsiteFinding(
            path="tools/bad_direct.py",
            line=2,
            mutator="checkout_reserved_resource",
        ),
        HolderMutationCallsiteFinding(
            path="tools/bad_qualified.py",
            line=2,
            mutator="execute_authorized_handoff",
        ),
    )
