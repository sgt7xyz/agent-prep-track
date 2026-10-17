# Determinism Map: Posture Brief Lite

Which parts of the tool may be probabilistic, and what happens if they are wrong.
Draft written by Claude at Steven's request, to be reviewed and rewritten in his own words.

## Definition

An agent is a model, in a loop, with tools, a context and a stopping condition, where the
model chooses the next step. Remove the choosing and it is a workflow. Remove the tools and
it is a chatbot. Posture Brief Lite today is a **workflow**: code decides every step and the
model writes one paragraph.

## The map

| # | Operation | Probabilistic OK? | Why | Blast radius if wrong |
|---|---|---|---|---|
| 1 | Validate the findings file | No | A bad file must be rejected the same way every time | Bad data flows into the brief; the owner acts on invented or missing findings |
| 2 | Reject an unknown control id | No | Guessing a mapping would hide a gap (AGENTS.md rule) | A finding gets the wrong fix; client remediates the wrong thing |
| 3 | Map a finding to its CIS item | No | Audit artifact, must be reproducible | Wrong benchmark cited; credibility lost with an auditor |
| 4 | Choose the NIST family | No, a human decides once | It is our own mapping, reviewed by a person and stored in a table | Wrong compliance family in a report; found at review, recoverable |
| 5 | Order findings by severity | No | Fixed ranking, ties broken by id | Critical issue buried under a low one; owner fixes the wrong thing first |
| 6 | Count findings per severity | No | Arithmetic; the model miscounted five words in the warm-up | Owner sees a wrong number of critical problems |
| 7 | Pick the "how to fix it" text | No, today | Written once in the table and reviewed | Unsafe or wrong advice. If a model suggested fixes later, a human must review them first |
| 8 | Write the owner summary paragraph | Yes | It is prose, and the table underneath shows the real facts | Awkward or wrong wording; can contradict the table (known gap, caught by reading or an eval) |
| 9 | Decide what data is sent to the model | No | Security decision: only titles, severity, effort and fix are sent | Resource names, ARNs or account ids leave the machine |
| 10 | Fall back to the template | No | Code checks the key, errors and stop_reason | If a model decided, a bad answer could ship with no safety net |

## The pattern

The "no" rows are the ones that decide **what is true** (rows 1 to 7) or **what leaves the
machine** (row 9). The one "yes" row only decides **how it is worded** (row 8). The facts are
computed by code first, then handed to the model, which never gets to change them.

## Failure modes I have already seen

- A reply cut off by `max_tokens` with no error: the tool noticed through `stop_reason` and
  used the template.
- A model that miscounted five words and noticed itself, which is why counts stay in code.

## Failure modes I have not guarded against yet

- The summary could state a number that disagrees with the table. Nothing checks it.
- Finding text could contain instructions. It is fenced as data in the prompt, but that
  reduces the risk and does not remove it.
- A loop that never ends, partial work reported as complete, and runaway cost only appear
  once there is a loop (Session 10), so the harness will need step and token limits.
