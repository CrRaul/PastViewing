import numpy as np
import cv2


point = []
x = 0
y = 0
for i in range(0,11):
	x = np.cos(np.radians((30*i)))*200
	y = np.sin(np.radians((30*i)))*200
	point.append([x,y])


i = 0
while True:
	blank_image = np.zeros((500,500,3), np.uint8)
	blank_image[:,:] = (0,0,0)

	#cv2.circle(blank_image, (250,250), 200, (255,255,255),1)

	cv2.circle(blank_image, (50,250), 30, (225,225,225),3)
	cv2.circle(blank_image, (450,250), 30, (225,225,225),3)
	cv2.circle(blank_image, (250,50), 30, (225,225,225),3)
	cv2.circle(blank_image, (250,450), 30, (225,225,225),3)
	
	cv2.circle(blank_image, (int(point[i][0])+250,int(point[i][1])+250), 15, (225,225,225),25)					

	cv2.imshow('image', blank_image)
	cv2.waitKey(50)

	i += 1
	if i == 11:
		i = 0


