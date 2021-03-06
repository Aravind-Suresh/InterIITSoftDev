# Necessary imports
import urllib, urllib2
from bs4 import BeautifulSoup
from PIL import Image
import os
import Tkinter as ttk

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

def getImage(path, rollNumber):
    url = "https://photos.iitm.ac.in/byroll.php?roll=" + rollNumber.upper()
    filePath = path + os.sep + rollNumber + ".jpg"
    urllib.urlretrieve(url, filePath)
    return filePath

def showImage(filePath):
    img = Image.open(filePath)
    img.show()

def displayData(details):
    root = ttk.Tk()
    idx = 0
    for key in details:
        if key == '__image_path__':
            continue
        ttk.Label(root, text=key).grid(column=0, row=idx)
        ttk.Label(root, text=details[key]).grid(column=1, row=idx)
        idx += 1

    showImage(details['__image_path__'])
    root.mainloop()
