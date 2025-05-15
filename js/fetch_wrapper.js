/**
 * fetch_wrapper.js
 * Author: Jeremy Tarkington
 *
 * A reusable fetch wrapper with:
 * - Automatic retries
 * - Timeout support
 * - Auto JSON response parsing
 * - Basic error handling
 *
 * Example usage:
 *   const result = await fetchWithRetry("https://api.example.com/data", { method: "GET" });
 */

function fetchWithRetry(url, options = {}, retries = 3, timeout = 5000) {
  return new Promise((resolve, reject) => {
    const controller = new AbortController();
    const { signal } = controller;
    const opts = { ...options, signal };

    const timer = setTimeout(() => {
      controller.abort();
    }, timeout);

    const attemptFetch = (attempt) => {
      fetch(url, opts)
        .then((response) => {
          clearTimeout(timer);
          if (!response.ok) {
            throw new Error(`HTTP ${response.status} - ${response.statusText}`);
          }
          return response.json();
        })
        .then((data) => resolve(data))
        .catch((error) => {
          if (attempt < retries) {
            console.warn(`Retry ${attempt}/${retries} for: ${url}`);
            setTimeout(() => attemptFetch(attempt + 1), 1000 * attempt);
          } else {
            reject(error);
          }
        });
    };

    attemptFetch(1);
  });
}

// === Example Usage ===
// fetchWithRetry("https://jsonplaceholder.typicode.com/posts/1")
//   .then(data => console.log(data))
//   .catch(err => console.error("Fetch failed:", err));

export default fetchWithRetry;
