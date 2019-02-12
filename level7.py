#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

from PIL import Image
import urllib.request
import re

def downloadImage():
    image = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png', 'oxygen.png')

def get_RGB_values():
    image = Image.open('oxygen.png')
    rgb_image = image.convert('RGB')
    rgb_list = []
    r = rgb_image.getpixel((4,(image.height)/2))
    rgb_list.append(r)

    X = 5
    while (image.width-29) > X:
        r = rgb_image.getpixel((X,(image.height)/2))
        rgb_list.append(r)
        X+=7

    rgb_value = []

    for rgb in rgb_list:
        rgb_value.append(rgb[0])
    
    return rgb_value

def RGB_to_char(rgbs):
    chars = []

    for rgb in rgbs:
        chars.append(chr(rgb))
    
    return chars

downloadImage()
rgbs = get_RGB_values()
#print("".join(RGB_to_char(rgbs)))
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join(RGB_to_char(next_level)))