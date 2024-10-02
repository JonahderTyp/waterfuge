from time import sleep

from comunication import DataSender
from configobj import ConfigObj

from .listen import get_server_ip


def main():
    print("Testing")
    config = ConfigObj("config.cfg")

    # Create a DataSender object
    data_sender = DataSender(
        f"http://{get_server_ip().get('ip', '0.0.0.0')}:8080/upload/{config.get('system_id')}/")

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
    main()
