from urllib.request import urlopen
import json


def fetch_json_data(url):
    if type(url) != str:
        raise TypeError("api url must be string.")
    
    response = response = urlopen(url)
    data_json = json.loads(response.read())
    
    return data_json
        
