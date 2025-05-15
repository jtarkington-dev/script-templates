# Agents Directory

This folder contains a set of modular, prompt-based AI agents written in Python. These agents are designed to act as intelligent helpers, components of larger systems, or reusable modules for automation pipelines and dashboards.

Each agent has a defined role and behavior. Agents are designed to be:

- Stateless or lightweight stateful
- Plug-and-play with core orchestrators
- Reusable in CLI tools, Streamlit dashboards, or async workers

---

## 🤖 Agent Templates

| File                      | Folder        | Description                                                                                                                     |
| ------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `basic_agent_template.py` | `base/`       | A foundational agent class or script that defines common logic and a callable structure. Start here for creating custom agents. |
| `gpt_agent_template.py`   | `gpt/`        | Base class for GPT-powered agents using OpenRouter or OpenAI-compatible APIs. Handles prompt sending, temperature, and parsing. |
| `task_runner_agent.py`    | `automation/` | General-purpose execution agent. Parses a user-defined goal and returns a step-by-step plan or suggestions.                     |
| `system_monitor_agent.py` | `monitoring/` | Agent that analyzes system information and suggests diagnostics, health checks, or risk alerts.                                 |
| `pandas_analyst_agent.py` | `pandas/`     | Data-focused agent that reads a DataFrame and returns summaries, anomalies, or chart-ready analysis. Ideal for dashboards.      |

---

## ✅ Requirements

All agents are written in Python 3.9+ and designed to work with a modular orchestrator or CLI shell.

### Core Libraries

```bash
pip install openai pandas requests
```

If using agents in a dashboard or CLI assistant, also install:

```bash
pip install streamlit rich
```

---

## 🧠 How They're Used

Each agent contains a `.run(input)` or `.invoke(prompt)` method depending on implementation. Some take additional context or config.

They are typically used like this:

```python
from automation.task_runner_agent import TaskRunnerAgent

task = "Set up a backup system on Ubuntu"
response = TaskRunnerAgent().run(task)
print(response)
```

---

## 🔄 Integration Ideas

These agents can be:

- Plugged into a CLI assistant
- Called from a Streamlit dashboard panel
- Combined with a router to form an autonomous multi-agent system
- Used to wrap LLM calls with validation, formatting, and prompts

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)
