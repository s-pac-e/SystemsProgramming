#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <errno.h>
#include <sys/wait.h>
#include <time.h>

// Function prototypes for signal handlers
void signal_handler_1(int sig);
void signal_handler_2(int sig);

int pipe_fd[2]; // Pipe file descriptors

int main() {
    pid_t pid;
    struct sigaction sa;

    // Create a pipe
    if (pipe(pipe_fd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    // Block SIGUSR1 and SIGUSR2 in the parent process
    sigset_t block_mask, empty_mask;
    sigemptyset(&empty_mask);
    sigemptyset(&block_mask);
    sigaddset(&block_mask, SIGUSR1);
    sigaddset(&block_mask, SIGUSR2);

    if (sigprocmask(SIG_BLOCK, &block_mask, NULL) == -1) {
        perror("sigprocmask");
        exit(EXIT_FAILURE);
    }

    // Setup signal handlers for parent
    sa.sa_flags = 0;
    sa.sa_mask = empty_mask;

    sa.sa_handler = signal_handler_1;
    if (sigaction(SIGUSR1, &sa, NULL) == -1) {
        perror("sigaction(SIGUSR1)");
        exit(EXIT_FAILURE);
    }

    sa.sa_handler = signal_handler_2;
    if (sigaction(SIGUSR2, &sa, NULL) == -1) {
        perror("sigaction(SIGUSR2)");
        exit(EXIT_FAILURE);
    }
    clock_t t;
    t = clock();
    printf("Parent started...\n");

    // Fork the process
    pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Child process

        // Unblock all signals
        if (sigprocmask(SIG_SETMASK, &empty_mask, NULL) == -1) {
            perror("sigprocmask");
            exit(EXIT_FAILURE);
        }

        // Setup signal handler for SIGUSR1
        sa.sa_handler = signal_handler_1;
        if (sigaction(SIGUSR1, &sa, NULL) == -1) {
            perror("sigaction(SIGUSR1) in child");
            exit(EXIT_FAILURE);
        }

        // Suspend and wait for SIGUSR1
        pause();

        // Read message from pipe
        char buffer[128];
        close(pipe_fd[1]); // Close write end of the pipe
        read(pipe_fd[0], buffer, sizeof(buffer));
        // clock_t childt;
        // childt = clock();
        printf("Child received message: %s\n", buffer);

        // Send SIGUSR2 to parent
        kill(getppid(), SIGUSR2);

        printf("Goodbye from Child (PID: %d)\n", getpid());
        exit(EXIT_SUCCESS);
        // childt = clock() - childt;
        // double child_taken = ((double)childt)/CLOCKS_PER_SEC;
        // printf("Child Process took %f seconds", child_taken);

    } else {
        // Parent process
        sleep(3);

        printf("Parent about to signal child...\n");
        // t = clock() - t;
        // double time_taken = ((double)t)/CLOCKS_PER_SEC;
        // printf("Process took %f seconds\n", time_taken);

        // Send SIGUSR1 to child
        kill(pid, SIGUSR1);

        // Write message to pipe
        close(pipe_fd[0]); // Close read end of the pipe
        const char *message = "Hello from Parent!\n";
        write(pipe_fd[1], message, strlen(message) + 1);

        // Wait for SIGUSR2
        sigsuspend(&empty_mask);

        printf("Parent received SIGUSR2!\n");
        printf("Goodbye from Parent (PID: %d)\n", getpid());

        // Wait for child process to finish
        wait(NULL);
    }

    return 0;
}

// Signal handlers
void signal_handler_1(int sig) {
    if (sig == SIGUSR1) {
        printf("Child received SIGUSR1!\n");
    }
}

void signal_handler_2(int sig) {
    if (sig == SIGUSR2) {
        printf("Parent received SIGUSR2!\n");
    }
}
