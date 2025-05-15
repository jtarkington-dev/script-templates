/**
 * clipboard_util.js
 * Author: Jeremy Tarkington
 *
 * Copies text to the clipboard using the Clipboard API (with fallback).
 * Works in modern browsers and gracefully degrades.
 *
 * Example:
 *   copyToClipboard("Hello World", () => alert("Copied!"));
 */

function copyToClipboard(text, onSuccess = null, onError = null) {
  // Modern API
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text)
      .then(() => {
        console.info("Copied to clipboard:", text);
        if (typeof onSuccess === "function") onSuccess();
      })
      .catch((err) => {
        console.warn("Clipboard API failed:", err);
        if (typeof onError === "function") onError(err);
      });
  } else {
    // Try using the deprecated execCommand as a fallback, but with a warning
    try {
      // Use the Clipboard API through a user interaction if possible
      const permissionStatus = navigator.permissions?.query({ name: 'clipboard-write' })
        .then(status => {
          if (status.state === 'granted' || status.state === 'prompt') {
            return navigator.clipboard.writeText(text)
              .then(() => {
                console.info("Copied to clipboard (permission fallback):", text);
                if (typeof onSuccess === "function") onSuccess();
              });
          } else {
            throw new Error("Clipboard permission denied");
          }
        })
        .catch(() => {
          throw new Error("Clipboard permission API not available");
        });

      // If the above fails or isn't supported, fall back to the textarea method
      if (!permissionStatus) {
        throw new Error("Using legacy fallback");
      }
    } catch (err) {
      // Legacy fallback using textarea
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";  // Avoid scrolling
      textarea.style.opacity = 0;
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();

      try {
        // Using execCommand with a console warning about deprecation
        console.warn("Using deprecated document.execCommand('copy') as fallback");
        const success = document.execCommand("copy");
        if (success) {
          console.info("Copied to clipboard (legacy fallback):", text);
          if (typeof onSuccess === "function") onSuccess();
        } else {
          throw new Error("Legacy fallback copy failed.");
        }
      } catch (innerErr) {
        console.error("All clipboard copy methods failed:", innerErr);
        if (typeof onError === "function") onError(innerErr);
      } finally {
        document.body.removeChild(textarea);
      }
    }
  }
}

// === Example Usage ===
// copyToClipboard("Copied text!", () => alert("Copied!"));

export default copyToClipboard;
