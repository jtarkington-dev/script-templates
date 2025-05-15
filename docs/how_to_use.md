# How to Use This Repository

This repo is a structured, multi-language template collection for automation, scripting, and agent-based tooling. It’s designed to help you:

- Write consistent and reusable scripts in Python, JavaScript, Bash, PowerShell, and Java
- Deploy modular AI agents in real-world automation flows
- Build dashboards, assistants, or schedulers without starting from scratch

---

## 🔄 Folder Overview

| Folder        | Purpose                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| `python/`     | CLI tools, automation routines, agents, decorators, threading, and logging         |
| `javascript/` | Browser-based utilities: debounce, fetch wrappers, localStorage helpers, DOM tools |
| `bash/`       | Linux/macOS shell scripts for cleanup, backup, and system info exports             |
| `powershell/` | Windows-native scripts for system automation, backup, service checking             |
| `java/`       | Menu-driven apps, JSON IO, backup tools, HTTP utilities                            |
| `agents/`     | Modular AI agents for task routing, monitoring, data analysis, and automation      |

---

## ✅ Getting Started

Clone the repository and choose the folder/language you need:

```bash
git clone https://github.com/jtarkington-dev/code-templates.git
cd code-templates
```

Then navigate to the script or agent you want to use.

---

## 📊 Agent Use (Python)

If you're using the agents:

1. Install dependencies:

```bash
pip install openai pandas requests streamlit rich
```

2. Run an agent:

```python
from automation.task_runner_agent import TaskRunnerAgent
result = TaskRunnerAgent().run("Build a simple backup system")
print(result)
```

3. Integrate agents into a Streamlit dashboard or CLI.

For architecture details, see `agent_architecture.md`.

---

## 📄 Running Scripts (Examples)

**Python:**

```bash
python data_cleaning_template.py --input data.csv --output cleaned.csv
```

**JavaScript (Frontend in browser):**

```html
<script type="module">
  import debounce from "./debounce_function.js";
</script>
```

**Bash:**

```bash
chmod +x delete_old_files.sh
./delete_old_files.sh /var/log 30
```

**PowerShell:**

```powershell
.\export_system_info.ps1 -OutFile "C:\temp\sysinfo.txt"
```

**Java:**

```bash
javac ConsoleAppMenu.java
java ConsoleAppMenu
```

---

## 🛠️ Extending This Repo

You can extend this project by:

- Creating new script types and adding a README in each folder
- Adding more agents and wiring them into a router/orchestrator
- Combining shell scripts + agents for hybrid automation stacks

All code is written to be copy-friendly and modular.

---

## 👤 Author

Maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)
