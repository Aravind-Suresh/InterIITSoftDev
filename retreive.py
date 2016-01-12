import urllib
import os, sys
import argparse
from PIL import Image

def getDetails(rollNumber):
    return details

def getImage(rollNumber):
    url = "https://photos.iitm.ac.in/byroll.php?roll=" + rollNumber.upper()
    filePath = "images/" + rollNumber + ".jpg"
    urllib.urlretrieve(url, filePath)
    return filePath

def showImage(filePath):
    img = Image.open(filePath)
    img.show()

def displayData(details):
    # Create window to display data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--roll_number', help='Roll number', required=True)
    parser.add_argument('-s','--save', help='Save data')
    args = parser.parse_args()

    toSave = False
    if(args['save']):
        toSave = True

    rollNumber = args['roll_number']

    details = getDetails(rollNumber)
    imagePath = getImage(rollNumber)
    details['__image_path__'] = os.getcwd() + os.sep + imagePath

    displayData(details)




if __name__ == '__main__':
    main()
