# Agent Prep Track: ATO 2026

A 21-session self-study track in preparation for **AI Agents in Production** (Don Shin) at ATO 2026, Monday, October 19, Raleigh Convention Center. It covers the foundations of the AI Agents & Vibe Coding workshop (Mark Hinkle) first, then works through the production syllabus: agent harnesses, context engineering, MCP and A2A, skills, memory, agent patterns, governance, security, tokenomics and ethics.

Every session ends with a deliverable committed to this repo.

## Through-line project: Cloud Posture Brief

One project carries all 21 sessions. It takes a set of cloud misconfiguration findings and returns a prioritized remediation brief for a non-technical owner. Each finding is mapped to a CIS benchmark item and a NIST 800-53 control family, with an effort estimate and a suggested fix.

- **Deterministic parts:** control ID mapping, severity math
- **Probabilistic parts:** prose, prioritization, explanation
- **Pieces:** web front end, an agent, and an MCP server exposing the control catalog and finding store as tools

## Repository layout

| Path | Purpose |
|---|---|
| [docs/](docs/) | The course plan ([ato2026-agent-prep-course.html](docs/ato2026-agent-prep-course.html)); open it in a browser |
| [agent/](agent/) | The agent behind the brief |
| [mcp/](mcp/) | MCP server (control catalog, finding store) |
| [skills/](skills/) | Agent skills |
| [evals/](evals/) | Eval suite |
| [notes/](notes/) | Session notes |

## Setup

Requires [mise](https://mise.jdx.dev/) (Node) and [uv](https://docs.astral.sh/uv/) (Python).

```zsh
# Node (version pinned in mise.toml)
mise install
node --version

# Python 3.12 (version pinned in .python-version)
uv python install 3.12
uv venv
source .venv/bin/activate
python --version
```

## Progress

Progress and notes for the course plan are stored in the browser that opens `docs/ato2026-agent-prep-course.html`.
