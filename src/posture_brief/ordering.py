"""Order findings by severity and count them. Deterministic, no model involved."""

from __future__ import annotations

from posture_brief.findings import SEVERITIES, Finding


def severity_rank(finding: Finding) -> tuple[int, str]:
    """Sort key: most severe first, then by id so ties never depend on file order."""
    # SEVERITIES is already written from most to least severe, so a finding's
    # position in that list is its rank (0 = critical).
    rank = SEVERITIES.index(finding.severity)
    return (rank, finding.id)


def order_findings(findings: list[Finding]) -> list[Finding]:
    """Return a new list, most severe first. The input list is not changed."""
    return sorted(findings, key=severity_rank)


def count_by_severity(findings: list[Finding]) -> dict[str, int]:
    """Count findings per severity. Every severity is present, even when zero."""
    counts = {}
    # Start every level at zero so the brief can always say "0 low".
    for severity in SEVERITIES:
        counts[severity] = 0
    # Add one for each finding.
    for finding in findings:
        counts[finding.severity] += 1
    return counts
