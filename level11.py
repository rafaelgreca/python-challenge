#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

from PIL import Image
import numpy

image = Image.open('cave.jpg')

array_pixels = numpy.asarray(image)
height = image.height

odds = []

for i in range(height):
    if i%2==0:
        odds.append(array_pixels[i][::2])

Image.fromarray(numpy.array(odds)).show()