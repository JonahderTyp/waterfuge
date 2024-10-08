from time import sleep

from configobj import ConfigObj

from .comunication import DataSender
from .listen import get_server_ip


def test(config: ConfigObj):
    print("Testing")

    # server_ip = get_server_ip().get('ip', '0.0.0.0')
    server_ip = "127.0.0.1"

    # Create a DataSender object
    data_sender = DataSender(
        f"http://{server_ip}:8080/data/{config.get('system_id')}/")

    # Send some data
    while True:
        data_sender.sendMesurment(100, 50)
        sleep(0.5)
        data_sender.sendMesurment(200, 10)
        sleep(0.5)
        data_sender.sendMesurment(300, 20)
        sleep(0.5)
        data_sender.sendMesurment(400, 30)
        sleep(0.5)
        data_sender.sendMesurment(500, 40)
        sleep(0.5)


if __name__ == "__main__":
    test()
