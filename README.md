# Agent Prep Track: ATO 2026

A 21-session self-study track (about 34 hours) in preparation for **AI Agents in Production** (Don Shin) at ATO 2026, Monday, October 19, Raleigh Convention Center. It compresses the foundations of the AI Agents & Vibe Coding workshop (Mark Hinkle) into five sessions, then spends the remaining sixteen on the production syllabus: agent harnesses, context engineering, MCP and A2A, skills, memory, agent patterns, evals, security, sovereignty, tokenomics and ethics.

Every session ends with a deliverable committed to this repo.

## Schedule

The track starts **Tuesday, October 13** (Mon Oct 12 is a reset day).

| Day | Sessions | Focus |
|---|---|---|
| Tue Oct 13 | 1–3 | Setup, project spec, baseline |
| Wed Oct 14 | 4 | The development loop |
| Fri Oct 16 | 5, 8, 9, 10 | CI, CLI brief with API warm-up, reading, hand-built harness |
| Sat Oct 17 | 11, 13, 14, 16, 20 | Reading versions, MCP over stdio, security and identity, intro and day-of kit |
| **Sun Oct 18** | | **Rest day** |
| Mon Oct 19 | | All Things Open workshop |
| After the workshop | 6, 7, 12, 15, 17, 18, 19, 21 | Static deploy, specs, memory, skills, patterns, evals, observability, sovereignty |

Protect sessions 10 and 20 above all. Nothing is scheduled on Sunday.

## Through-line project: Posture Brief Lite

A small Python CLI. It reads a JSON file of cloud misconfiguration findings, maps each one to a CIS benchmark item and a NIST 800-53 control family, orders them by severity, and uses one LLM call to write a plain-English summary for a non-technical owner. Output is a markdown brief, also rendered as a static page.

- **Deterministic parts:** control ID mapping, severity math
- **Probabilistic part:** the owner-facing prose
- **How it grows:** hand-built agent harness (Session 10), MCP server (14), eval suite (18), threat model (20)

## Repository layout

| Path               | Purpose                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| [docs/](docs/)     | The course plan ([Agent Prep Track\_ ATO 2026.html](<docs/Agent Prep Track_ ATO 2026.html>)); open it in a browser |
| [agent/](agent/)   | The agent behind the brief                                                                                         |
| [mcp/](mcp/)       | MCP server (control catalog, finding store)                                                                        |
| [skills/](skills/) | Agent skills                                                                                                       |
| [evals/](evals/)   | Eval suite                                                                                                         |
| [notes/](notes/)   | Session notes                                                                                                      |

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

## Progress
