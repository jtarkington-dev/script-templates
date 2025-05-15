# Code Templates Repository

Welcome to the **Code Templates Repository**, a complete multi-language toolkit of reusable scripts, automation modules, and AI agents. This repo is designed to save you time, help you stay consistent, and build production-ready tools faster — whether you’re automating tasks, building dashboards, or wiring together multi-agent systems.

---

## 🌐 What’s Inside

This project includes fully documented script templates across five languages and a complete modular agent system:

| Folder        | Purpose                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------- |
| `python/`     | CLI tools, logging, retries, data cleaners, and agent-ready classes                         |
| `javascript/` | Browser-side utilities like debounce, clipboard, DOM logging, fetch wrappers                |
| `bash/`       | Shell scripts for cleanup, backups, archiving, and system info exports                      |
| `powershell/` | Windows-native scripts for IT, file cleanup, service checks, and logs                       |
| `java/`       | Menu-driven apps, backup utilities, JSON config, and HTTP clients                           |
| `agents/`     | Modular AI agents (LLM/GPT powered) for automation, analysis, monitoring, and orchestration |

---

## ✅ Getting Started

Clone the repo:

```bash
git clone https://github.com/jtarkington-dev/code-templates.git
cd code-templates
```

Browse to the folder you want:

```bash
cd python
python cli_script_template.py --input "hello" --verbose
```

---

## 🧰 Agents Overview

The `agents/` system contains:

- A base agent interface
- Specialized LLM agents (GPT)
- Agents for pandas data analysis, system monitoring, and goal execution

Each agent has a `.run()` or `.invoke()` method and can be wired into a CLI, dashboard, or orchestrator.

For full design docs, see:

- [`agent_architecture.md`](agent_architecture.md)
- [`how_to_use.md`](how_to_use.md)

---

## 📊 Real-World Use Cases

- Automating file cleanups and backups on Linux/Windows
- Creating agents that interpret system info or analyze DataFrames
- Scheduling Python scripts and shell tasks
- Building toolkits with consistent CLI structure and logging
- Rapidly prototyping automation flows, dashboards, and assistants

---

## 🔄 Contributing

This repo is structured for modularity. You can:

- Add new scripts or agents in any language
- Extend existing ones
- Write your own orchestrator to route tasks across them

If you have a request or want to contribute, open an issue or PR.

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [@jtarkington-dev](https://github.com/jtarkington-dev)
