from time import sleep
from comunication.DataSender import DataSender


def main():
    # Create a DataSender object
    sender = DataSender("http://localhost:50000/data", 1)

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
