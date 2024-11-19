import socket
import threading

# Function to handle the client's communication
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            # Receive data from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            # Send the same message back to the client (Echo)
            client_socket.send(f"Echo: {message}".encode('utf-8'))
        except ConnectionResetError:
            break

    print(f"Connection from {client_address} closed.")
    client_socket.close()

# Main server function
def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)  # Max number of clients to handle simultaneously

    print(f"Server listening on {server_address[0]}:{server_address[1]}")

    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()