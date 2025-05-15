# Agent Architecture Overview

This document outlines the modular architecture used to design, implement, and coordinate AI agents across this project. The system is built around the idea of composable agents — each with a clearly defined purpose, prompt structure, and invocation method — so they can work independently or together as part of a broader automation system.

---

## 🧬 Core Design Principles

- **Single-responsibility**: Each agent performs one distinct role (e.g. analyzing data, generating steps, monitoring a system).
- **Modular**: Agents can be imported or swapped in and out easily, depending on the environment (CLI, dashboard, API).
- **Stateless by default**: Agents don’t retain memory between calls unless extended explicitly.
- **Orchestrator-aware**: All agents are built with integration in mind. They can be triggered by a router, command input, or system event.

---

## 🚀 Agent Types

### 1. **Base Agent (`basic_agent_template.py`)**

- Provides a minimal interface and response format
- Meant to be subclassed or used to define custom agents

### 2. **LLM-Powered Agent (`gpt_agent_template.py`)**

- Handles prompt construction and response parsing using OpenAI/OpenRouter APIs
- Controls model, temperature, system message, and JSON formatting

### 3. **Task Runner Agent (`task_runner_agent.py`)**

- Given a user task ("set up a backup system"), it generates high-level steps, subtasks, or shell command outlines

### 4. **System Monitor Agent (`system_monitor_agent.py`)**

- Reads a system info payload (RAM, CPU, disk, etc.) and returns warnings, risks, or suggestions

### 5. **Pandas Analyst Agent (`pandas_analyst_agent.py`)**

- Takes a `pandas.DataFrame`, a user question, and returns insights, summaries, or chart suggestions

---

## 🧮 Common Methods

Most agents expose one of the following methods:

```python
response = agent.run(input)
response = agent.invoke(prompt_dict)
```

Each agent defines its own `system_prompt`, `format`, and postprocessing structure.

---

## 🌐 Integration Options

Agents are designed to be plug-and-play in:

- ✅ Streamlit dashboards (visual interaction)
- ✅ CLI tools (e.g. `sys_assist.py`)
- ✅ Autonomous orchestrators (router dispatches request to agent)
- ✅ API endpoints or webhooks (modular execution)

---

## 🛠️ Agent Routing Architecture

A typical multi-agent system looks like this:

```text
[ user request ]
       |
     Router (intent classifier)
       |
  -----------------------------
  |    |      |      |       |
 Task  GPT  Monitor  Data  ...
Agent Agent Agent   Agent
```

Each agent handles one intent and returns a result in a standard format (`title`, `steps`, `summary`, `risk`, `output`, etc.).

---

## 📉 Output Schema (Flexible)

Agents generally return a dictionary with any of the following fields:

```json
{
  "title": "Recommended Steps for Linux Backup Setup",
  "steps": ["Install rsync", "Create cron job"],
  "summary": "This agent analyzed your input and proposed a simple 3-step setup.",
  "risks": ["No offsite backup detected."],
  "output": "rsync -av /home /mnt/backup"
}
```

Custom agents may return charts, markdown, tables, or shell commands as needed.

---

## 👤 Author

Architecture maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)
