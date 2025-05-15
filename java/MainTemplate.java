
/**
 * MainTemplate.java
 * Author: Jeremy Tarkington
 * Description: A reusable starting point for Java console applications.
 * Features basic CLI input, logging, and method structure.
 */

import java.util.Scanner;

public class MainTemplate {

  // Entry point
  public static void main(String[] args) {
    System.out.println("=== Java MainTemplate Started ===");

    // Parse args if needed
    if (args.length > 0) {
      System.out.println("Arguments provided:");
      for (String arg : args) {
        System.out.println(" - " + arg);
      }
    } else {
      System.out.println("No command-line arguments provided.");
    }

    // Example of user input
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter your name: ");
    String name = scanner.nextLine();
    scanner.close();

    greetUser(name);

    System.out.println("=== Java MainTemplate Finished ===");
  }

  // Example method
  public static void greetUser(String name) {
    System.out.println("Hello, " + name + "! This is your starter Java program.");
  }
}
