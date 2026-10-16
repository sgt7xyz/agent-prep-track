from pathlib import Path

import pytest

from posture_brief.controls import (
    ASSESSMENTS,
    CONTROLS,
    EFFORTS,
    UnknownControlError,
    lookup_control,
)
from posture_brief.findings import load_findings

SAMPLE = Path(__file__).parent.parent / "data" / "findings.sample.json"


def test_known_control_returns_its_row():
    control = lookup_control("CIS-AWS-2.5")
    assert control.title == "Ensure MFA is enabled for the 'root' user account"
    assert control.nist_primary == "IA"


def test_unknown_control_is_an_error():
    with pytest.raises(UnknownControlError) as error:
        lookup_control("CIS-AWS-9.9.9")
    assert "CIS-AWS-9.9.9" in str(error.value)


def test_near_miss_id_is_not_guessed():
    # A lowercase or padded id must not quietly match a real row.
    for bad_id in ["cis-aws-2.5", " CIS-AWS-2.5", "CIS-AWS-2.5 ", "CIS-AWS-2", ""]:
        with pytest.raises(UnknownControlError):
            lookup_control(bad_id)


def test_every_sample_finding_has_a_table_row():
    # Success criterion 1: no finding in the sample file may be unmapped.
    for finding in load_findings(SAMPLE):
        assert lookup_control(finding.control_id).control_id == finding.control_id


def test_every_row_is_complete_and_consistent():
    for key, control in CONTROLS.items():
        assert control.control_id == key
        assert control.assessment in ASSESSMENTS
        assert control.effort in EFFORTS
        assert len(control.nist_primary) == 2
        assert control.nist_primary not in control.nist_secondary
        assert control.title.strip()
        assert control.fix.strip()


def test_cli_stops_on_unknown_control_id(tmp_path, capsys):
    from posture_brief.cli import main

    # A finding that is well formed but names a control we do not have.
    path = tmp_path / "findings.json"
    path.write_text(
        '[{"id": "F-900", "title": "t", "severity": "low", "resource": "r",'
        ' "control_id": "CIS-AWS-9.9.9", "description": "d"}]'
    )
    assert main([str(path)]) == 1
    assert "F-900" in capsys.readouterr().err
