# Agent Prep Track: ATO 2026

A 21-session self-study track (about 33.5 hours) in preparation for **AI Agents in Production** (Don Shin) at ATO 2026, Monday, October 19, Raleigh Convention Center. It compresses the foundations of the AI Agents & Vibe Coding workshop (Mark Hinkle) into five sessions, then spends the remaining sixteen on the production syllabus: agent harnesses, context engineering, MCP and A2A, skills, memory, agent patterns, evals, security, sovereignty, tokenomics and ethics.

Every session ends with a deliverable committed to this repo.

## Schedule

The track starts **Tuesday, October 13** (Mon Oct 12 is a reset day).

| Day | Sessions | Focus |
|---|---|---|
| Tue Oct 13 | 1–5 | Setup, project spec, baseline, PR gate, agent review |
| Wed Oct 14 | 6–8 | v0 and Vercel, specs, ship v1 |
| Thu Oct 15 | 9–12 | Determinism, hand-built harness (Session 10), context, memory |
| Fri Oct 16 | 13–15 | MCP brief, MCP server, skills |
| Sat Oct 17 | 16–18 | A2A, agent patterns, evals |
| Sun Oct 18 | 19–21 | Observability, security, sovereignty; intro, questions, day-of kit |
| Mon Oct 19 | | All Things Open workshop |

If a day slips, protect sessions 10, 14 and 20 first; drop 18 and 17 before anything else.

## Through-line project: Cloud Posture Brief

One project carries all 21 sessions. It takes a set of cloud misconfiguration findings and returns a prioritized remediation brief for a non-technical owner. Each finding is mapped to a CIS benchmark item and a NIST 800-53 control family, with an effort estimate and a suggested fix.

- **Deterministic parts:** control ID mapping, severity math
- **Probabilistic parts:** prose, prioritization, explanation
- **Pieces:** web front end, an agent, and an MCP server exposing the control catalog and finding store as tools

## Repository layout

| Path | Purpose |
|---|---|
| [docs/](docs/) | The course plan ([Agent Prep Track_ ATO 2026.html](<docs/Agent Prep Track_ ATO 2026.html>)); open it in a browser |
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

Progress and notes for the course plan are stored in the browser that opens `docs/Agent Prep Track_ ATO 2026.html`.
