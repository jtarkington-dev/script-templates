/**
 * event_delegate.js
 * Author: Jeremy Tarkington
 *
 * Adds event delegation to a container element.
 * - One listener for many dynamic children
 * - Matches selector within container
 * - Supports multiple event types
 *
 * Example:
 *   delegateEvent("#list", "click", "button.delete", (e, target) => { ... });
 */

function delegateEvent(containerSelector, eventType, targetSelector, handler) {
  const container = typeof containerSelector === "string"
    ? document.querySelector(containerSelector)
    : containerSelector;

  if (!container) {
    console.warn(`delegateEvent: container "${containerSelector}" not found.`);
    return;
  }

  container.addEventListener(eventType, (event) => {
    const targets = container.querySelectorAll(targetSelector);
    for (const el of targets) {
      if (el.contains(event.target) || el === event.target) {
        handler(event, el);
        break;
      }
    }
  });
}

// === Example Usage ===
// HTML:
// <ul id="list">
//   <li><button class="delete">Delete</button></li>
//   <li><button class="delete">Delete</button></li>
// </ul>

// JS:
// delegateEvent("#list", "click", "button.delete", (e, button) => {
//   button.closest("li").remove();
// });

export default delegateEvent;
