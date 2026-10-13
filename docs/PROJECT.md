# Posture Brief Lite

## Problem
Cloud security scanners produce long lists of findings written for engineers. The people who own the risk, such as a small business owner or an office manager, can't act on them. They need to know what is exposed, what to fix first, how hard it is, and why it matters, in plain English.

## Who has it
Owners of small and mid sized businesses that run on AWS or GCP and rely on a consultant (sgt7) to interpret scanner output.

## The one command that solves it
```
uv run posture-brief data/findings.sample.json
```
It reads a JSON file of findings and writes a markdown remediation brief to stdout. A later session also renders the brief as a static HTML page.

## What the tool does
| Step | Kind | Notes |
|---|---|---|
| Load and validate the findings file | Deterministic | Reject malformed input with a clear error |
| Map each finding to a CIS benchmark item and a NIST 800-53 control family | Deterministic | Lookup table, never model output. Unknown control id is an error, not a guess |
| Order findings by severity | Deterministic | Fixed severity ranking, ties broken by id |
| Estimate effort and suggest a fix | Deterministic | From the lookup table |
| Write the owner facing summary paragraph | Probabilistic | One LLM call, given facts the code already computed. Template fallback if no API key |

## Data shape
Each finding in the input has: `id`, `title`, `severity` (`critical|high|medium|low`), `resource`, `control_id`, `description`. The tool adds the CIS item, NIST family, effort and suggested fix. Control ids are pinned to **CIS AWS Foundations Benchmark v7.1.0** (Oct 2026). The NIST 800-53 family is not in the benchmark, so it is our own mapping and must be reviewed by a human. See `data/findings.sample.json`.

Each row of the control lookup table holds: `control_id`, `benchmark_version`, `title`, `assessment` (`automated|manual`), `nist_primary` (one family), `nist_secondary` (list, may be empty), `effort`, `fix`. NIST maps by the control that failed, not by the technology involved. A finding with no CIS item can still be mapped to NIST, and the brief says so plainly.

## Success criteria
1. Every finding in the sample file appears in the brief, mapped to a CIS item and a NIST 800-53 family, with none invented and none dropped.
2. Findings are ordered by severity, and running the tool twice on the same input gives the same order and the same mappings. Only the summary prose may vary.
3. The tool runs end to end with no API key, using the template summary, and exits with a clear error on a malformed file or an unknown control id.

## Non goals
- No web framework and no front end beyond one static page.
- No live connection to AWS or GCP. Input is a file.
- No automatic remediation. The tool recommends, a human acts.
- No real client data in this repo. Sample data is invented.
- No agent loop, MCP server or evals at the start. Those arrive in Sessions 10, 14 and 18.
- No model computed severity, counts or control mappings.
