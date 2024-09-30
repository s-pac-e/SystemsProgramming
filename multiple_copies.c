
// Branden Sauceda //

#include <fcntl.h>  
#include <unistd.h>  
#include <stdio.h> 
#include <stdlib.h>  

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    int src_fd, dest_fd1, dest_fd2;
    ssize_t read_bytes, written_bytes;
    char buffer[BUFFER_SIZE];

    if (argc != 4) {
        write(STDERR_FILENO, "Usage: ./multiple_copies <source> <dest1> <dest2>\n", 50);
        exit(EXIT_FAILURE);
    }

    src_fd = open(argv[1], O_RDONLY);
    if (src_fd == -1) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    dest_fd1 = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dest_fd1 == -1) {
        perror("Error opening first destination file");
        close(src_fd);
        exit(EXIT_FAILURE);
    }

    dest_fd2 = open(argv[3], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dest_fd2 == -1) {
        perror("Error opening second destination file");
        close(src_fd);
        close(dest_fd1);
        exit(EXIT_FAILURE);
    }

    while ((read_bytes = read(src_fd, buffer, BUFFER_SIZE)) > 0) {
        written_bytes = write(dest_fd1, buffer, read_bytes);
        if (written_bytes == -1) {
            perror("Error writing to first destination file");
            close(src_fd);
            close(dest_fd1);
            close(dest_fd2);
            exit(EXIT_FAILURE);
        }

        written_bytes = write(dest_fd2, buffer, read_bytes);
        if (written_bytes == -1) {
            perror("Error writing to second destination file");
            close(src_fd);
            close(dest_fd1);
            close(dest_fd2);
            exit(EXIT_FAILURE);
        }
    }

    if (read_bytes == -1) {
        perror("Error reading from source file");
    }

    close(src_fd);
    close(dest_fd1);
    close(dest_fd2);

    return 0;
}
