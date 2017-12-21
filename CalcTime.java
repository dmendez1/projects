import java.util.Scanner;

/** David Mendez -- Programming Fundamentals -- Fall 2017 -- Programming Assignment 1 (CalcTime)
 */

public class CalcTime {

    public static void main (String args []) {

        // create a new Scanner
        Scanner s = new Scanner(System.in);

        System.out.println("CPSC 21000, Fall 2017");

        System.out.println("<David Mendez>");

        System.out.println("PROGRAMMING ASSIGNMENT 1");

        System.out.println();

        //use print not println so it stays on the same line
        System.out.print("Enter the number of seconds: ");

        // Create integers
        int secs;
        int mins;
        int hr;
        int days;
        int user_output;
        {
            // Set the "secs" integer equal to scanner output but to use the next integer
            secs = s.nextInt();
        }

        // Define integers by giving them values
        mins = (secs % 3600) / 60;

        // set mins to equal secs and modulus operator to 36000 divided by 602

        hr = (secs % 86400) / 3600;
        // hours will be secs modulus 86400 to equal the amount of days first then divided by 3600 secs in an hour

        days = secs / 86400;
        // there are 86400 seconds in one day so seconds divided by 86400 will give you one day

        user_output = (secs % 3600) % 60;

        //blank line to space in console looks neater
        System.out.println();

        //use print not println so output is on the same line
        System.out.print("The equivalent time is "  );

        // print an output for the user adding all the ints after the text output
        System.out.println(days + " days, " + hr + " hours, " + mins + " minutes," + " and " + user_output + " seconds" );

    }

}