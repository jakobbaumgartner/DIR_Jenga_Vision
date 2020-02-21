import numpy as np
import cv2

class cameraSettings:

    areaPointsX = []
    areaPointY = 0
    wait = True

    def getPoint(self, image):

        # To get X coordinates click twice left mouse button, to get Y click once right mouse button, 
        # to clear values click middle mouse button.

        # open image
        cv2.namedWindow('source', cv2.WINDOW_NORMAL)
        cv2.imshow('source', image)
        # get two clicks and save coordinates

        cv2.setMouseCallback('source', cameraSettings().getCoordinate, param = None)

        

        # while(self.wait):
        #     # keep waiting
        #     wait = True
        
        # return [self.areaPointsX(0), self.areaPointsX(1), self.areaPointY]



    def getCoordinate(self, event, x, y, flag, other):
        # print(str(x) + ' - ' + str(y))
        

        if(flag == 1):
            if(len(self.areaPointsX) < 2):
                print('-----------')
                self.areaPointsX.append(x)
                print(self.areaPointsX)
                print('-----------')
            
            else:
                print('ERROR - TOO MANY POINTS.')

        if(flag == 2):
            print('-----------')
            self.areaPointY = y
            print(self.areaPointY)
            print('-----------')

        if(flag == 4):
            # delete all values
            self.areaPointsX = []
            self.areaPointY = 0
            print('VALUES CLEARED, INPUT AGAIN.')
            return 0
        
        