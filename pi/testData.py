from time import sleep
from comunication import DataSender
import socket


def listen_for_ip(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    while True:
        data, addr = s.recvfrom(1024)
        if data.startswith(b"SERVER_IP:"):
            server_ip = data.split(b":")[1].decode()
            return server_ip


def main():
    print("Waiting for server IP")
    server_ip = listen_for_ip(37020)
    print("Server IP found: ", server_ip)
    # Create a DataSender object
    sender = DataSender(f"http://{server_ip}:50123/data", 1)

    # Send some data
    while True:
        sender.sendMesurment(100, 10)
        sleep(1)
        sender.sendMesurment(200, 20)
        sleep(1)
        sender.sendMesurment(300, 30)
        sleep(1)
        sender.sendMesurment(400, 40)
        sleep(1)
        sender.sendMesurment(500, 50)
        sleep(1)


if __name__ == "__main__":
    main()
