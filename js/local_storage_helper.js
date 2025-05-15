/**
 * local_storage_helper.js
 * Author: Jeremy Tarkington
 *
 * Wrapper for storing, retrieving, and removing JSON-safe data
 * from localStorage with fallbacks and default handling.
 */

const StorageHelper = {
  /**
   * Save an object or value as JSON to localStorage
   * @param {string} key
   * @param {any} value
   */
  setItem(key, value) {
    try {
      const json = JSON.stringify(value);
      localStorage.setItem(key, json);
    } catch (err) {
      console.error(`Failed to set localStorage item '${key}':`, err);
    }
  },

  /**
   * Retrieve and parse a JSON value from localStorage
   * @param {string} key
   * @param {any} defaultValue - fallback if key not found or invalid JSON
   * @returns {any}
   */
  getItem(key, defaultValue = null) {
    try {
      const raw = localStorage.getItem(key);
      if (raw === null) return defaultValue;
      return JSON.parse(raw);
    } catch (err) {
      console.warn(`Failed to parse localStorage item '${key}':`, err);
      return defaultValue;
    }
  },

  /**
   * Remove a localStorage item by key
   * @param {string} key
   */
  removeItem(key) {
    try {
      localStorage.removeItem(key);
    } catch (err) {
      console.error(`Failed to remove localStorage item '${key}':`, err);
    }
  },

  /**
   * Clear all keys in localStorage (use with caution)
   */
  clearAll() {
    try {
      localStorage.clear();
    } catch (err) {
      console.error("Failed to clear localStorage:", err);
    }
  }
};

// === Example Usage ===
// StorageHelper.setItem("user", { id: 1, name: "Jeremy" });
// const user = StorageHelper.getItem("user", {});
// StorageHelper.removeItem("user");

export default StorageHelper;
