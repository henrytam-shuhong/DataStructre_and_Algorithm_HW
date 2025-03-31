import java.io.*;
import java.util.Scanner;
public class HelloWorld {
    public static void main(String[] args) {
        // make sure correct file name provide as an argument
        if (args.length !=1){
            System.out.println("usage: java HelloWorld <file>");
            return;
        }

        String filename = args[0];

        try (Scanner scanner = new Scanner(new File(filename))) {
            // Read the file line by line and print it to standard output
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
        } catch (FileNotFoundException e){
            System.err.println("File not found: " + filename);
        }


    }
}