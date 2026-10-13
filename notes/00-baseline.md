# Baseline

## What is an agent, as distinct from a workflow or a chatbot?

An agent is an AI system that can make decisions, use tools, and take actions to complete a task. A chatbot mainly responds to questions, while a workflow follows a predefined set of steps. An agent is different because it can figure out what steps to take based on the situation and adjust its approach as needed.

## What is an agent harness?

An agent harness is the system that supports and controls an AI agent. It handles things like giving the agent access to tools, managing its memory and context, setting permissions, and keeping track of what it's doing. Basically, it's the environment that allows the agent to operate.

## What does MCP give you that an API key and an SDK do not?

MCP (Model Context Protocol) provides a standard way for AI agents to connect to different tools and services. An API key provides authentication, and an SDK helps developers interact with a specific service. MCP makes it easier for agents to discover and use tools without having to build a separate integration for every service.

## Name three agent failure modes that are not exceptions?

Need to learn this.

## What is context engineering?

I am aware of prompt engineering, but context engineering is a new term to me, so I need to learn this.

## What is a skill?

A skill is a reusable set of instructions that teaches an agent how to perform a particular task. For example, an agent could have a skill for reviewing Terraform code, troubleshooting Kubernetes, or generating reports. Instead of explaining the process every time, the agent can use the skill when needed.

## What is A2A for?

Still need to learn this.

## How would you tell if an agent regressed?

Still need to learn this.

## What identity does an agent use to call AWS?

Ideally, an agent should use an IAM role with temporary credentials rather than permanent AWS access keys. The role should follow the principle of least privilege, meaning the agent only gets the permissions it actually needs. I would also want its actions logged through CloudTrail so there's an audit trail.

## What does an agent cost to run?

I have a general idea based upon tokens etc. but honestly I still need to learn more about this.

## Five open questions

1. What are the real failure modes of an agent, and which one should I worry about first?
2. What is the difference between a prompt and a context?
3. When do I need A2A instead of just calling a tool?
4. How would I measure that a change made the agent worse?
5. What does a month of running this actually cost?

_Revisit on Oct 18. Cross out what I can now answer, and add the questions I only know to ask now._
