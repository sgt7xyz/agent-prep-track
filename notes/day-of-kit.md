# Day-of kit: AI Agents in Production, Mon Oct 19

_One page. Doors 7:30, programming 9:00 to 5:30. Fill the [brackets] on Saturday night._

## Before you leave
- [ ] Paid Claude subscription works on the account you'll sign in with (check tonight, not at 8:55)
- [ ] Claude Code / VS Code open, repo cloned, `uv run pytest` passes
- [ ] API key in an untracked env file, phone tethering tested (conference wifi is bad)
- [ ] Charger, this page open, `notes/00-baseline.md` re-read, `docs/PROJECT.md` in a tab
- [ ] One markdown file open for notes. Don't start a clever system

## Your 90-second intro (about 170 words, say it out loud three times)
> I'm Steven. I run sgt7, a small cloud security and DevSecOps practice for small and mid-sized businesses in the Triangle. I'm an Army veteran with an AWS and GCP background.
>
> This week I built **Posture Brief Lite**. It takes cloud misconfiguration findings and writes a plain-English remediation brief for a business owner, mapped to CIS and NIST. The mapping and severity are plain code, so they're reproducible for an audit. Only the owner-facing prose uses a model. [By Monday add what's true: a hand-built agent loop? an MCP server over stdio?]
>
> What I'm stuck on is **[pick one that's still true: how to tell an agent got worse after a change / which identity the agent should run as / where the human approval gate belongs]**. I'd like to hear how people handle that in production.

## Terms in plain English
| Term | Means |
|---|---|
| Agent | A model in a loop with tools and a stopping condition, where the model picks the next step |
| Harness | The code around the model: runs the loop, tools, budgets, logging |
| Context engineering | Deciding what goes in the context window each turn, like budgeting a resource |
| MCP | Open standard for connecting agents to tools and data. Now stateless (July 2026) |
| A2A | Protocol for agents to hand tasks to agents they don't own |
| Skill | A folder with SKILL.md. Only the short description loads until it's needed |
| Drift | Behavior changing with no code change: model, prompt, tool schema or data moved |
| Eval | A test set that catches agent regressions unit tests can't |
| Prompt injection | Untrusted text (a file, a ticket, a finding) treated as instructions |
| Lethal trifecta | Private data + untrusted content + outside communication in one agent |
| Workload identity | A non-human identity for the agent, with short-lived scoped credentials |

## Questions to ask
**Yours (from your baseline):**
1. What are the real failure modes of an agent, and which should I worry about first?
2. What's the difference between a prompt and a context?
3. When do I need A2A instead of just calling a tool?
4. How would I measure that a change made the agent worse?
5. What does a month of running this actually cost?

**From the plan, best fits for your background:**
- On AWS, what identity does your agent use in production, and how short-lived are its credentials?
- A wrong but plausible result goes unnoticed for a week. What's your incident process with no stack trace?
- What are you telling clients to keep agents away from entirely right now?
- What does agent governance look like at a 20-person company, not a 2,000-person one?

**Questions I only know to ask now (add after Sat):** [ ] [ ] [ ]

## What to listen for, by block
_Order from the plan's coverage map. Check it against the real agenda._
| Block | Listen for |
|---|---|
| What an agent is; probabilistic vs deterministic | Where *they* draw the line. Does it match "push determinism to the edges"? |
| Harnesses | What the loop guards against (steps, tokens, cost). Compare to your own loop |
| Context engineering | What gets compacted or dropped, and how they measure the loss |
| MCP and A2A | What broke in real deployments after the stateless change; who actually uses A2A |
| Skills | Skill vs tool decisions; the supply-chain story for skills you didn't write |
| Memory | The write policy: who owns what gets remembered |
| Patterns | When they collapsed a multi-agent design back into one agent, and the tell |
| Drift, observability, evals | What they log, how big their eval set is, how they stop it rotting |
| Security and identity | Your home ground. Compare to your IAM instincts: roles, OIDC, least privilege, audit |
| Sovereignty, tokenomics | Real cost per outcome; where local models fail (tool calling) |
| Ethics, 2027 | Who is accountable when it's wrong. What they expect to look naive by end of 2027 |

**Rule for the day:** write the term you don't know, then keep listening. Ask at the break.
