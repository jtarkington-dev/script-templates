
/**
 * JsonLoader.java
 * Author: Jeremy Tarkington
 *
 * A reusable utility to:
 * - Load JSON into a custom Java object
 * - Save an object back to JSON
 * Requires: com.google.gson.Gson
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class JsonLoader {

  private static final Gson gson = new GsonBuilder().setPrettyPrinting().create();

  /**
   * Load a JSON file into a specified class type.
   */
  public static <T> T load(String filePath, Class<T> type, T fallback) {
    try (FileReader reader = new FileReader(filePath)) {
      return gson.fromJson(reader, type);
    } catch (IOException e) {
      System.err.println("Failed to load JSON from: " + filePath);
      e.printStackTrace();
      return fallback;
    }
  }

  /**
   * Save an object to a JSON file.
   */
  public static void save(String filePath, Object data) {
    try (FileWriter writer = new FileWriter(filePath)) {
      gson.toJson(data, writer);
      System.out.println("JSON saved to: " + filePath);
    } catch (IOException e) {
      System.err.println("Failed to write JSON to: " + filePath);
      e.printStackTrace();
    }
  }

  // === Example Model & Usage ===
  public static class Config {
    public String username;
    public boolean darkMode;
    public int refreshInterval;
  }

  public static void main(String[] args) {
    String path = "config.json";

    // Load with fallback if not found
    Config defaultConfig = new Config();
    defaultConfig.username = "default";
    defaultConfig.darkMode = true;
    defaultConfig.refreshInterval = 30;

    Config config = load(path, Config.class, defaultConfig);
    System.out.println("Loaded user: " + config.username);

    // Save it back
    config.username = "username";
    save(path, config);
  }
}
