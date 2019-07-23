# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
import sys
import setup_path 
import airsim
import os
import cv2 
import numpy as np



# img = cv.imread("D:/AirSim/New/Images/Images_batch2/with_Border.jpg",0)
# print("image type = ",type(img))
# np.savetxt("Numpy_with_Border.txt", img, newline=" ")
# print(img.shape)
# print(img[0])
# print(np.unique(img))


img = cv2.imread('D:/AirSim/New/Images/Images_master_v2/image_61_raw.png')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# cv2.imshow('Color input image', img)
# cv2.imshow('Histogram equalized', img_output)
cv2.imwrite('D:/AirSim/New/Images/Misc_test/Rotate_equalize/clahe_2.jpg',img_output)


# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
# cv2.imwrite('D:/AirSim/New/Images/Misc_test/Rotate_equalize/clahe_2.jpg',cl1)
