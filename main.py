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

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # creating empty list for issue items
    foodissues = []

    for item in root.findall('./channel/item'):

        # emtpy issues dictionary
        issues = {}

        # iterate child elements of issue
        for child in item:
            
             # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                issues['media'] = child.attrib['url']
            else:
                issues[child.tag] = child.text.encode('utf8')
        
        # append news dictionary to news items list
        foodissues.append(issues)

    i = 0
    for item in foodissues:
        item['ID'] = i
        i += 1
    
    return foodissues

# def addID(foodissues):
#     for item in foodissues:
#         item.update({'ID': 0})

#     print(foodissues)

def savetoCSV(foodissues, filename):
    # specifying the fields of csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'content', 'ID']

    # writing to csv file
    with open(filename, 'w') as csvfile:
        #creating a new csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        # writing headers
        writer.writeheader()

        # write data rows
        writer.writerow(foodissues)




def main(): 
    # load rss from web to update existing xml file 
    loadRSS() 
  
    # parse xml file 
    foodissues = parseXML('lebensmittelwarnungen.xml')
    print(foodissues)
  
    # store news items in a csv file 
    savetoCSV(foodissues, 'lebensmittelwarnungen.csv') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 