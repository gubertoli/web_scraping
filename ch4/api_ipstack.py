import json
from urllib.request import urlopen
import os


def getCountry(ipAddress, api_key):
    response = urlopen("http://api.ipstack.com/"+ipAddress+"?access_key="+api_key).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

api_key = os.getenv('API_ipstack')
print(getCountry("50.78.253.58", api_key))
