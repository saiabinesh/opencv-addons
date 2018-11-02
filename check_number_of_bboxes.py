# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np

global filename

# client = airsim.VehicleClient()
# client.confirmConnection()

# ###################################################################################################################
# #Setting all object IDs to 0
# found = client.simSetSegmentationObjectID("[\w]*", 0, True);
# print("Set everything to 0 color code: %r" % (found))

# #below code didn't work beacause currently in computerVision mode
# #client.moveToPositionAsync(273, -7167, 1036, 10, 0).join() # , DrivetrainType.ForwardOnly, YawMode(False,0), 20, 1) 

# found = client.simSetSegmentationObjectID("FbxScene_PickupTruck[\w]*", 2, True);
# print("found FbxScene_PickupTruck? ",found)
# found = client.simSetSegmentationObjectID("KamazNov2[\w]*", 2, True);
# print("found KamazNov2? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_JCB2[\w]*", 2, True);
# print("found FbxScene_JCB2? ",found)
# found = client.simSetSegmentationObjectID("Cube_2[\w]*", 2, True); #Floor mat of the pickup truck which is of a different ID
# print("found Cube_2? ",found) 


# #Set train alone to 1. Means setting the cars as well
# # found = client.simSetSegmentationObjectID("cannopcart[\w]*", 2, True);
# # print("found cannopcart? ",found)
# # found = client.simSetSegmentationObjectID("FbxScene_GraveCart[\w]*", 2, True);
# # print("found FbxScene_GraveCart? ",found)
# # found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# # print("found FbxScene_GraveCart? ",found)
# # found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# # print("found FbxScene_train_model? ",found)


def analyze_bounding_boxes(filename): #without extension
	img = cv.imread(filename+'.jpg',0)
	color = [255, 255, 255] # 'white color
	top, bottom, left, right = [1]*4
	img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color) #drawing border to recognize contours of partial objects
	ret,thresh = cv.threshold(img_with_border,127,255,0) #converting to bw format first
	im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
	print("Number of contours :", len(contours))
	print("datatype of contours: ", type(contours))
	rectangle_areas_dictionary = {}


	#Extracting the coorindates of the biggest enclosing rectangle
	min_x, min_y, max_x, max_y = 1025,1025,0,0
	counter = 1
	for contour in contours[:-1]: #ignoring the last contour because it's the one around the whole picture
	    # get rectangle bounding contour
		[x,y,w,h] = cv.boundingRect(contour)
		rectangle_areas_dictionary[str(counter)] = w*h
		cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		counter = counter + 1
	print("Size of rectangle_areas_dictionary: ",len(rectangle_areas_dictionary))
	sorted_areas = sorted(rectangle_areas_dictionary.values(),reverse = True)
	#for area in sorted_areas[0:2]:
	for contour_no, dict_area in rectangle_areas_dictionary.items():    # for name, age in list.items():  (for Python 3.x)
	    if dict_area in sorted_areas[0:10]:
	        print(contour_no," - Area: ",dict_area )		

	final_cropped_img = img[1:1025, 1:1025]
	cv.imwrite(filename+"_bbox"+".jpg", final_cropped_img)


analyze_bounding_boxes("D:/AirSim/New/Images/Images_gas_cylinders/segmented_gas_cylinders_187")
# #Change the code below to move the camera to desired position
# i =1
# for z in np.linspace(-30,-100,10):
# 	for x in np.linspace(2.93,-37.37, 10):
# 		for y in np.linspace(-88.17, -192.27,10):
# 			global filename
# 			client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
# 			#print(client.simGetCameraInfo("0"))
# 			responses = client.simGetImages([
# 			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
# 			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
# 			airsim.ImageRequest("3", airsim.ImageType.Scene, False, False),
# 			airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
# 			#print('Retrieved images: %d', len(responses))
# 			#save segmentation images in various formats
# 			for idx, response in enumerate(responses):
# 				global filename
# 				if idx== 0:
# 					filename = 'D:/AirSim/New/Images/Images_truck/original_'+str(i)
# 				else:
# 					filename = 'D:/AirSim/New/Images/Images_truck/segmented_truck_'+str(i)
# 				if response.pixels_as_float:
# 					#print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
# 					airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
# 				elif response.compress: #png format
# 					#print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
# 					airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
# 				else: #uncompressed array - numpy demo
# 					#print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
# 					img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
# 					img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
# 					img_rgba = np.flipud(img_rgba) #original image is flipped vertically
# 					airsim.write_png(os.path.normpath(filename + '.jpg'), img_rgba) #write to jpg
# 			draw_bounding_box(filename)
# 			print("Image count = ", i)
# 			i = i +1








