/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproject12;
import java.util.Scanner;

public class Javaproject12 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Text Adventure!");
        System.out.println("You find yourself in a dark forest...");
        System.out.println("You can go NORTH or EAST.");

        String choice = scanner.nextLine().toUpperCase();

        if (choice.equals("NORTH")) {
            northPath(scanner);
        } else if (choice.equals("EAST")) {
            eastPath(scanner);
        } else {
            System.out.println("Invalid choice. You stumble and fall.");
            gameOver();
        }

        scanner.close();
    }

    public static void northPath(Scanner scanner) {
        System.out.println("You walk north and find a small cottage.");
        System.out.println("Do you ENTER or CONTINUE?");

        String choice = scanner.nextLine().toUpperCase();

        if (choice.equals("ENTER")) {
            enterCottage(scanner);
        } else if (choice.equals("CONTINUE")) {
            System.out.println("You continue north and find a deep ravine. You cannot cross.");
            gameOver();
        } else {
            System.out.println("Invalid choice. You are lost.");
            gameOver();
        }
    }

    public static void eastPath(Scanner scanner) {
        System.out.println("You walk east and find a shimmering stream.");
        System.out.println("Do you DRINK or FOLLOW?");

        String choice = scanner.nextLine().toUpperCase();

        if (choice.equals("DRINK")) {
            System.out.println("The water is refreshing. You feel stronger.");
            followStream(scanner);
        } else if (choice.equals("FOLLOW")) {
            followStream(scanner);
        } else {
            System.out.println("Invalid choice. You are lost.");
            gameOver();
        }
    }

    public static void enterCottage(Scanner scanner) {
        System.out.println("You enter the cottage. An old woman is inside.");
        System.out.println("She offers you a potion. Do you ACCEPT or DECLINE?");

        String choice = scanner.nextLine().toUpperCase();

        if (choice.equals("ACCEPT")) {
            System.out.println("You drink the potion and feel a surge of energy. You win!");
            gameWon();
        } else if (choice.equals("DECLINE")) {
            System.out.println("The old woman smiles. You leave the cottage and find a path out of the forest.");
            gameWon();
        } else {
            System.out.println("Invalid choice. The old woman shoos you out.");
            gameOver();
        }
    }

    public static void followStream(Scanner scanner) {
        System.out.println("You follow the stream and find a hidden cave.");
        System.out.println("Do you ENTER or BYPASS?");

        String choice = scanner.nextLine().toUpperCase();

        if (choice.equals("ENTER")) {
            System.out.println("You enter the cave and find a treasure chest. You win!");
            gameWon();
        } else if (choice.equals("BYPASS")) {
            System.out.println("You bypass the cave and find a path out of the forest.");
            gameWon();
        } else {
            System.out.println("Invalid choice. You are lost.");
            gameOver();
        }
    }

    public static void gameOver() {
        System.out.println("Game Over.");
    }

    public static void gameWon() {
        System.out.println("Congratulations! You won the game!");
    }
}
/**
 *
 * @author hp
 */
