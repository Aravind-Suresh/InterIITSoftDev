import urllib
import os, sys
import argparse
from PIL import Image

def getDetails(rollNumber):
    details = {}
    # TODO: Parse hostel CCW page and store results
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
    parser.add_argument('-s','--save', help='Save data')
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
