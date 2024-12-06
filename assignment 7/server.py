import socket

def start_server():
    host = '127.0.0.1'  # localhost
    port = 65432        # non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)  # Listening for one connection
        print("Server is listening...")

        conn, addr = server_socket.accept()  # Accept connection
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()  # Receive data from client
                if not data:
                    break
                print(f"Msg received from client: {data}")

                if data == "hello":
                    response = "world"
                elif data == "exit":
                    response = "exit"
                    conn.sendall(response.encode())
                    print("Responding with: exit")
                    print("Closing connection")
                    break
                else:
                    response = "Invalid message"

                conn.sendall(response.encode())  # Send response to client
                print(f"Responding with: {response}")

if __name__ == "__main__":
    start_server()
