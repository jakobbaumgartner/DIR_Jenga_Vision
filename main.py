# Plan here is to get image coordinates of all the dots, 
# decide out of them somehow which are on same vertical 
# level and on which parts are they.



import numpy as np
import cv2
import json
import imutils

from optional import optional
from importer import importer
from recognizer import recognizer
from cameraSettings import cameraSettings

settings = cameraSettings()


image = importer.getImage('camera0')[0]
source = importer.getImage('camera0')[1]


coordinates = recognizer.getDots(source, np.array([28, 180, 125]), np.array([40, 255, 180]), 60, 255)

optional.printImages(image,coordinates)

recognizer.simpleArray(coordinates, image.shape[1], 400)

cameraSettings.getPoint(cameraSettings, image)




cv2.waitKey(0)