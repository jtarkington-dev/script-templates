
/**
 * RetryExecutor.java
 * Author: Jeremy Tarkington
 *
 * A reusable utility to retry a Callable task:
 * - Set max retries
 * - Set delay between attempts
 * - Handle exceptions gracefully
 */

import java.util.concurrent.Callable;

public class RetryExecutor {

  /**
   * Executes a task with retries on failure.
   *
   * @param task       Callable to run
   * @param maxRetries Number of attempts before giving up
   * @param delayMs    Delay between attempts in milliseconds
   * @param <T>        Return type of the task
   * @return T (result of the task)
   * @throws Exception Final exception thrown after all retries fail
   */
  public static <T> T executeWithRetry(Callable<T> task, int maxRetries, long delayMs) throws Exception {
    int attempts = 0;
    while (true) {
      try {
        return task.call();
      } catch (Exception e) {
        attempts++;
        System.err.println("Attempt " + attempts + " failed: " + e.getMessage());

        if (attempts >= maxRetries) {
          System.err.println("Max retries reached. Giving up.");
          throw e;
        }

        Thread.sleep(delayMs);
      }
    }
  }

  // === Example Usage ===
  public static void main(String[] args) {
    try {
      String result = executeWithRetry(() -> {
        if (Math.random() < 0.8) {
          throw new RuntimeException("Simulated failure");
        }
        return "Success!";
      }, 5, 1000);

      System.out.println("Result: " + result);
    } catch (Exception e) {
      System.err.println("Task failed after retries: " + e.getMessage());
    }
  }
}
