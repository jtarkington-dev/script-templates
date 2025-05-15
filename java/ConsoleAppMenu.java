/**
 * ConsoleAppMenu.java
 * Author: Jeremy Tarkington
 *
 * A reusable menu-based console application structure.
 * Includes:
 * - Scanner input loop
 * - Switch-case option handling
 * - Graceful exit
 */

import java.util.Scanner;

public class ConsoleAppMenu {

    private static boolean running = true;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (running) {
            printMenu();
            System.out.print("Select an option: ");
            String input = scanner.nextLine().trim();

            switch (input) {
                case "1":
                    runActionOne();
                    break;
                case "2":
                    runActionTwo();
                    break;
                case "3":
                    exitApp();
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }

            System.out.println(); // spacing
        }

        scanner.close();
    }

    private static void printMenu() {
        System.out.println("===== MAIN MENU =====");
        System.out.println("1. Run Task A");
        System.out.println("2. Run Task B");
        System.out.println("3. Exit");
    }

    private static void runActionOne() {
        System.out.println("Task A executed.");
        // TODO: Add logic here
    }

    private static void runActionTwo() {
        System.out.println("Task B executed.");
        // TODO: Add logic here
    }

    private static void exitApp() {
        System.out.println("Goodbye!");
        running = false;
    }
}
