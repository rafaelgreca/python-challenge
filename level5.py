#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

import urllib.request
import re
import pickle

def getDataWebsite(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return str(resp.read())

def getImage(data):
    nothing = re.findall(r'<peakhell\s+src="(.*?)"/>', str(data))
    return str(nothing[0])

def downloadImage(url, path):
    req = urllib.request.Request(url+path)
    resp = urllib.request.urlopen(req)
    image = urllib.request.urlretrieve(url+path, "banner.p")
    
url = "http://www.pythonchallenge.com/pc/def/peak.html"

data = getDataWebsite(url)
image_path = getImage(data)

url = "http://www.pythonchallenge.com/pc/def/"
downloadImage(url, image_path)

peak_file = open("banner.p", 'rb')
file = pickle.load(peak_file)
peak_file.close()

for lis in file:
    print (''.join(i[0] * i[1] for i in lis))