# helloworld Project


## Overview

this is a simple Java project that reads a file provided as a command-line argument and prints its contents line by line to the standard output. 

### main features:
- takes a file name as input
- reads the file line by line.
- prints each line to the console

## implementation
- create a HelloWorld class containing the main method that reads from a file via the command line and prints its content to standard output. 
- compile the code using Javac
    - `javac -d out/production/HelloWorld src/HelloWorld.java`
- package the project:
    - create the manifest.txt at the root directory to specify the main class for .jar file
    - use jar at the command line to package the project into a .jar file
        - `jar cvfm HelloWorld.jar manifest.txt -C out/production/HelloWorld/ .`
- run the .jar file
    - `java -jar HelloWorld.jar myfile.txt`

## how to run

- Ensure you have the JDK installed. 
- go to the directory containing HelloWorld.jar
- input the command line in terminal: 
```bash
Java -jar HelloWorld.jar myfile.txt
```








