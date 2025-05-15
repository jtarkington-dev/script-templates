/**
 * debounce_function.js
 * Author: Jeremy Tarkington
 *
 * A reusable debounce utility to delay function execution until
 * after a specified delay has passed without new calls.
 *
 * Useful for: input handlers, resize, scroll, auto-save, etc.
 *
 * Example:
 * const debouncedSearch = debounce(handleSearch, 300);
 * window.addEventListener("input", debouncedSearch);
 */

function debounce(func, delay = 300, immediate = false) {
  let timeout;

  const debounced = function (...args) {
    const context = this;

    const later = function () {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };

    const callNow = immediate && !timeout;

    clearTimeout(timeout);
    timeout = setTimeout(later, delay);

    if (callNow) func.apply(context, args);
  };

  // Optional methods for control
  debounced.cancel = function () {
    clearTimeout(timeout);
    timeout = null;
  };

  debounced.flush = function () {
    if (timeout) {
      func();
      clearTimeout(timeout);
      timeout = null;
    }
  };

  return debounced;
}

// === Example Usage ===
// const logInput = debounce((e) => console.log("Input:", e.target.value), 500);
// document.querySelector("input").addEventListener("input", logInput);

export default debounce;
