# Necessary imports
import os
import json

def search(path, rollNumber):
    fileList = os.listdir(path)
    try:
        idx = fileList.index(rollNumber + ".json")
    except ValueError:
        return None

    with open(path + os.sep + fileList[idx]) as dataFile:
        details = json.load(dataFile)

    return details
