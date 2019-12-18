import numpy as np
import cv2

class recognizer:
	
	def getDots (source, low, high, treshold, max_treshold):
		
		# source is HSV file 

		# low and high are settings for green levels in numpy format, look example:
		# low_filter = np.array([40, 100, 0])
		# high_filter = np.array([190, 255, 255])

		# treshold and max_treshold are settings for contour

		# set color filter and run it on the image
		mask = cv2.inRange(source, low, high)
		#filter out dots with mask
		dots = cv2.bitwise_and(source, source, mask=mask) 

		# convert from HSV to RGB, than to GRAY and use blurring 
		dotsRGB = cv2.cvtColor(dots, cv2.COLOR_HSV2RGB)
		dotsGray = cv2.cvtColor(dotsRGB, cv2.COLOR_RGB2GRAY)
		dotsGraybl = cv2.blur(dotsGray, (5,5))

		# using tresholding convert form GRAY to B&W
		retval, dotsBW = cv2.threshold(dotsGraybl, treshold, max_treshold,	cv2.THRESH_BINARY) 

		# contour returns just a couple of points for every 'dot'
		cnts = cv2.findContours(dotsBW.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


		# for every point out of contour get coordinates and calculate an average of x and y. That is the center of
		# our dots. The dots are kind of 'circular', so it should be quite accurate.
		coordinates = []
		# dotsRGBc = dotsRGB

		for element in cnts[0]:
			count = 0
			x = 0
			y = 0

			for tocka in (element):
				count+=1

				x = x + tocka[0][0]
				y= y + tocka[0][1]

				
			coordinates.append([int(x/count), int(y/count)])

		print('\n-------------------------------------------------------')
		print('\n  List of coordinates: \n')
		print(coordinates)

		return coordinates

