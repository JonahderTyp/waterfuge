from time import sleep

import requests


class ConectionError(Exception):
    pass


class DataSender():
    def __init__(self, url):
        self.url = url

    def sendMesurment(self, rpm, flow, trys=5):
        error = False
        for try_ in range(trys):
            # print(
            # f"Sending data to {self.url} \trpm: {rpm}\tflow: {flow}")
            data = {
                "rpm": rpm,
                "flow": flow
            }

            try:
                response = requests.post(self.url, json=data, timeout=1)
                if response.status_code // 100 != 2:
                    raise Exception(f"Status code {response.status_code}")
                if error:
                    print(f"Request successfull after {try_+1} atempts")
                return
            except Exception as ex:
                error = True
                print(
                    f"Error sending data to server. Try {try_+1}/{trys} {ex}")
                sleep(1)
                if try_ >= trys-1:
                    raise ConectionError("Error sending data to server")
