#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    // Step 1
    // Pass in your student id via command line argument. DONE
    printf("argc: %d\n", argc);
    printf("argv0: %s\n", argv[0]);
    printf("argv1: %s\n", argv[1]);

    // Set environment variable USER_ID to your student ID. DONE
    int setenv_results = setenv("USER_ID", argv[1], 1);
    char *env_results = getenv("USER_ID");
    // Print USER_ID. DONE
    printf("USER_ID: %s\n", env_results);
    if ( setenv_results == -1){
        printf("Error checking putenv"); //self-check
        return -1;
    }

    // Step 2

    // Set environment variable ASSIGNMENT3 to "Environment Variables and Process IDs".DONE
    int result = putenv("ASSIGNMENT3= Environment Variables and Process IDs");
    if (result == -1)
    {
        printf("Error checking putenv");
        return -1;
    }

    // Print ASSIGNMENT3.DONE
    char *env_results1 = getenv("ASSIGNMENT3");
    printf("ASSIGNMENT3: %s\n", env_results1);



    

    // Step 3
    // Write code to get your process's ID (PID).DONE
    char buff[10] = {0};
    pid_t pid = getpid();
    sprintf(buff, "%d", pid);


    // Step 4
    // Set environment variable MY_PID to the PID found above.DONE
    int setenv_results1 = setenv("MY_PID", buff, 1);
    char *env_results2 = getenv("MY_PID");
    // Print the PID.DONE
    printf("PID: %s\n", env_results2);


    // Step 5
    char *course_name = getenv("COURSE_NAME");
    if (course_name != NULL) {
        printf("COURSE_NAME (before): %s\n", course_name);

        // Change it to the correct course name "EE3233 Systems Programming".
        int setenv_results2 = setenv("COURSE_NAME", "EE3233 Systems Programming", 1);
        if (setenv_results2 == -1) {
            printf("Error setting COURSE_NAME\n");
            return -1;
        }

        // Print the new value of COURSE_NAME.
        char *env_results3 = getenv("COURSE_NAME");
        printf("COURSE_NAME (after): %s\n", env_results3);
    } else {
        printf("COURSE_NAME is not set in the environment.\n");
    }

    return 0;
}