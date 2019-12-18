import numpy as np
import cv2

class importer:

	def getImage(open):

		# different source imports
		
		if open == 'file':
			image = cv2.imread('./kamera_m0/IMG_20191218_193049.jpg')
			source = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		return [image, source]
		