import socket

def start_client():
    host = '127.0.0.1'  # localhost
    port = 65432        # same port as server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  # Connect to server
        while True:
            message = input("Msg to send: ")  # User input
            client_socket.sendall(message.encode())  # Send message to server
            response = client_socket.recv(1024).decode()  # Receive response from server

            print(f"Server responded with: {response}")

            if message == "exit":
                print("Closing connection")
                break

if __name__ == "__main__":
    start_client()
