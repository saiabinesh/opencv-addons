#resize_image_camera_check_scale_invariance
import cv2
import os
#current_image_directory = "C:\\Projects\\mask_rcnn_retrain\\images"
current_image_directory = "D:\\AirSim\\New\\Images\\Real images from lab\\test_members"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1

for file in os.listdir(current_image_directory):
	#print(file)
	filename = os.path.join(current_image_directory,file)
	oriimg = cv2.imread(filename)
	scale_percent = 33 # percent of original size
	width = int(oriimg.shape[1] * scale_percent / 100)
	height = int(oriimg.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized_image = cv2.resize(oriimg, dim, interpolation = cv2.INTER_AREA) 
	#resized_image = cv2.resize(oriimg, (640,853)) #dimensions are width, height
	new_filename = "C:\\Projects\\mask_rcnn_retrain\\images\\"+file
	cv2.imwrite(new_filename,resized_image)
	if counter%2==0:
		print(counter)
	counter = counter + 1