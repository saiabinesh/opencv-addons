# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np

global filename

client = airsim.VehicleClient()
client.confirmConnection()

###################################################################################################################
#Setting all object IDs to 0
found = client.simSetSegmentationObjectID("[\w]*", 0, True);
print("Set everything to 0 color code: %r" % (found))

#below code didn't work beacause currently in computerVision mode
#client.moveToPositionAsync(273, -7167, 1036, 10, 0).join() # , DrivetrainType.ForwardOnly, YawMode(False,0), 20, 1) 

found = client.simSetSegmentationObjectID("Propane_Tank_E_Blueprint[\w]*", 2, True);
print("found Propane_Tank_E_Blueprint? ",found)

#Checking if in the first 100 images, Propane_Tank_E_Blueprint9 is found or not
counter = 0 
for z in np.linspace(-30,-100,10):
	for x in np.linspace(2.93,-37.37, 10):
		for y in np.linspace(-88.17, -192.27,10):
		    found = client.simSetSegmentationObjectID("Propane_Tank_E_Blueprint9", 2, True)
		    print("found Propane_Tank_E_Blueprint? ",found)
		    if not found:
		        print("found Propane_Tank_E_Blueprint? ",found)
		    if counter == 100:
		        break   
		    counter = counter + 1



# found = client.simSetSegmentationObjectID("FbxScene_PickupTruck[\w]*", 2, True);
# print("found FbxScene_PickupTruck? ",found)
# found = client.simSetSegmentationObjectID("KamazNov2[\w]*", 2, True);
# print("found KamazNov2? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_JCB2[\w]*", 2, True);
# print("found FbxScene_JCB2? ",found)
# found = client.simSetSegmentationObjectID("Cube_2[\w]*", 2, True); #Floor mat of the pickup truck which is of a different ID
# print("found Cube_2? ",found) 

#Set train alone to 1. Means setting the cars as well
# found = client.simSetSegmentationObjectID("cannopcart[\w]*", 2, True);
# print("found cannopcart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_GraveCart[\w]*", 2, True);
# print("found FbxScene_GraveCart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# print("found FbxScene_GraveCart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# print("found FbxScene_train_model? ",found)




# def draw_bounding_box(filename,image_count):
	# img = cv.imread(filename+'.jpg',0)
	# color = [255, 255, 255] # 'white color
	# top, bottom, left, right = [1]*4
	# img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color) #drawing border to recognize contours of partial objects
	# ret,thresh = cv.threshold(img_with_border,127,255,0) #converting to bw format first
	# im2,contours,hierarchy = cv.findContours(thresh, 1, 2)

	# #Extracting the coorindates of the biggest enclosing rectangle
	# bounding_box_coordinates = []
	# object_count = 0
	# if len(contours)>1:
		# for contour in contours[:-1]: #ignoring the last contour because it's the one around the whole picture
		    # # get rectangle bounding contour
			# [x,y,w,h] = cv.boundingRect(contour)
			# if w*h>100:
				# cv.rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2) #To avoid really small and complex contours that we do not need
				# object_count = object_count + 1
				# centre_x, centre_y = x+w/2, y+h/2 #since x and y are center coordinates
				# bounding_box_coordinates.append("object: gas_cylinder_"+str(object_count)+", x: "+str(centre_x)+", y: "+str(centre_y)+", width: "+str(w)+", height: "+str(h))
		# if(len(bounding_box_coordinates)!=0):
			# print(bounding_box_coordinates)
			# with open("D:/AirSim/New/Images/Images_master/gas_cylinder_bbox_coordinates_"+str(image_count)+".txt", "w+") as file:
				# file.write(','.join(map(repr, bounding_box_coordinates)))
		# final_cropped_img = im2[1:2001, 1:2001]
		# cv.imwrite(filename+"_bbox"+".jpg", final_cropped_img)
	# else:
		# os.remove(filename + '.jpg')

# #Change the code below to move the camera to desired position
# i =1
# for z in np.linspace(-30,-100,10):
	# for x in np.linspace(2.93,-37.37, 10):
		# for y in np.linspace(-88.17, -192.27,10):
			# global filename
			# client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
			# #print(client.simGetCameraInfo("0"))
			# responses = client.simGetImages([
			# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
			# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
			# #airsim.ImageRequest("3", airsim.ImageType.Scene, False, False),
			# airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
			# #print('Retrieved images: %d', len(responses))
			# #save segmentation images in various formats
			# for idx, response in enumerate(responses):
				# global filename
				# filename = 'D:/AirSim/New/Images/Images_master/segmented_gas_cylinders_'+str(i)
				# if response.pixels_as_float:
					# #print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
					# airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
				# elif response.compress: #png format
					# #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
					# airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
				# else: #uncompressed array - numpy demo
					# #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
					# img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
					# img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
					# img_rgba = np.flipud(img_rgba) #original image is flipped vertically
					# airsim.write_png(os.path.normpath(filename + '.jpg'), img_rgba) #write to jpg
			# draw_bounding_box(filename, i)
			# print("Image count = ", i)
			# i = i +1
