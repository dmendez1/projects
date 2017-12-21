// David Mendez -- Programming Fundamentals -- Fall 2017 -- Programming Assignment 6 (MouseRace2)


import java.util.Random;
import java.util.Scanner;
import java.util.Stack;




public class MouseRace2 {

    // This internal class here to take care of their objects and things makes life a lot easier later on in the code, trust me
    class Animal {
        int x;
        int y;
        String representation;
        Stack moveList = new Stack();

        public Animal(int x, int y, String representation) {
            this.x = x;
            this.y = y;
            this.representation = representation;
        }
    }


    // Variables
    private int mouseX;
    private int mouseY;
    private int catX;
    private int catY;
    private int cheeseX;
    private int cheeseY;
    private int score;

    // I formatted it this way for ease of reading if someone wanted to modify it later
    private String[][] board = {{"#","#","#","#","#","#","#","#","#","#","#","#"},
            {"#","%"," ","#","#","#","#","#","#","#"," ","#"},
            {"#","#"," ","#","#","#","#","#","#"," ", " ","#"},
            {"#","#"," "," "," "," "," ","#","#"," ","#","#"},
            {"#"," "," ","#","#","#"," ","#"," "," ","#","#"},
            {"#"," ","#","#","#","#"," ","#"," "," ","#","#"},
            {"#"," ","#"," "," ","#"," ","#","#"," ","#","#"},
            {"#"," ","#","#"," ","#"," ","#","#"," ","#","#"},
            {"#"," "," ","#"," ","#"," ","#","#"," ","#","#"},
            {"#","#"," ","#"," ","#"," "," "," "," ","#","#"},
            {"#"," "," "," "," ","#","#","#","#"," ","$","#"},
            {"#","#","#","#","#","#","#","#","#","#","#","#"},
    };

    private String[] potentialCatMoves = {"n","s","e","w"};

    private Stack mouseMoves = new Stack();
    private Stack catMoves = new Stack();
    static Animal mouse;
    static Animal cat;
    public MouseRace2() {
        // Sets all the score values
        score = 0;
        mouseX = 1;
        mouseY = 1;
        cheeseX = 10;
        cheeseY = 10;
        catX = new Random().nextInt(12);
        catY = new Random().nextInt(12);

        mouse = new Animal(1, 1, "%");


        while((catX == mouse.x && catY == mouse.y)&&(board[catX][catY] == "#")&&(board[catX][catY] == "$")) {
            catX = new Random().nextInt(12);
            catY = new Random().nextInt(12);
        }

        cat = new Animal(catX, catY, "C");

        // Prints the requested header
        System.out.println("CPSC 21000, Fall 2017");
        System.out.println("NAME: David Mendez");
        System.out.println("PROGRAMMING ASSIGNMENT 6\n");
        System.out.println("**************************************");
        System.out.println("*** WELCOME TO THE MOUSE RACE GAME ***");
        System.out.println("**************************************\n");

        board[catX][catY] = cat.representation;

        // Main game loop
        while(!gameWon()  || gameLost()) {
            printMaze();
            System.out.printf("\nYour current score: %d\n", score);
            Scanner input = new Scanner(System.in);
            System.out.print("Select a move direction (n/s/e/w): ");
            parseCmd(input.nextLine(), mouse);
            parseCmd(potentialCatMoves[new Random().nextInt(4)], cat);

        }

        // If the mouse wins, add 100 to the score, if he loses, subtract 100. Display board and win/loss message
        if (gameWon()) {
            score += 100;
            printMaze();
            System.out.println("GAME OVER! MOUSE GOT THE CHEESE!");

        } else if (gameLost()) {
            score -= 100;
            printMaze();
            System.out.println("GAME OVER! MOUSE GOT CAUGHT!");

        }

        // And finally tell them of their scores
        System.out.printf("Your score was: %d", score);


    }

    // Checks if the x and y's of the cheese and mouse match up
    private boolean gameWon() {
        if (mouse.x == cheeseX && mouse.y == cheeseY)
            return true;
        else
            return false;
    }

    // Checks if the mouse's position is the same as the cat's
    private boolean gameLost() {
        if (mouse.x == cat.x && mouse.y == cat.y) {
            return true;
        } else
            return false;
    }

    // Moves the mouse, if it's a wall it prints out that you can't move, if there's whitespace it'll do all the updates and print a newline for formatting
    private void makeMove(int x, int y, Animal animal) {
        if(board[x][y] == "#" && animal.representation == "%") {
            System.out.println("You cannot move there!\n");
        } else if ((board[x][y] == "#" || board[x][y] == "%") && animal.representation == "C"){
            // Dummy condition, no output should be shown to the player since the cat isn't the player in the game
            System.out.println();
        } else {
            board[animal.x][animal.y] = " ";
            board[x][y] = animal.representation;
            animal.x = x;
            animal.y = y;
            // If the animal is the mouse we want to minus out the score, otherwise if it's the cat then do the score shouldn't be affected
            if (animal.representation == "%")
                score--;
            System.out.println();
        }
    }

    // Prints out the maze
    private void printMaze() {
        for(int x = 0; x < board.length; x++) {
            for(int y = 0; y < board[0].length; y++) {
                System.out.print(board[x][y]);
            }
            System.out.println();
        }

    }

    // Sets the command to uppercase just so we don't have to worry about cases
    private void parseCmd(String cmd, Animal animal) {
        switch(cmd.toUpperCase()) {
            case "N":
                makeMove(animal.x-1, animal.y, animal);
                animal.moveList.push("N");
                break;
            case "S":
                makeMove(animal.x+1, animal.y, animal);
                animal.moveList.push("S");
                break;
            case "W":
                makeMove(animal.x, animal.y-1, animal);
                animal.moveList.push("W");
                break;
            case "E":
                makeMove(animal.x, animal.y+1, animal);
                animal.moveList.push("E");
                break;
            case "U":
                // We want to basically undo the most recent move, so everything needs to happen reverso, also add 1 to the score so it looks like the score wasn't changed
                switch((String)animal.moveList.pop()) {
                    case "N":
                        parseCmd("S", animal);
                        parseCmd("S", MouseRace2.cat);
                        score++;
                        break;
                    case "S":
                        parseCmd("N", animal);
                        parseCmd("N", MouseRace2.cat);
                        score++;
                        break;
                    case "E":
                        parseCmd("W", animal);
                        parseCmd("W", MouseRace2.cat);
                        score++;
                        break;
                    case "W":
                        parseCmd("E", animal);
                        parseCmd("E", MouseRace2.cat);
                        score++;
                        break;
                    default:
                        break;

                }
                break;
            default:
                System.out.println("Unknown command!");
                break;
        }
    }

    // Main method that creates the MouseRace2 object
    public static void main(String[] args) {
        MouseRace2 game = new MouseRace2();
    }

}
