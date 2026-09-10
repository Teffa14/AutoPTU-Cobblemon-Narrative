from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path


LOW_LEVEL_HOLDER_MUTATORS = frozenset(
    {
        "checkout_reserved_resource",
        "return_resource",
        "execute_authorized_handoff",
    }
)

APPROVED_TOOL_CALLERS = {
    "checkout_reserved_resource": frozenset(
        {"tools/global_npc_resource_holder_transitions.py"}
    ),
    "return_resource": frozenset(
        {"tools/global_npc_resource_holder_transitions.py"}
    ),
    "execute_authorized_handoff": frozenset(
        {"tools/global_npc_resource_holder_transitions.py"}
    ),
}


@dataclass(frozen=True, order=True)
class HolderMutationCallsiteFinding:
    path: str
    line: int
    mutator: str


def _called_name(node: ast.Call) -> str | None:
    target = node.func
    if isinstance(target, ast.Name):
        return target.id
    if isinstance(target, ast.Attribute):
        return target.attr
    return None


def find_unjournaled_holder_mutation_calls(
    repo_root: Path,
) -> tuple[HolderMutationCallsiteFinding, ...]:
    """Return tool-layer calls that bypass the holder-transition journal boundary.

    Tests, research and historical documents are intentionally excluded. The audit is
    a production call-site guard: a new tool module may not call a low-level holder
    mutator unless that path is explicitly admitted in APPROVED_TOOL_CALLERS.
    """
    tools_root = repo_root / "tools"
    findings: list[HolderMutationCallsiteFinding] = []

    for source_path in sorted(tools_root.rglob("*.py")):
        relative_path = source_path.relative_to(repo_root).as_posix()
        source = source_path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=relative_path)

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            mutator = _called_name(node)
            if mutator not in LOW_LEVEL_HOLDER_MUTATORS:
                continue
            if relative_path in APPROVED_TOOL_CALLERS.get(mutator, frozenset()):
                continue
            findings.append(
                HolderMutationCallsiteFinding(
                    path=relative_path,
                    line=node.lineno,
                    mutator=mutator,
                )
            )

    return tuple(sorted(findings))
