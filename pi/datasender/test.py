from time import sleep

from configobj import ConfigObj

from .comunication import DataSender
from .listen import get_server_ip


def test():
    print("Testing")
    config = ConfigObj("config.cfg")

    server_ip = get_server_ip().get('ip', '0.0.0.0')

    # Create a DataSender object
    data_sender = DataSender(
        f"http://{server_ip}:8080/upload/{config.get('system_id')}/")

    # Send some data
    while True:
        data_sender.sendMesurment(100, 10)
        sleep(1)
        data_sender.sendMesurment(200, 20)
        sleep(1)
        data_sender.sendMesurment(300, 30)
        sleep(1)
        data_sender.sendMesurment(400, 40)
        sleep(1)
        data_sender.sendMesurment(500, 50)
        sleep(1)


if __name__ == "__main__":
    test()
