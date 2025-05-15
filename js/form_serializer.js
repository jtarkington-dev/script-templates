/**
 * form_serializer.js
 * Author: Jeremy Tarkington
 *
 * Converts an HTML form into a JSON object.
 * Handles:
 * - Text inputs, selects, checkboxes, radios
 * - Multiple fields with the same name (e.g. checkboxes)
 */

function serializeForm(formElement) {
  if (!(formElement instanceof HTMLFormElement)) {
    throw new Error("serializeForm expects a <form> element.");
  }

  const formData = new FormData(formElement);
  const result = {};

  for (const [key, value] of formData.entries()) {
    if (result.hasOwnProperty(key)) {
      // Convert to array if duplicate fields exist (e.g. checkboxes)
      if (!Array.isArray(result[key])) {
        result[key] = [result[key]];
      }
      result[key].push(value);
    } else {
      result[key] = value;
    }
  }

  return result;
}

// === Example Usage ===
// const form = document.getElementById("myForm");
// const data = serializeForm(form);
// console.log(JSON.stringify(data));

export default serializeForm;
