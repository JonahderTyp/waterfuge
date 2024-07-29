import requests

class ConectionError(Exception):
    pass

class DataSender():
    def __init__(self, url, id):
        self.url = url
        self.id = id

    def sendMesurment(self, rpm, flow):
        print(f"Sending data to {self.url} with id {self.id}\trpm: {rpm}\tflow: {flow}")
        data = {
            "id": self.id,
            "rpm": rpm,
            "flow": flow
        }
        response = requests.post(self.url, json=data)
        
        if response.status_code != 200:
            raise ConectionError("Error sending data to server")
        return True