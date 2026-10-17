from pathlib import Path

from posture_brief.brief import render_brief, template_summary
from posture_brief.cli import main
from posture_brief.controls import CONTROLS, NIST_FAMILY_NAMES
from posture_brief.findings import load_findings

SAMPLE = Path(__file__).parent.parent / "data" / "findings.sample.json"


def sample_brief() -> str:
    findings = load_findings(SAMPLE)
    return render_brief(findings, template_summary(findings))


def test_every_finding_appears_exactly_once():
    brief = sample_brief()
    for finding in load_findings(SAMPLE):
        assert brief.count(f"({finding.id})") == 1
        assert finding.title in brief


def test_findings_appear_in_severity_order():
    brief = sample_brief()
    positions = []
    for finding_id in ["F-001", "F-002", "F-003", "F-004", "F-005"]:
        positions.append(brief.index(f"({finding_id})"))
    assert positions == sorted(positions)


def test_each_finding_shows_cis_item_and_nist_family():
    brief = sample_brief()
    assert "CIS-AWS-6.3" in brief
    assert "System and Communications Protection (SC)" in brief
    assert "also Access Control (AC)" in brief


def test_count_table_is_correct():
    brief = sample_brief()
    assert "| Critical | 2 |" in brief
    assert "| High | 1 |" in brief
    assert "| Low | 1 |" in brief


def test_template_summary_is_stable_and_mentions_the_first_fix():
    findings = load_findings(SAMPLE)
    first = template_summary(findings)
    assert first == template_summary(findings)
    assert "5 security problems" in first
    assert "Start with F-001" in first


def test_same_input_gives_identical_brief():
    assert sample_brief() == sample_brief()


def test_every_nist_family_in_the_table_has_a_name():
    for control in CONTROLS.values():
        assert control.nist_primary in NIST_FAMILY_NAMES
        for family in control.nist_secondary:
            assert family in NIST_FAMILY_NAMES


def test_cli_prints_the_brief(capsys):
    assert main([str(SAMPLE)]) == 0
    assert "## What to fix, in order" in capsys.readouterr().out


def test_summary_uses_singular_for_one_finding():
    one = load_findings(SAMPLE)[:1]
    assert "1 security problem in" in template_summary(one)
