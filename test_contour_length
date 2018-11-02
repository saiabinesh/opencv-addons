import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np

global filename
i=1
filename = 'D:/AirSim/New/Images/Images_master/original_'+str(i)
img = cv.imread(filename+'.jpg',0)
color = [255, 255, 255] # 'white color
top, bottom, left, right = [1]*4
img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color) #drawing border to recognize contours of partial objects
ret,thresh = cv.threshold(img_with_border,127,255,0) #converting to bw format first
im2,contours,hierarchy = cv.findContours(thresh, 1, 2)

print(len(contours))