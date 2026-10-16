"""Command line entry point: `uv run posture-brief <findings.json>`."""

from __future__ import annotations

import argparse
import sys

from posture_brief.controls import UnknownControlError, lookup_control
from posture_brief.findings import FindingsError, load_findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="posture-brief", description=__doc__)
    parser.add_argument("findings_file", help="path to a findings JSON file")
    args = parser.parse_args(argv)

    try:
        findings = load_findings(args.findings_file)
    except FindingsError as exc:
        print(f"error: {args.findings_file} is invalid:\n{exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: cannot read {args.findings_file}: {exc.strerror}", file=sys.stderr)
        return 1

    # Check every finding has a row in the control table before doing anything else.
    # An unknown id is an error, so the run stops here instead of guessing.
    problems = []
    for finding in findings:
        try:
            lookup_control(finding.control_id)
        except UnknownControlError as exc:
            problems.append(f"{finding.id}: {exc}")
    if problems:
        print(f"error: {args.findings_file} has unmapped findings:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(f"Loaded {len(findings)} findings from {args.findings_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
