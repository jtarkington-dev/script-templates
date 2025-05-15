# Python Script Templates

Welcome to the Python section of this multi-language template repository. This folder contains a full collection of useful, real-world Python scripts and starter modules designed to accelerate your workflow. Whether you're building a CLI tool, a threaded worker, a scheduled job, or just need better logging and retry logic, these templates will save you time and help you stay consistent.

Each script is written for Python 3.8+, includes comments and usage examples, and is structured in a way that's easy to extend or drop into existing projects.

---

## 📂 Included Templates

| File                        | Description                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| `cli_script_template.py`    | Command-line script with `argparse`, logging, exception handling, and testable main() method   |
| `logging_template.py`       | Configurable logger with verbosity control and rotating file support                           |
| `retry_decorator.py`        | Decorator that retries a function on failure, with optional exponential backoff and logging    |
| `json_loader.py`            | Safely load and save JSON files with defaults and error handling built-in                      |
| `main_with_test_mode.py`    | Template for scripts that support --test and --live modes with clearly separated logic blocks  |
| `threaded_worker.py`        | Multithreaded task queue using `queue.Queue` and named worker threads                          |
| `schedule_task.py`          | Task runner that schedules functions to run at intervals using the `schedule` library          |
| `api_request_template.py`   | HTTP wrapper using `requests` with retry logic, headers, timeouts, and JSON response parsing   |
| `data_cleaning_template.py` | Cleans CSV data with `pandas`: nulls, types, column normalization, and export                  |
| `class_template.py`         | Base class structure with config, actions, and string representation for larger apps or agents |

---

## ✅ Requirements

These templates are written for **Python 3.8 or newer**. They are modular, so you only need to install packages based on which scripts you want to use.

### 📆 Core Dependencies

Install everything needed for full use:

```bash
pip install pandas schedule requests
```

> • `pandas` is used in `data_cleaning_template.py`
> • `schedule` is used in `schedule_task.py`
> • `requests` is used in `api_request_template.py`

No script uses external packages that aren't listed above.

---

## ▶️ How to Run the Scripts

Each script can be run directly:

```bash
python cli_script_template.py --input "hello world" --verbose
python main_with_test_mode.py --test
python schedule_task.py
python data_cleaning_template.py --input raw.csv --output cleaned.csv
```

All scripts are fully standalone and log clean output to your terminal or optionally to a file.

---

## 🔄 Why These Matter

These templates were built based on real-world scripting patterns: handling flaky APIs, building repeatable CLI tools, automating agents with scheduled runs, and cleaning messy CSVs for downstream automation.

They help you:

- Avoid repeating boilerplate code
- Build scripts that are debuggable, loggable, and extendable
- Prototype ideas fast without sacrificing good structure

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)

---

## 📅 Explore Other Script Sets

- `javascript/` — Utilities for DOM interaction, input handling, storage, and clipboard use
- `bash/` — Shell scripts for cleaning, backup, system tasks
- `powershell/` — Windows automation scripts for admins
- `java/` — Backup tools, JSON I/O, HTTP client, and CLI app templates
