# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
import sys
import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np



img = cv.imread("D:/AirSim/New/Images/Images_batch2/with_Border.jpg",0)
print("image type = ",type(img))
np.savetxt("Numpy_with_Border.txt", img, newline=" ")
print(img.shape)
print(img[0])
print(np.unique(img))


img = cv.imread('D:/AirSim/New/Images/Images_batch2/py_seg_new_1 1.numpy.png',0)
color = [255, 255, 255] # 'cause purple!
# border widths; I set them all to 150
top, bottom, left, right = [1]*4
img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color)
ret,thresh = cv.threshold(img_with_border,127,255,0)
im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
print(im2.shape)
print(im2[0])
print(np.unique(im2))
#print(len(contours))
#cv.imwrite("D:/AirSim/New/Images/Images_batch2/with_Border.jpg", im2)
#cnt = contours[len(contours)-1]
#M = cv.moments(cnt)
#print( M )

# x,y,w,h = cv.boundingRect(cnt)
# print(" x: "+str(x)+" y: "+str(y)+" w: "+str(w)+" h: "+str(h))
# rect = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect_lastcontour.jpg", rect)

# x,y,w,h = cv.boundingRect(cnt)
# print(" x: "+str(x)+" y: "+str(y)+" w: "+str(w)+" h: "+str(h))
# rect = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect.jpg", rect)

# #Extracting the coorindates of the biggest enclosing rectangle
# min_x, min_y, max_x, max_y = 1025,1025,0,0
# for contour in contours[:-1]: #ignoring the last contour because it's the one around the whole picture
#     # get rectangle bounding contour
#     [x,y,w,h] = cv.boundingRect(contour)
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


#     #Below code for finding the largest enclosing rectange of all of rectangles
#     # if x<min_x:
#     # 	min_x=x
#     # 	#print(x,min_x)
#     # if y<min_y:
#     # 	min_y=y
#     # if x+w>max_x:
#     # 	max_x=x+w
#     # 	#print(max_x,x+w)
#     # if y+h>max_y:
#     # 	max_y=y+h   	    	
#     # draw rectangle around contour on original image

# #print(min_x, min_y, max_x, max_y)
# #cv.rectangle(im2,(min_x,min_y),(max_x, max_y),(0,255,0),2)
# crop_img = im2[1:1025, 1:1025]
# cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect_cropped.jpg", crop_img)


# exif_data = 
# {
# "width"
# : int,
# "height"
# : int,
# "category"
# : int,
# "bbox"
# : [x,y,width,height],
# "iscrowd"
# : 0 or 1,
# "category_id"
# }






