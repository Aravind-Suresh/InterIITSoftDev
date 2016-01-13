import urllib, urllib2
import os, sys, argparse
import json
from bs4 import BeautifulSoup
from PIL import Image

def getDetails(rollNumber):
    # Creating request
    req = urllib2.Request('https://ccw.iitm.ac.in/IITMHostels/sinfo/' + rollNumber)
    response = urllib2.urlopen(req)
    htmlDoc = response.read()

    details = {}

    # Initiating the parser
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    table = soup.find(id='block-system-main').table

    details['Name'] = table.find_all('h2')[0].getText().strip()

    detRaw = table.find_all('td')[3::2]

    details['Gender'] = detRaw[0].getText().strip()
    details['Department'] = detRaw[4].getText().strip()
    details['Course'] = detRaw[1].getText().strip()
    details['Date of joining'] = detRaw[3].getText().strip()
    details['Faculty advisor'] = detRaw[7].getText().strip()
    details['Current semester'] = detRaw[6].getText().strip()

    return details

def getImage(rollNumber):
    url = "https://photos.iitm.ac.in/byroll.php?roll=" + rollNumber.upper()
    filePath = os.getcwd() + os.sep + "data" + os.sep + "images" + os.sep + rollNumber + ".jpg"
    urllib.urlretrieve(url, filePath)
    return filePath

def showImage(filePath):
    img = Image.open(filePath)
    img.show()

def displayData(details):
    # TODO: Create window to display data
    showImage(details['__image_path__'])

if __name__ == '__main__':
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--roll_number', help='Roll number', required=True)
    parser.add_argument('-s','--save', help='Save data', action='store_true')
    args = parser.parse_args()

    toSave = False
    if args.save:
        toSave = True

    rollNumber = args.roll_number.upper()

    details = getDetails(rollNumber)
    imagePath = getImage(rollNumber)
    details['__image_path__'] = imagePath

    # Displaying student details and showing image
    displayData(details)

    if toSave:
        # Saving details to json file
        outFilePath = os.getcwd() + os.sep + "data" + os.sep + "details" + os.sep + rollNumber + ".json"
        with open(outFilePath, 'w') as outfile:
            json.dump(details, outfile)

    else:
        # Removing the image file which was retrieved earlier
        os.rmdir(imagePath)
