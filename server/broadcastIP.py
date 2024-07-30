import socket
import time


def broadcast_ip(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.2)
    message = "SERVER_IP:" + input("Server IP: ").strip()
    while True:
        print("Broadcasting IP: " + message)
        s.sendto(message.encode(), ('<broadcast>', port))
        time.sleep(5)


broadcast_ip(37020)
