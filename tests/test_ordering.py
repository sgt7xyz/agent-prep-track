from pathlib import Path

from posture_brief.findings import Finding, load_findings
from posture_brief.ordering import count_by_severity, order_findings

SAMPLE = Path(__file__).parent.parent / "data" / "findings.sample.json"


def make_finding(finding_id: str, severity: str) -> Finding:
    # Only id and severity matter for ordering, so the rest is filler.
    return Finding(
        id=finding_id,
        title="t",
        severity=severity,
        resource="r",
        control_id="CIS-AWS-2.5",
        description="d",
    )


def ids(findings: list[Finding]) -> list[str]:
    result = []
    for finding in findings:
        result.append(finding.id)
    return result


def test_sample_is_ordered_critical_to_low():
    ordered = order_findings(load_findings(SAMPLE))
    assert ids(ordered) == ["F-001", "F-002", "F-003", "F-004", "F-005"]


def test_shuffled_input_gives_the_same_order():
    shuffled = [
        make_finding("F-5", "low"),
        make_finding("F-3", "high"),
        make_finding("F-1", "critical"),
        make_finding("F-4", "medium"),
    ]
    assert ids(order_findings(shuffled)) == ["F-1", "F-3", "F-4", "F-5"]


def test_ties_are_broken_by_id():
    findings = [make_finding("F-9", "high"), make_finding("F-2", "high")]
    assert ids(order_findings(findings)) == ["F-2", "F-9"]


def test_input_order_does_not_change_the_result():
    findings = [make_finding("F-1", "low"), make_finding("F-2", "low")]
    forward = ids(order_findings(findings))
    backward = ids(order_findings(list(reversed(findings))))
    assert forward == backward


def test_input_list_is_not_modified():
    findings = [make_finding("F-2", "low"), make_finding("F-1", "critical")]
    order_findings(findings)
    assert ids(findings) == ["F-2", "F-1"]


def test_counts_for_the_sample():
    counts = count_by_severity(load_findings(SAMPLE))
    assert counts == {"critical": 2, "high": 1, "medium": 1, "low": 1}


def test_counts_include_zero_levels():
    counts = count_by_severity([make_finding("F-1", "low")])
    assert counts == {"critical": 0, "high": 0, "medium": 0, "low": 1}
