"""Command line entry point: `uv run posture-brief <findings.json>`."""

from __future__ import annotations

import argparse
import sys

from posture_brief.brief import render_brief
from posture_brief.controls import UnknownControlError, lookup_control
from posture_brief.findings import FindingsError, load_findings
from posture_brief.summary import get_summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="posture-brief", description=__doc__)
    parser.add_argument("findings_file", help="path to a findings JSON file")
    parser.add_argument(
        "--template-only",
        action="store_true",
        help="skip the model and use the template summary",
    )
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

    # The summary comes from the model when a key is set, else from the template.
    # The note explains a fallback. It goes to stderr so the brief stays clean.
    summary, note = get_summary(findings, use_model=not args.template_only)
    if note:
        print(f"note: {note}", file=sys.stderr)
    print(render_brief(findings, summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
