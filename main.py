# Plan here is to get image coordinates of all the dots, 
# decide out of them somehow which are on same vertical 
# level and on which parts are they.



import numpy as np
import cv2

from optional import optional
from importer import importer
from recognizer import recognizer
from cameraSettings import cameraSettings


image = importer.getImage('file')[0]
source = importer.getImage('file')[1]


coordinates = recognizer.getDots(source, np.array([40, 100, 0]), np.array([190, 255, 255]), 60, 255)

optional.printImages(image,coordinates)

recognizer.simpleArray(coordinates, image.shape[1], 150)

cameraSettings.getPoint(image)

# wait before exit
cv2.waitKey(0)