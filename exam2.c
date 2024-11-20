#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <errno.h>

#define PID_MAX_PATH "/proc/sys/kernel/pid_max"

void handle_error(const char *message) {
    perror(message);
    exit(EXIT_FAILURE);
}

int read_pid_max() {
    int fd = open(PID_MAX_PATH, O_RDONLY);
    if (fd == -1) {
        handle_error("Failed to open pid_max for reading");
    }

    char buffer[64];
    int bytes_read = read(fd, buffer, sizeof(buffer) - 1);
    if (bytes_read == -1) {
        close(fd);
        handle_error("Failed to read pid_max");
    }

    buffer[bytes_read] = '\0';  // Null-terminate the string
    close(fd);

    return atoi(buffer);
}

void write_pid_max(int new_value) {
    int fd = open(PID_MAX_PATH, O_WRONLY);
    if (fd == -1) {
        handle_error("Failed to open pid_max for writing");
    }

    char buffer[64];
    int bytes_written = snprintf(buffer, sizeof(buffer), "%d", new_value);
    if (write(fd, buffer, bytes_written) == -1) {
        close(fd);
        handle_error("Failed to write to pid_max");
    }

    close(fd);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <new_pid_max>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int desired_pid_max = atoi(argv[1]);
    if (desired_pid_max <= 0) {
        fprintf(stderr, "Invalid pid_max value. Must be a positive integer.\n");
        exit(EXIT_FAILURE);
    }

    pid_t pid = fork();
    if (pid == -1) {
        handle_error("Failed to fork process");
    }

    if (pid == 0) {  // Child process
        int old_pid_max = read_pid_max();
        printf("Child: Current pid_max = %d\n", old_pid_max);

        if (desired_pid_max <= old_pid_max) {
            write_pid_max(desired_pid_max);
            printf("Child: pid_max updated to %d\n", desired_pid_max);
        } else {
            fprintf(stderr, "Child: Desired value exceeds current pid_max. No change made.\n");
        }

        exit(EXIT_SUCCESS);
    } else {  // Parent process
        if (wait(NULL) == -1) {
            handle_error("Failed to wait for child process");
        }

        int new_pid_max = read_pid_max();
        printf("Parent: New pid_max = %d\n", new_pid_max);

        exit(EXIT_SUCCESS);
    }
}
