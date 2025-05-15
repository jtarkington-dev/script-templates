# Changelog

All notable changes to this project will be documented in this file.
This project follows semantic versioning and tracks script, agent, and documentation improvements across all supported languages.

---

## \[1.0.0] - 2025-05-15

### Added

- Initial release of cross-language script template system
- Python templates: CLI, scheduler, logging, API, threading, data cleaning, retry
- JavaScript utilities: debounce, fetch, DOM logger, local storage, clipboard, form serializer, UUID
- PowerShell scripts: file cleanup, backup, service checks, info export
- Bash scripts: cleanup, backup, service check, system info, log archiving
- Java templates: CLI menu, JSON loader, file backup, HTTP client, retry executor, system reporter
- Modular AI agent architecture with 5 agents:

  - `basic_agent_template.py`
  - `gpt_agent_template.py`
  - `task_runner_agent.py`
  - `system_monitor_agent.py`
  - `pandas_analyst_agent.py`

- `agent_architecture.md` and `how_to_use.md` documentation
- Root-level `README.md`, `LICENSE`, and `CONTRIBUTING.md`

### Structure

- Project organized by language with one folder per type
- Agent folders match purpose (e.g., `automation/`, `monitoring/`, `gpt/`)
- Each folder includes its own `README.md`

---

## Future

- Add orchestrator examples for routing between agents
- Add GUI version of script dashboard (Streamlit or web)
- Expand agents to include shell command interpreter and web scraping support
