# This program just creates separate png masks for each instance of the gas truck object. Then writes out those coordinates to 
# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np
global filename
import time
import csv
import datetime

client = airsim.VehicleClient()
client.confirmConnection()

def csv_to_list_of_strings(filename_to_convert):
	with open(filename_to_convert) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		# print("type(csv_reader) = ",type(csv_reader))
		list_of_object_IDs = []
		for line in csv_reader:
			# print(line)
			list_of_object_IDs.append(line[0])
	return(list_of_object_IDs)


# Check if object is present in the image in filename and if so, append a binary flag onto a list, that the object is present
def check_object_present(filename,image_count,object_exists_list):
	img = cv.imread(filename+'.png',0)
	color = [255, 255, 255] # 'white color
	top, bottom, left, right = [1]*4
	img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color) #drawing border to recognize contours of partial objects
	ret,thresh = cv.threshold(img_with_border,127,255,0) #converting to bw format first
	im2,contours,hierarchy = cv.findContours(thresh, 1, 2)

	#Extracting the coorindates of the biggest enclosing rectangle
	if len(contours)>1:
		object_exists_list.append(1)
	else:
		object_exists_list.append(0)
		if(os.path.isfile(filename + '.png')):
			os.remove(filename + '.png')
	return(object_exists_list)

#The following counter to create a set of 100 test images to check whether changing the color of objects in the middle of the code works 

# This function is similar to create_truck_masks, but slightly different because all the truck objects have different mesh id names that are not serial number formats. 
def create_object_masks(object_IDs_list, class_label, image_directory):
    print("Object ID list: ",object_IDs_list)
    start_time = time.time()
    object_count = 0
    for object_ID in object_IDs_list:
        #Setting all object IDs to 0 and all the gas truck tanks to a specific ID
        object_count = object_count + 1
        found = client.simSetSegmentationObjectID("[\w]*", 0, True);
        # print("Set everything to 0 color code: %r" % (found))
        ################################################################################################################
        ##################################### Change object ID below ###################################################
        found = client.simSetSegmentationObjectID(object_ID, 2, True);
        print("Setting color for "+str(object_ID)+": "+str(found))
        i =1 #resetting i, the image count, before moving on to the next instance of the object
        object_exists_list = [] #initializing a list that can hold whether a truck exists in each of these images
        for z in np.linspace(-10,-50,4):
            for x in np.linspace(-150,0, 10):
                for y in np.linspace(-60,-240,10):
                    global filename
                    client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
                    #print(client.simGetCameraInfo("0"))
                    responses = client.simGetImages([
                    #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
                    #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
                    #airsim.ImageRequest("3", airsim.ImageType.Scene, False, False),
                    airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
                    #print('Retrieved images: %d', len(responses))
                    #save segmentation images in various formats
                    for idx, response in enumerate(responses):
                        global filename
                        #################################################################################################
                        ############################ Image directory here ###############################################
                        filename = str(image_directory)+'/image_'+str(i)+'_'+str(class_label)+'_'+str(object_count)
                        if response.pixels_as_float:
                            #print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
                            airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
                        elif response.compress: #png format
                            #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                            airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
                        else: #uncompressed array - numpy demo
                            #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                            img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
                            img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
                            img_rgba = np.flipud(img_rgba) #original image is flipped vertically
                            airsim.write_png(os.path.normpath(filename + '.png'), img_rgba) #write to jpg
                    object_exists_list = check_object_present(filename, i,object_exists_list)
                    # if i%100 == 0:
                        # # print("Image count = ", i)
                    i = i+1
        #####################################################################################################
        ################################ Change filename for other objects ##################################
        text_filename = "list_"+str(class_label)+"_"+str(object_count)+".txt"
        buffsize=1
        file = open(text_filename,"a+",buffsize)
        print("Object count: ",object_count )
        print(datetime.datetime.now().time())
        # print(object_exists_list)
        for item in object_exists_list:
            file.write("%s\n" % item) 

        
#Checking the number of contours in a few files before actually deciding the criteria for deleting empty images
#delete_empty_images("D:/AirSim/New/Images/Test_images_contour_detection")

#Storing all the function parameters in master_csv.csv
master_filename= 'D:/List_of_object_IDs/master_csv.csv'
with open(master_filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	# print("type(csv_reader) = ",type(csv_reader))
	master_csv = []
	for line in csv_reader:
		# print(line)
		master_csv.append(line)


current_image_directory = "D:/AirSim/New/Images/Images_master_v2"
for file_name,label in master_csv:
	start_time = time.time()
	list_of_object_IDs = csv_to_list_of_strings(file_name)
	create_object_masks(list_of_object_IDs, label, current_image_directory)
	print("Time taken for masks of class :", label)
	print("--- %s minutes ---" % ((time.time() - start_time)/60))


