import socket


def receive_broadcast(port=12345):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('', port))

    print(f"Listening for broadcast messages on port {port}")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message: {data.decode('utf-8')} from {addr}")


if __name__ == "__main__":
    receive_broadcast()
