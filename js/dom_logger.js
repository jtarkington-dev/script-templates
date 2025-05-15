/**
 * dom_logger.js
 * Author: Jeremy Tarkington
 *
 * Appends log messages to a DOM container (plus console).
 * Supports:
 * - Log levels: info, warn, error
 * - Auto-scroll to bottom
 * - Optional timestamp
 */

class DOMLogger {
  constructor(containerId = "log", showTimestamps = true) {
    this.logContainer = document.getElementById(containerId);
    if (!this.logContainer) {
      console.warn(`DOMLogger: Container #${containerId} not found.`);
      return;
    }

    this.showTimestamps = showTimestamps;
  }

  _formatMessage(level, message) {
    const timestamp = this.showTimestamps
      ? `[${new Date().toLocaleTimeString()}] `
      : "";
    return `${timestamp}<strong>[${level.toUpperCase()}]</strong> ${message}`;
  }

  _appendToDOM(formattedHtml) {
    const line = document.createElement("div");
    line.innerHTML = formattedHtml;
    this.logContainer.appendChild(line);
    this.logContainer.scrollTop = this.logContainer.scrollHeight;
  }

  info(message) {
    console.info(message);
    if (this.logContainer) this._appendToDOM(this._formatMessage("info", message));
  }

  warn(message) {
    console.warn(message);
    if (this.logContainer) this._appendToDOM(this._formatMessage("warn", message));
  }

  error(message) {
    console.error(message);
    if (this.logContainer) this._appendToDOM(this._formatMessage("error", message));
  }
}

// === Example Setup ===
// <div id="log" style="height: 200px; overflow-y: auto; font-family: monospace;"></div>
// const logger = new DOMLogger();
// logger.info("Loaded successfully");

export default DOMLogger;
