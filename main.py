# trying to get rss feed and parse it into dictionary before converting it into a csv file

import csv 
import requests 
import xml.etree.ElementTree as ET 

def loadRSS():
    # url of rss feed
    url = "https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/alle/alle_bundeslaender.rss"

    #creating HTTP response object from url
    response = requests.get(url)

    # saving xml file

    with open("lebensmittelwarnungen.xml", "wb") as f:
        f.write(response.content)