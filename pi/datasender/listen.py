import json
import socket


def get_server_ip(port=8080) -> dict:
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    server_socket.bind(('', port))

    server_socket.settimeout(5)

    # Listen for incoming connections (1 client at a time)
    server_socket.listen(1)
    print(f"Listening for connections on port {port}...")

    # Accept incoming connection
    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            # Receive the data
            data = conn.recv(1024).decode('utf-8')
            conn.close()
            if data:
                res = json.loads(data)
                print(f"Received data: {res}")
                return res['ip']
            return {}
        except socket.timeout:
            print("no connection... is the server running?")
        except KeyboardInterrupt:
            server_socket.close()
            print("Exiting...")
            exit(0)
