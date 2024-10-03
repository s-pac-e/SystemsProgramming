#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    // Step 1
    // Pass in your student id via command line argument.
    // Set environment variable USER_ID to your student ID.
    // Print USER_ID

    // Step 2
    // Set environment variable ASSIGNMENT3 to "Environment Variables and Process IDs"
    // Print ASSIGNMENT3

    // Step 3
    // Write code to get your process's ID (PID)
    // Example code to convert int to char[]
    // char pid_str[8] = {0};
    // sprintf(pid_str, "%d", <variable used for getpid>);

    // Step 4
    // Set environment variable MY_PID to the PID found above
    // Print the PID

    // Step 5
    // An environment variable named "COURSE_NAME" is available
    // Print the value
    // Change it to the correct course name (EE3233 Systems Programming)
    // Print it again

    return 0;
}