# LangGraph vs n8n

This document compares **LangGraph** and **n8n**, focusing on what they have in common, how they differ, and when you should choose one over the other.

Although both are often described as “workflow tools,” they solve **very different problems**.

---

## 1. High-level overview

| Tool | What it is |
|----|-----------|
| **LangGraph** | A framework for building **stateful, multi-step LLM agents** using code |
| **n8n** | A **general-purpose automation platform** for connecting services and APIs |

In short:

- **LangGraph** answers: *“How should my AI think, decide, and retry?”*
- **n8n** answers: *“When X happens, what systems should run next?”*

---

## 2. Mental model

### LangGraph

```

START
↓
Planner (LLM)
↓
Executor (tool / LLM)
↓
Critic
├── retry → Planner
└── success → END

```

- Focused on **reasoning**
- Explicit loops and conditions
- Shared, persistent state
- Code-driven

---

### n8n

```

Trigger (Webhook / Cron)
↓
Fetch Data (API)
↓
Process / Transform
↓
Send Result (Slack / Email / DB)

```

- Focused on **automation**
- Event-driven
- Mostly linear flows
- UI-driven (low-code)

---

## 3. What they have in common

Despite their differences, LangGraph and n8n share some surface similarities:

### ✅ Similarities

- Both define workflows as **nodes connected by edges**
- Both support **conditional branching**
- Both can call **APIs and external services**
- Both can include **LLM steps**
- Both can be part of larger systems

However, these similarities are mostly structural — the intent is very different.

---

## 4. Key differences (core idea)

### Primary purpose

| Aspect | LangGraph | n8n |
|----|---------|----|
| Core goal | Control LLM reasoning | Automate systems |
| Primary user | AI / ML engineers | DevOps, product, ops |
| Main abstraction | State + graph | Event + workflow |
| Execution style | Stateful, iterative | Event-driven |

---

## 5. Comparison table

| Aspect | LangGraph | n8n |
|------|-----------|-----|
| Primary focus | LLM agents | Automation |
| Interface | Code (Python / TS) | Visual UI |
| State handling | Explicit, shared state | Limited / per-node |
| Loops & retries | First-class | Basic |
| Conditional logic | Code-level control | UI-level rules |
| Multi-agent support | Native | Not designed for it |
| Debugging | Code-level, explicit | UI logs |
| Integrations | You build them | Many built-in |
| Best for production AI | Yes | Limited |
| Learning curve | Higher | Lower |

---

## 6. LLM usage differences

### LangGraph + LLMs

- LLMs are **core**
- Used for:
  - Planning
  - Decision making
  - Evaluation
  - Tool selection
- LLM failures are expected and handled (retry, critique, loop)

### n8n + LLMs

- LLMs are **optional**
- Usually used for:
  - Summarization
  - Classification
  - Simple generation
- Typically one-shot calls
- Limited retry and reasoning control

---

## 7. When to use LangGraph

Use **LangGraph** when:

- You are building **AI agents**
- You need **multi-step reasoning**
- You need **retry / validation / critics**
- You care about **correctness and determinism**
- You want **explicit control over state**
- You are moving toward **production AI systems**

Example use cases:
- Research agents
- Coding agents
- Planning + execution systems
- Multi-agent collaboration

---

## 8. When to use n8n

Use **n8n** when:

- You are automating workflows
- You need to connect many services quickly
- You want minimal code
- AI is just **one step** in the flow
- Non-engineers need to modify workflows

Example use cases:
- GitHub → Slack automation
- Cron-based reports
- Data syncing between tools
- Simple AI-powered summaries

---

## 9. Using them together (very common)

LangGraph and n8n are **not competitors**.

A common architecture:

```

n8n (trigger, schedule, integrations)
↓
LangGraph API (reasoning-heavy AI agent)
↓
n8n (notifications, storage, follow-up actions)

```

- n8n handles **when things happen**
- LangGraph handles **how the AI thinks**

---

## 10. Summary

- **LangGraph** = AI reasoning engine
- **n8n** = automation glue

If your problem is:
- *“How should this AI reason step-by-step?”* → **LangGraph**
- *“How do these systems connect?”* → **n8n**

In modern stacks, it’s common (and smart) to use **both**.

---
```




