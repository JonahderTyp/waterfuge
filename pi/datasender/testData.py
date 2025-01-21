from time import sleep

from datasender.comunication import DataSender
from configobj import ConfigObj


def test(serverurl: str):
    print("Testing")
    

    # Create a DataSender object
    data_sender = DataSender(serverurl)

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
    print(" DO NOT RUN VIA THIS")
    exit()
