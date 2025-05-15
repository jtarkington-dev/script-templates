/**
 * uuid_generator.js
 * Author: Jeremy Tarkington
 *
 * Generates a UUID v4 (random) string using native crypto APIs.
 * - RFC4122 compliant
 * - No dependencies
 * - Works in browser and Node.js
 */

function generateUUIDv4() {
  // Use crypto API from Node or browser
  const cryptoObj = typeof crypto !== "undefined" ? crypto : require("crypto");

  const bytes = cryptoObj.getRandomValues
    ? cryptoObj.getRandomValues(new Uint8Array(16))
    : cryptoObj.randomBytes(16);

  // RFC4122 version 4 bits:
  bytes[6] = (bytes[6] & 0x0f) | 0x40; // Set version to 0100
  bytes[8] = (bytes[8] & 0x3f) | 0x80; // Set variant to 10xx

  const hex = [...bytes].map(b => b.toString(16).padStart(2, "0"));

  return [
    hex.slice(0, 4).join(""),
    hex.slice(4, 6).join(""),
    hex.slice(6, 8).join(""),
    hex.slice(8, 10).join(""),
    hex.slice(10, 16).join("")
  ].join("-");
}

// === Example Usage ===
// console.log(generateUUIDv4());

export default generateUUIDv4;
