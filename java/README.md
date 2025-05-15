# Java Script Templates

Welcome to the Java folder of this multi-language template repo. This section is focused on providing clean, practical Java utilities and console app scaffolds that can be reused across many types of projects — from CLI tools and agents to basic file operations and HTTP clients.

Each script is fully documented, designed to run out-of-the-box (with minimal setup), and demonstrates clear Java patterns that are both educational and production-friendly.

---

## 📂 Included Templates

| File                      | Description                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| `MainTemplate.java`       | Basic Java console entry point — useful for all standalone testing or bootstrapping            |
| `ConsoleAppMenu.java`     | Interactive menu-driven CLI with input handling using `Scanner` and a `while` loop             |
| `FileBackupUtility.java`  | Safely backs up files or entire folders into a timestamped directory                           |
| `JsonLoader.java`         | Loads and saves structured data as JSON using Google's `Gson` library                          |
| `SimpleHttpClient.java`   | Makes HTTP GET and POST requests using Java 11's `HttpClient`, with header support and logging |
| `SystemInfoReporter.java` | Prints out basic OS, CPU, memory, and uptime info from the local JVM and system                |
| `RetryExecutor.java`      | A retry wrapper for unstable or fail-prone operations, with configurable retry count and delay |

---

## ✅ Requirements & Setup

These templates assume you're using **Java 11 or later**. If you're still on Java 8, upgrade to access `HttpClient`, lambda syntax, and newer utilities.

### ⚡ JDK Version

- Java 11 or higher recommended
- Java 17 LTS is also fully compatible

### 📆 External Libraries

Only one script requires a third-party library:

#### Gson (for `JsonLoader.java`)

Google's Gson is used to parse and write JSON config files.

**Option 1: Maven dependency**

```xml
<dependency>
  <groupId>com.google.code.gson</groupId>
  <artifactId>gson</artifactId>
  <version>2.10.1</version>
</dependency>
```

**Option 2: Download manually**
Get the JAR directly from [Gson releases](https://github.com/google/gson/releases) and add it to your classpath.

---

## ▶️ How to Compile and Run

Each file can be compiled and run individually using `javac` and `java`:

```bash
javac FileBackupUtility.java
java FileBackupUtility /path/to/source /path/to/backup_root
```

For `JsonLoader.java`, make sure the Gson JAR is on your classpath:

```bash
javac -cp gson-2.10.1.jar JsonLoader.java
java -cp .:gson-2.10.1.jar JsonLoader
```

> On Windows, replace `:` with `;` in the classpath.

---

## 🔄 Suggested Usage

These scripts are designed to be:

- Dropped into any Java project as utility classes or starting points
- Extended with your own logic or wrapped inside larger tools
- Educational templates for learning Java's built-in features

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)

---

## 📅 Other Folders in This Repo

- `python/` — Agent templates, CLI tools, automation scripts
- `javascript/` — Frontend utilities and DOM logic
- `bash/` — Shell scripts for system automation
- `powershell/` — Windows-based scripting for sysadmin and automation tasks
