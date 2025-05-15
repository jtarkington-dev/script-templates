# PowerShell Script Templates

This folder contains a collection of practical PowerShell script templates focused on system administration, automation, and Windows task routines. These scripts are production-ready, reusable, and designed to minimize boilerplate when you're automating common admin tasks.

Whether you're backing up files, checking services, exporting system info, or cleaning up old data — these scripts let you focus on execution, not syntax.

---

## 📂 Included Scripts

| File                     | Description                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `delete_old_files.ps1`   | Deletes files older than a given number of days from a target directory |
| `backup_folder.ps1`      | Copies a folder to a timestamped backup directory with logging          |
| `archive_logs.ps1`       | Compresses all `.log` files in a folder into a ZIP archive              |
| `service_checker.ps1`    | Checks if a Windows service is running and restarts it if not           |
| `export_system_info.ps1` | Gathers basic system info and exports it to a text file                 |

---

## ✅ Requirements

These scripts require:

- Windows 10 or later
- PowerShell 5.1 or higher (most are compatible with PowerShell Core)
- No external modules needed

All scripts are portable and self-contained.

---

## ▶️ How to Use

Run a script in PowerShell by navigating to the folder and executing:

```powershell
.ackup_folder.ps1 -SourcePath "C:\MyData" -DestinationRoot "D:\Backups"
```

Each script includes parameter validation, console output, and inline comments so you can customize it easily for your environment.

---

## 🔄 What These Are For

These templates are designed to be reused by IT admins, help desk engineers, and automation developers. You can:

- Schedule them with Task Scheduler
- Drop them into system maintenance pipelines
- Expand them into larger automation routines

They’re built to be:

- Clean
- Readable
- Modular

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)

---

## 📅 Explore More

- `python/` — Agents, CLI apps, schedulers, and automation
- `javascript/` — Frontend utility modules and DOM scripting
- `bash/` — Cross-platform shell automation
- `java/` — Backup tools, menu apps, HTTP, and JSON utilities
