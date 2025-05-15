
/**
 * SystemInfoReporter.java
 * Author: Jeremy Tarkington
 *
 * A reusable utility to print basic system stats:
 * - OS and JVM info
 * - CPU cores
 * - Memory usage
 * - Uptime (approx based on system start)
 */

import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.text.DecimalFormat;
import java.util.concurrent.TimeUnit;

public class SystemInfoReporter {

  public static void main(String[] args) {
    printSystemInfo();
  }

  public static void printSystemInfo() {
    System.out.println("===== System Info =====");

    // OS Info
    System.out.println("OS: " + System.getProperty("os.name"));
    System.out.println("OS Version: " + System.getProperty("os.version"));
    System.out.println("Architecture: " + System.getProperty("os.arch"));

    // Java Info
    System.out.println("Java Version: " + System.getProperty("java.version"));
    System.out.println("Java Vendor: " + System.getProperty("java.vendor"));

    // CPU Info
    System.out.println("Available CPU Cores: " + Runtime.getRuntime().availableProcessors());

    // Memory Info
    long maxMem = Runtime.getRuntime().maxMemory();
    long usedMem = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
    DecimalFormat df = new DecimalFormat("#.##");

    System.out.println("Memory Used: " + df.format(usedMem / 1024.0 / 1024.0) + " MB");
    System.out.println("Memory Max : " + df.format(maxMem / 1024.0 / 1024.0) + " MB");

    // Uptime (approx)
    RuntimeMXBean runtimeBean = ManagementFactory.getRuntimeMXBean();
    long uptimeMs = runtimeBean.getUptime();
    String formattedUptime = formatDuration(uptimeMs);
    System.out.println("JVM Uptime: " + formattedUptime);
  }

  private static String formatDuration(long millis) {
    long hours = TimeUnit.MILLISECONDS.toHours(millis);
    long minutes = TimeUnit.MILLISECONDS.toMinutes(millis) % 60;
    long seconds = TimeUnit.MILLISECONDS.toSeconds(millis) % 60;
    return String.format("%02dh %02dm %02ds", hours, minutes, seconds);
  }
}
