import numpy as np
import cv2

class cameraSettings:
    def getPoint(image):

        # open image
        cv2.namedWindow('source', cv2.WINDOW_NORMAL)
        cv2.imshow('source', image)
        # get two clicks and save coordinates
        count = 0

        cv2.setMouseCallback('source', cameraSettings().getCoordinate, param = None)


    def getCoordinate(self, event, x, y, flag, other):
        print(str(x) + ' - ' + str(y))