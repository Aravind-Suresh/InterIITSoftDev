# Necessary imports
import os, sys, argparse
import json
from retreive import *
from search import *
import atexit

def deleteFile(path):
    os.remove(path)

# Path variables
DATA_PATH = os.getcwd() + os.sep + "data"
DATA_DETAILS_PATH = DATA_PATH + os.sep + "details"
DATA_IMAGE_PATH = DATA_PATH + os.sep + "images"

if __name__ == '__main__':
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--roll_number', help='Roll number', required=True)
    parser.add_argument('-s', '--save', help='Save data', action='store_true')
    parser.add_argument('-l', '--load', help='Search and load data', action='store_true')
    args = parser.parse_args()

    rollNumber = args.roll_number.upper()

    toSave = False
    if args.save:
        toSave = True

    toLoad = False
    if args.load:
        toLoad = True
        details = search(DATA_DETAILS_PATH, rollNumber)
        if details is None:
            print "Sorry. The content is not available offline."
            sys.exit()

    else:
        details = getDetails(rollNumber)
        imagePath = getImage(DATA_IMAGE_PATH, rollNumber)
        details['__image_path__'] = imagePath

    # Displaying student details and showing image
    displayData(details)

    if not toLoad and toSave:
        # Saving details to json file
        outFilePath = DATA_DETAILS_PATH + os.sep + rollNumber + ".json"
        with open(outFilePath, 'w') as outfile:
            json.dump(details, outfile)

    elif not toLoad and not toSave:
        # Removing the image file which was retrieved earlier
        atexit.register(deleteFile, details['__image_path__'])
