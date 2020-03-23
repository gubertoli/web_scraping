# this is the last example from chapter 4
# using multiples APIs to understanding who contributes more with wikipedia

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import os
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    return bsObj.find("div", {"id" : "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"

    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, features="html.parser")

    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})

    addressList = set()

    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())

    return addressList

def getCountry(ipAddress, api_key):
    try:
        response = urlopen("http://api.ipstack.com/"+ipAddress+"?access_key="+api_key).read().decode('utf-8')
    except HTTPError:
        return None

    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")
api_key = os.getenv('API_ipstack')

while(len(links) > 0):
    for link in links:
        print("-----------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP, api_key)
            if country is not None:
                print(historyIP + " is from " + country)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
