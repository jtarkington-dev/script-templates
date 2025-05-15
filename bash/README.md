# Bash Script Templates

This folder contains a set of practical Bash scripts designed for system automation, backups, service checks, log handling, and general Unix/Linux task management. These are real-world utilities meant to run in production environments with minimal modification.

Each script is written for portability, using common POSIX-compatible commands and syntax. They are useful for sysadmins, DevOps engineers, and anyone maintaining Linux-based systems.

---

## 📂 Included Scripts

| File                    | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| `delete_old_files.sh`   | Deletes files older than X days from a given directory using `find`    |
| `backup_folder.sh`      | Copies a folder to a timestamped backup location using `cp` or `rsync` |
| `archive_logs.sh`       | Compresses `.log` files in a directory into a single ZIP archive       |
| `service_checker.sh`    | Checks if a systemd service is running and restarts it if necessary    |
| `export_system_info.sh` | Outputs basic system information: OS, CPU, memory, disk, uptime        |

---

## ✅ Requirements

These scripts require:

- A Unix-like OS (Linux, macOS, WSL)
- Standard GNU core utilities: `find`, `cp`, `zip`, `systemctl`, `df`, `free`, etc.

> Optional: `zip` must be installed for `archive_logs.sh`.

All scripts are POSIX-compliant unless otherwise noted.

---

## ▶️ How to Use

Make the script executable and run it with the required parameters:

```bash
chmod +x delete_old_files.sh
./delete_old_files.sh /var/log 30
```

Each script includes inline comments and clearly marked variables so you can customize them for your system.

---

## 🔄 Use Cases

These Bash scripts are ideal for:

- Cron jobs (automated cleanup or backups)
- Emergency recovery tasks
- System provisioning
- Lightweight server automation

They're especially useful on headless Linux servers or minimal distros.

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)

---

## 📅 Explore More Templates

- `python/` — Automation agents, data tools, CLI wrappers
- `javascript/` — DOM utilities, input handling, browser-side tools
- `powershell/` — Windows-focused scripting for sysadmin tasks
- `java/` — Console apps, JSON I/O, HTTP utilities, file automation
