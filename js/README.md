# JavaScript Utility Templates

This folder contains a curated set of JavaScript utility modules for browser-based development and frontend tooling. Each script is written in clean ES6+ syntax, well-documented, and designed to drop directly into your project.

Whether you're working with user input, DOM manipulation, local storage, or building frontend tools, these utilities are designed to solve the common headaches fast.

---

## 📂 Included Utilities

| File                      | Description                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------ |
| `debounce_function.js`    | Debounce wrapper to delay execution until user stops triggering the event            |
| `fetch_wrapper.js`        | A retryable `fetch` wrapper with timeout and auto JSON parsing                       |
| `uuid_generator.js`       | Dependency-free UUID v4 generator (RFC-compliant) using `crypto` APIs                |
| `dom_logger.js`           | Stream logs to a DOM element with timestamps and console sync                        |
| `form_serializer.js`      | Convert form inputs to a clean JSON object, including checkbox groups                |
| `clipboard_util.js`       | Copy text to clipboard using modern API or fallback to `<textarea>`                  |
| `event_delegate.js`       | Lightweight event delegation utility that works on dynamically added elements        |
| `local_storage_helper.js` | Store, retrieve, and remove JSON from `localStorage` safely                          |
| `throttle_function.js`    | Limit function execution to once per interval (throttling) for high-frequency events |

---

## ✅ Requirements

All scripts are written in plain ES6+ JavaScript and work in modern browsers.

### 🌟 No External Dependencies

You don’t need to install anything. These scripts are 100% standalone. Just import them into your HTML or ES module setup:

```html
<script type="module">
  import copyToClipboard from "./clipboard_util.js";
  copyToClipboard("Hello, world!");
</script>
```

Or attach them to a `<script type="module">` in your project.

---

## ▶️ Example Use Cases

- **`debounce_function.js`**: Add to any search box or input listener
- **`form_serializer.js`**: Submit full forms as JSON to APIs or save states
- **`dom_logger.js`**: Great for web dashboards, console mirroring, or AI UI overlays
- **`event_delegate.js`**: Efficient listener for dynamic UIs (e.g., a todo list)
- **`throttle_function.js`**: Smooth scroll performance handlers

---

## 🔄 Why These Exist

Frontend apps often repeat the same small tasks: copying to clipboard, throttling scroll events, debouncing input, storing JSON safely. These templates give you a head start:

- No libraries or frameworks required
- Browser-safe and optimized
- Built from practical, repeat-use patterns

These aren’t generic snippets — they’re purpose-built for real frontend work.

---

## 👤 Maintainer

Created and maintained by **Jeremy Tarkington**
GitHub: [jtarkington-dev](https://github.com/jtarkington-dev)

---

## 📅 Explore Other Folders

- `python/` — CLI tools, automation agents, schedulers, and data cleaners
- `java/` — File utilities, menu-driven apps, JSON and HTTP clients
- `bash/` — Unix shell scripts for backup, cleanup, and logging
- `powershell/` — Windows scripting for IT, cleanup, and automation
