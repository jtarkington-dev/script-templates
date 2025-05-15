
/**
 * SimpleHttpClient.java
 * Author: Jeremy Tarkington
 *
 * A reusable Java 11+ HTTP client wrapper that supports:
 * - GET and POST requests
 * - Custom headers and body
 * - Logging of response status and content
 */

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpHeaders;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.Map;

public class SimpleHttpClient {

  private static final HttpClient client = HttpClient.newBuilder()
      .connectTimeout(Duration.ofSeconds(5))
      .build();

  public static String get(String url, Map<String, String> headers) throws IOException, InterruptedException {
    HttpRequest.Builder builder = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .GET();

    headers.forEach(builder::header);

    HttpRequest request = builder.build();
    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

    logResponse(response);
    return response.body();
  }

  public static String post(String url, String jsonBody, Map<String, String> headers)
      throws IOException, InterruptedException {
    HttpRequest.Builder builder = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
        .header("Content-Type", "application/json");

    headers.forEach(builder::header);

    HttpRequest request = builder.build();
    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

    logResponse(response);
    return response.body();
  }

  private static void logResponse(HttpResponse<String> response) {
    System.out.println("Status: " + response.statusCode());
    HttpHeaders headers = response.headers();
    headers.map().forEach((key, values) -> System.out.println(key + ": " + String.join(", ", values)));
    System.out.println("Body:\n" + response.body());
  }

  // === Example Usage ===
  public static void main(String[] args) {
    try {
      System.out.println("=== GET Example ===");
      get("https://jsonplaceholder.typicode.com/posts/1", Map.of());

      System.out.println("\n=== POST Example ===");
      post("https://jsonplaceholder.typicode.com/posts",
          "{\"title\": \"foo\", \"body\": \"bar\", \"userId\": 1}",
          Map.of());
    } catch (Exception e) {
      System.err.println("Request failed: " + e.getMessage());
    }
  }
}
