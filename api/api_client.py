import requests
import json

class APIClient:

    def __init__(self, url, api_key, header) -> None:
        self.url = url
        self.api_key = api_key
        self.header = header

    #TODO: refactor code for different type of Auth
    #Function to send API request
    def get_data(self):

        url = f"{self.url}"

        #Check if there is an API key and run corresponding request you if you do have one
        if isinstance(self.api_key, str):
            headers = f"{self.header}: {self.api_key}"
            response = requests.get(url, headers=headers) 
        else:
            response = requests.get(url)

        if response.status_code == 200:
            json_object = response.json()
            return json_object
        else:
            response.raise_for_status()

