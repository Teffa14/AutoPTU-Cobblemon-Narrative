from __future__ import annotations

import sys
from pathlib import Path

from tools.ecology_fixture_scope import ecology_fixture_paths
from tools.validate_ecology_fixtures import ValidationError, validate_file


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    paths = ecology_fixture_paths(root)
    if not paths:
        print("No ecology-owned fixture JSON files found", file=sys.stderr)
        return 2

    failures: list[str] = []
    for path in paths:
        try:
            validate_file(path)
            print(f"PASS {path.relative_to(root)}")
        except ValidationError as exc:
            failures.append(str(exc))
            print(f"FAIL {exc}", file=sys.stderr)

    if failures:
        print(f"{len(failures)} ecology fixture(s) failed validation", file=sys.stderr)
        return 1
    print(f"Validated {len(paths)} ecology-owned fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
