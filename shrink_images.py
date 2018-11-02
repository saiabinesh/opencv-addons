import cv2
import os
for image_number in [2,12,22]:
	color_mask_file_name = "D:/AirSim/New/Images/coco/train2014/segmented_train_"+str(image_number)+".jpg" 
	img = cv2.imread(color_mask_file_name,1) 
	height, width = img.shape[:2]
	print(height,width)
	res = cv2.resize(img,(512, 512), interpolation = cv2.INTER_AREA)
	cv2.imwrite("D:/AirSim/New/Images/coco/train2014/segmented_train_"+str(image_number)+".jpg",res)