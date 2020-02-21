import numpy as np
import cv2

class importer:

	def getImage(open):

		# different source imports
		
		if open == 'file':
			image = cv2.imread('./kamera_m0/b1.jpg')
			source = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		if open == 'camera0':
			cap = cv2.VideoCapture(1)
			ret, frame = cap.read()
			source = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			cap.release()
			image = frame

		if open == 'camera1':
			cap = cv2.VideoCapture(2)
			ret, frame = cap.read()
			source = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			cap.release()
			image = frame

		# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

		return [image, source]

		