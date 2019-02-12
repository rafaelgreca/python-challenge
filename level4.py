#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

import urllib.request
import re

def getDataWebsite(url, value_nothing):
    req = urllib.request.Request(url+value_nothing)
    resp = urllib.request.urlopen(req)
    return str(resp.read())

def getNothingValue(data):
    nothing = re.search(r"\d+", str(data))
    return str(nothing.group())

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
value_nothing = "12345"

for i in range(250):
    data = getDataWebsite(url, value_nothing)
    
    if value_nothing == '16044':
        value_nothing = '8022'
    elif value_nothing == '82682':
        value_nothing = '63579'
    else:
        value_nothing = getNothingValue(data)

answer = getDataWebsite(url, value_nothing)
print(answer)