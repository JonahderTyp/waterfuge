from time import sleep

import requests


class ConectionError(Exception):
    pass


class DataSender():
    def __init__(self, url):
        self.url = url

    def sendMesurment(self, rpm, flow):
        trys = 5
        for try_ in range(trys):
            print(
                f"Sending data to {self.url} \trpm: {rpm}\tflow: {flow}")
            data = {
                "rpm": rpm,
                "flow": flow
            }
            response = requests.post(self.url, json=data, timeout=1)

            if response.status_code == 200:
                print("Data sent successfully")
                return
            print(f"Error sending data to server. Try {try_+1}/{trys}")
            sleep(1)
            if try_ >= trys-1:
                raise ConectionError("Error sending data to server")