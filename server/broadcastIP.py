import socket
from time import sleep


def send_ip(ip, server_ip, port=8080, timeout=1):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout for the connection attempt
    client_socket.settimeout(timeout)

    try:
        # Try to connect to the server with the timeout
        print(
            f"Attempting to connect to {server_ip}:{port} (timeout {timeout} seconds)...")
        client_socket.connect((server_ip, port))

        # Send the IP address
        message = str({'ip': ip})
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent IP {ip} to server {server_ip}:{port}")

    except socket.timeout:
        # Handle the case where the connection times out
        print(f"Connection attempt to {server_ip}:{port} timed out.")

    except socket.error as e:
        # Handle other socket errors (e.g., server not running)
        print(f"Socket error occurred: {e}")

    finally:
        # Close the socket
        client_socket.close()


# Get the IP of the Windows machine
windows_ip = socket.gethostbyname(socket.gethostname())

linux_server_ips = ['192.168.0.151', '192.168.0.152',
                    '192.168.0.153', '192.168.0.154']

while True:
    for linux_server_ip in linux_server_ips:
        send_ip(windows_ip, linux_server_ip)
        print(f"Sent IP {windows_ip} to server {linux_server_ip}")
    print()
    sleep(5)
