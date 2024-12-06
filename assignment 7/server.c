#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 65432
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    const char *response_hello = "world";
    const char *response_exit = "exit";

    // Create socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }

    // Bind the socket to the port
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Listen for connections
    if (listen(server_fd, 1) < 0) {
        perror("Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening...\n");

    // Accept a client connection
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
        perror("Accept failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Client connected.\n");

    while (1) {
        memset(buffer, 0, BUFFER_SIZE);
        read(new_socket, buffer, BUFFER_SIZE);
        printf("Msg received from client: %s\n", buffer);

        if (strcmp(buffer, "hello") == 0) {
            send(new_socket, response_hello, strlen(response_hello), 0);
            printf("Responding with: %s\n", response_hello);
        } else if (strcmp(buffer, "exit") == 0) {
            send(new_socket, response_exit, strlen(response_exit), 0);
            printf("Responding with: %s\n", response_exit);
            break;
        } else {
            const char *invalid = "Invalid message";
            send(new_socket, invalid, strlen(invalid), 0);
            printf("Responding with: %s\n", invalid);
        }
    }

    printf("Closing connection\n");
    close(new_socket);
    close(server_fd);

    return 0;
}
