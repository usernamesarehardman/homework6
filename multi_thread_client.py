import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 12345)

    # Connect to the server
    client_socket.connect(server_address)

    try:
        # Send some messages to the server
        while True:
            message = input("Enter message for server (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.send(message.encode('utf-8'))

            # Receive the server's response
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {response}")

    finally:
        print("Closing connection.")
        client_socket.close()

if __name__ == '__main__':
    start_client()
