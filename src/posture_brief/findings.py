"""Load and validate a findings file. Deterministic, no model involved."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

SEVERITIES = ("critical", "high", "medium", "low")
FIELDS = ("id", "title", "severity", "resource", "control_id", "description")
CONTROL_ID_PATTERN = re.compile(r"^CIS-AWS-\d+(\.\d+)*$")


class FindingsError(ValueError):
    """The findings file is malformed. The message lists every problem found."""


@dataclass(frozen=True)
class Finding:
    id: str
    title: str
    severity: str
    resource: str
    control_id: str
    description: str


def load_findings(path: str | Path) -> list[Finding]:
    """Read and validate a findings file, returning findings in file order.

    Raises FindingsError listing every problem found, not just the first.
    """
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise FindingsError("not a text file: it is not valid UTF-8") from exc
    except json.JSONDecodeError as exc:
        raise FindingsError(
            f"not valid JSON (line {exc.lineno}, column {exc.colno}): {exc.msg}"
        ) from exc

    if not isinstance(raw, list):
        raise FindingsError("top level must be a JSON list of findings")
    if not raw:
        raise FindingsError("the file contains no findings")

    errors: list[str] = []
    findings: list[Finding] = []
    seen_ids: set[str] = set()

    for position, item in enumerate(raw, start=1):
        label = _label(item, position)
        if not isinstance(item, dict):
            errors.append(f"{label}: must be a JSON object")
            continue

        problems = _check_item(item, label)
        item_id = item.get("id")
        if isinstance(item_id, str) and item_id.strip():
            if item_id in seen_ids:
                problems.append(f"{label}: duplicate id")
            seen_ids.add(item_id)

        if problems:
            errors.extend(problems)
        else:
            findings.append(Finding(**{name: item[name] for name in FIELDS}))

    if errors:
        raise FindingsError("\n".join(errors))
    return findings


def _label(item: object, position: int) -> str:
    if isinstance(item, dict) and isinstance(item.get("id"), str) and item["id"].strip():
        return f"finding {item['id']}"
    return f"finding at position {position}"


def _check_item(item: dict, label: str) -> list[str]:
    problems: list[str] = []
    for name in FIELDS:
        if name not in item:
            problems.append(f"{label}: missing required field '{name}'")
        elif not isinstance(item[name], str) or not item[name].strip():
            problems.append(f"{label}: field '{name}' must be a non-empty string")
    for name in item:
        if name not in FIELDS:
            problems.append(f"{label}: unexpected field '{name}'")

    severity = item.get("severity")
    if isinstance(severity, str) and severity.strip() and severity not in SEVERITIES:
        allowed = "|".join(SEVERITIES)
        problems.append(f"{label}: severity '{severity}' is not one of {allowed}")

    control_id = item.get("control_id")
    if (
        isinstance(control_id, str)
        and control_id.strip()
        and not CONTROL_ID_PATTERN.match(control_id)
    ):
        problems.append(f"{label}: control_id '{control_id}' does not look like CIS-AWS-<number>")
    return problems
