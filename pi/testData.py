from .comunication import DataSender
from time import sleep


def main():
    # Create a DataSender object
    sender = DataSender("http://localhost:50000/data", 1)

    # Send some data
    sender.sendMesurment(100, 10)
    sleep(1)
    sender.sendMesurment(200, 20)
    sleep(1)
    sender.sendMesurment(300, 30)