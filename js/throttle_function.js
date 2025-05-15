/**
 * throttle_function.js
 * Author: Jeremy Tarkington
 *
 * A reusable throttle utility that ensures a function is only
 * called once every X milliseconds — regardless of how often it's triggered.
 *
 * Useful for: scroll, mousemove, window resize, etc.
 *
 * Example:
 *   const throttled = throttle(updateUI, 100);
 *   window.addEventListener("scroll", throttled);
 */

function throttle(func, delay = 300) {
  let lastCall = 0;
  let timeoutId = null;

  return function (...args) {
    const now = Date.now();
    const timeSinceLast = now - lastCall;

    if (timeSinceLast >= delay) {
      lastCall = now;
      func.apply(this, args);
    } else if (!timeoutId) {
      // Ensure the last trigger is captured
      timeoutId = setTimeout(() => {
        lastCall = Date.now();
        timeoutId = null;
        func.apply(this, args);
      }, delay - timeSinceLast);
    }
  };
}

// === Example Usage ===
// const onScroll = throttle(() => console.log("Throttled scroll"), 200);
// window.addEventListener("scroll", onScroll);

export default throttle;
