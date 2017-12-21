import java.util.Scanner;
 
/** David Mendez -- Programming Fundamentals -- Fall 2017 -- Programming Assignment 2 (UserNames)
 */
 
public class UserNames {
    public static void main(String args[]) {
 
        System.out.println("CPSC 21000, Fall 2017");
        System.out.println("<David Mendez>");
        System.out.println("PROGRAMMING ASSIGNMENT 2");
 
        Scanner input = new Scanner(System.in);
//create variables  
        do {
            int randNum = 10 + (int) (Math.random() * 99);
            String fName;
            String lName;
            String output;
//give values to the variables 
            System.out.print("Enter your first name: ");
            fName = input.next();
            System.out.print("Enter your last name: ");
            lName = input.next();
            output = lName.substring(0, 4) + fName.substring(0, 1) + randNum;
 
            System.out.println("Your user name is " + output);
            System.out.print("Are there more users (y/n)? ");
 //use ignorecase to let user input a noncase sensitive input 
        } while (input.next().equalsIgnoreCase("Y"));
 // create goodbye message
        System.out.println();
        System.out.println("Goodbye.");
    }
}