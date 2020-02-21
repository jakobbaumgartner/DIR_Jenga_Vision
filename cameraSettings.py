import numpy as np
import cv2

class cameraSettings:

    areaPointsX = []
    areaPointY = 0
    wait = True

    def getPoint(self, image):

        # To get X coordinates click twice left mouse button, to get Y click once right mouse button, 
        # to clear values click middle mouse button. To save values press altkey and move mouse just a bit.

        # open image
        cv2.namedWindow('settings', cv2.WINDOW_NORMAL)
        cv2.imshow('settings', image)
        # get two clicks and save coordinates

        cv2.setMouseCallback('settings', self().getCoordinate, param = None)
      
   

     



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
        
        if (flag == cv2.EVENT_FLAG_ALTKEY):
            print('SAVED')
        
        