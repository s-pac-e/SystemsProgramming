#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid_child;

    // Create a child process using fork()
    pid_child = fork();

    if (pid_child < 0) {
        // Error handling if fork() fails
        perror("fork failed");
        return 1;
    } else if (pid_child == 0) {
        // This block executes in the child process
        printf("[PID %d] Child process. Parent PID = %d.\n", (int)getpid(), (int)getppid());
    } else {
        // This block executes in the parent process
        printf("[PID %d] Parent process. Child PID = %d.\n", (int)getpid(), (int)pid_child);
    }

    return 0;
}
