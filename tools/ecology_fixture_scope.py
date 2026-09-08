from __future__ import annotations

from pathlib import Path


ECOLOGY_FIXTURE_GLOB = "marea-sendero-*-fixture-v1.json"


def ecology_fixture_paths(root: Path) -> tuple[Path, ...]:
    """Return only fixtures owned by the current ecology validator.

    Global NPC, communication, resource and other implementation regressions live in
    the same implementation directory but have different schemas and validators.
    """
    implementation = root / "implementation"
    return tuple(sorted(implementation.glob(ECOLOGY_FIXTURE_GLOB)))
