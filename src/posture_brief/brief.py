"""Build the markdown remediation brief. Deterministic except for the summary text."""

from __future__ import annotations

from posture_brief.controls import NIST_FAMILY_NAMES, lookup_control
from posture_brief.findings import SEVERITIES, Finding
from posture_brief.ordering import count_by_severity, order_findings


def nist_label(family: str) -> str:
    """Turn a family code into 'Access Control (AC)'."""
    # A family missing from the name table is a bug in the table, so fail loudly.
    return f"{NIST_FAMILY_NAMES[family]} ({family})"


def template_summary(findings: list[Finding]) -> str:
    """Write the owner summary from a fixed template. No model, no API key needed."""
    counts = count_by_severity(findings)
    total = len(findings)
    ordered = order_findings(findings)

    # Say how many problems there are and how serious they are.
    parts = []
    for severity in SEVERITIES:
        if counts[severity] > 0:
            parts.append(f"{counts[severity]} {severity}")
    breakdown = ", ".join(parts)
    # Use the singular word when there is exactly one problem.
    noun = "security problem" if total == 1 else "security problems"
    text = f"We found {total} {noun} in your cloud account ({breakdown})."

    # Point the owner at the first thing to fix.
    first = ordered[0]
    text += f" Start with {first.id}: {first.title}."
    return text


def render_brief(findings: list[Finding], summary: str) -> str:
    """Build the full markdown brief for the given findings and summary text."""
    ordered = order_findings(findings)
    counts = count_by_severity(findings)
    lines = []

    # Title and the owner-facing summary come first.
    lines.append("# Cloud Security Brief")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary)
    lines.append("")

    # A small table of counts, computed by code and never by the model.
    lines.append("| Severity | Findings |")
    lines.append("|---|---|")
    for severity in SEVERITIES:
        lines.append(f"| {severity.capitalize()} | {counts[severity]} |")
    lines.append("")

    # One section per finding, most severe first.
    lines.append("## What to fix, in order")
    lines.append("")
    position = 1
    for finding in ordered:
        control = lookup_control(finding.control_id)

        lines.append(f"### {position}. [{finding.severity.upper()}] {finding.title} ({finding.id})")
        lines.append("")
        lines.append(f"- **Resource:** `{finding.resource}`")
        lines.append(f"- **What we saw:** {finding.description}")
        lines.append(f"- **How to fix it:** {control.fix}")
        lines.append(f"- **Effort:** {control.effort}")
        lines.append(f"- **CIS item:** {control.control_id} - {control.title}")

        # Show the main NIST family, plus any others that also apply.
        nist = nist_label(control.nist_primary)
        for family in control.nist_secondary:
            nist += f"; also {nist_label(family)}"
        lines.append(f"- **NIST 800-53 family:** {nist}")
        lines.append("")
        position += 1

    # Remind the reader which benchmark the CIS items come from.
    lines.append(f"_CIS items from the {lookup_control(ordered[0].control_id).benchmark_version}. "
                 "NIST families are our own mapping and need human review._")
    lines.append("")
    return "\n".join(lines)
