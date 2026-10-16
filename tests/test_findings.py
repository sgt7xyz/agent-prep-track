import json
from pathlib import Path

import pytest

from posture_brief.cli import main
from posture_brief.findings import FindingsError, load_findings

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "findings.sample.json"
MISSING_SEVERITY = ROOT / "tests" / "fixtures" / "missing_severity.json"

GOOD = {
    "id": "F-100",
    "title": "t",
    "severity": "high",
    "resource": "r",
    "control_id": "CIS-AWS-6.3",
    "description": "d",
}


def write(tmp_path, data) -> Path:
    path = tmp_path / "findings.json"
    path.write_text(data if isinstance(data, str) else json.dumps(data))
    return path


def test_valid_file_loads_all_five_findings():
    findings = load_findings(SAMPLE)
    assert [f.id for f in findings] == ["F-001", "F-002", "F-003", "F-004", "F-005"]


def test_missing_severity_names_the_field_and_the_finding():
    with pytest.raises(FindingsError) as exc:
        load_findings(MISSING_SEVERITY)
    assert "finding F-003" in str(exc.value)
    assert "missing required field 'severity'" in str(exc.value)


def test_all_problems_are_reported_together(tmp_path):
    bad = [
        {**GOOD, "id": "F-1", "severity": "urgent"},
        {k: v for k, v in GOOD.items() if k != "title"} | {"id": "F-2"},
    ]
    with pytest.raises(FindingsError) as exc:
        load_findings(write(tmp_path, bad))
    assert "finding F-1" in str(exc.value) and "urgent" in str(exc.value)
    assert "finding F-2" in str(exc.value) and "'title'" in str(exc.value)


@pytest.mark.parametrize(
    "data, expected",
    [
        ("{not json", "not valid JSON"),
        ({"id": "F-1"}, "must be a JSON list"),
        ([], "no findings"),
        (["nope"], "must be a JSON object"),
        ([{**GOOD, "control_id": "AWS-6.3"}], "control_id"),
        ([{**GOOD, "title": "  "}], "non-empty string"),
        ([{**GOOD, "extra": "x"}], "unexpected field 'extra'"),
        ([GOOD, GOOD], "duplicate id"),
    ],
)
def test_malformed_input_is_rejected_with_a_clear_message(tmp_path, data, expected):
    with pytest.raises(FindingsError) as exc:
        load_findings(write(tmp_path, data))
    assert expected in str(exc.value)


def test_non_text_file_is_rejected_not_a_traceback(tmp_path, capsys):
    path = tmp_path / "binary.json"
    path.write_bytes(b"\xff\xfe\x00bad")
    with pytest.raises(FindingsError, match="not valid UTF-8"):
        load_findings(path)
    assert main([str(path)]) == 1
    assert "not valid UTF-8" in capsys.readouterr().err


def test_cli_succeeds_on_the_sample(capsys):
    assert main([str(SAMPLE)]) == 0
    assert "Loaded 6 findings" in capsys.readouterr().out


def test_cli_fails_with_exit_1_and_names_the_problem(capsys):
    assert main([str(MISSING_SEVERITY)]) == 1
    assert "severity" in capsys.readouterr().err


def test_cli_reports_a_missing_file(capsys):
    assert main(["does-not-exist.json"]) == 1
    assert "cannot read" in capsys.readouterr().err
