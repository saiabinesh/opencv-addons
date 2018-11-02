# This program just creates separate png masks for each instance of the gas cylinder object. Then writes out those coordinates to 
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

# Check if object is present in the image in filename and if so, append a binary flag onto a list, that the object is present
def check_object_present(filename,image_count,cylinder_exists_list):
	img = cv.imread(filename+'.png',0)
	color = [255, 255, 255] # 'white color
	top, bottom, left, right = [1]*4
	img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color) #drawing border to recognize contours of partial objects
	ret,thresh = cv.threshold(img_with_border,127,255,0) #converting to bw format first
	im2,contours,hierarchy = cv.findContours(thresh, 1, 2)

	#Extracting the coorindates of the biggest enclosing rectangle
	if len(contours)>1:
        # Ignoring the following lines because there will only be one contour
		# for contour in contours[:-1]: #ignoring the last contour because it's the one around the whole picture
			# [x,y,w,h] = cv.boundingRect(contour)
			# if w*h>100: #To avoid really small and complex contours that we do not need
		cylinder_exists_list.append(1)
	else:
		cylinder_exists_list.append(0)
		if(os.path.isfile(filename + '.png')):
			os.remove(filename + '.png')
	return(cylinder_exists_list)

#Change the code below to move the camera to desired position
object_count = 0
#The following counter to create a set of 100 test images to check whether changing the color of objects in the middle of the code works 
cylinder_numbers = [8,9,10,11,12]

def create_cylinder_masks():
    for cylinder_number in cylinder_numbers:
        #Setting all object IDs to 0 and all the gas cylinder tanks to a specific ID
        object_count = object_count + 1
        found = client.simSetSegmentationObjectID("[\w]*", 0, True);
        print("Set everything to 0 color code: %r" % (found))
        found = client.simSetSegmentationObjectID("Propane_Tank_E_Blueprint"+str(cylinder_number), 2, True);
        print("Setting color for Propane_Tank_E_Blueprint"+str(cylinder_number),found)
        i =1 #resetting i, the image count, before moving on to the next instance of the object
        cylinder_exists_list = [] #initializing a list that can hold whether a cylinder exists in each of these images
        for z in np.linspace(-30,-100,10):
            for x in np.linspace(2.93,-37.37, 10):
                for y in np.linspace(-88.17, -192.27,10):
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
                        filename = 'D:/AirSim/New/Images/Images_master/image_'+str(i)+'_gas cylinder_'+str(object_count)
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
                    cylinder_exists_list = check_object_present(filename, i,cylinder_exists_list)
                    print("Image count = ", i)
                    i = i +1
        #####################################################################################################
        ################################ Change filename for other objects ##################################
        text_filename = "list_gas_cylinder_"+str(object_count)+".txt"
        buffsize=1
        file = open(text_filename,"a+",buffsize)
        print("Object count: ",object_count )
        print(cylinder_exists_list)
        for item in cylinder_exists_list:
            file.write("%s\n" % item) 

                
def delete_empty_images(folder):
    file_names = [f.name for f in os.scandir(folder)]
    for file in file_names:
        full_file_path = os.path.join(folder, file)
        # print(full_file_path)
        img = cv.imread(full_file_path,0)
        # Testing if the image has been read properly. It works . and the image is recreated. No issues with that. The following error was created due to not specifying the grayscale flag in previous line
        # print(img[0])
        # cv.imwrite("Test image.jpg", img)
        ret,thresh = cv.threshold(img,127,255,0)
        # print(thresh)
        im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
        ############Creating an empty list to write the contours information into a text file to analyze logs###########
        info_list = []
        # info_list.append("For image in file:",file)
        # info_list.append("Number of contours = ",len(contours))
        filename = 'number_of_contours_log.txt'
        buffsize=1
        file = open(filename,"a+",buffsize)
        for item in info_list:
            file.write("%s\n" % item) 
        file.write("\n")
        

def test_check_object_present():
    object_count = 0
    for cylinder_number in cylinder_numbers:
        #Setting all object IDs to 0 and all the gas cylinder tanks to a specific ID
        object_count = object_count + 1
        # found = client.simSetSegmentationObjectID("[\w]*", 0, True);
        # print("Set everything to 0 color code: %r" % (found))
        # found = client.simSetSegmentationObjectID("Propane_Tank_E_Blueprint"+str(cylinder_number), 2, True);
        # print("Setting color for Propane_Tank_E_Blueprint"+str(cylinder_number),found)
        i =1 #resetting i, the image count, before moving on to the next instance of the object
        cylinder_exists_list = [] #initializing a list that can hold whether a cylinder exists in each of these images

        for z in np.linspace(-30,-100,10):
            for x in np.linspace(2.93,-37.37, 10):
                for y in np.linspace(-88.17, -192.27,10):
                    global filename
                    filename = 'D:/AirSim/New/Images/Images_master/image_'+str(i)+'_gas cylinder_'+str(object_count)
                    cylinder_exists_list = check_object_present(filename, i,cylinder_exists_list)
                    if i%50 == 0:
                        print("Image count = ", i)
                    i = i +1
        text_filename = "list_gas_cylinder_"+str(object_count)+".txt"
        buffsize=1
        file = open(text_filename,"a+",buffsize)
        print("Object count: ",object_count )
        print(cylinder_exists_list)
        for item in cylinder_exists_list:
            file.write("%s\n" % item) 

#Checking the number of contours in a few files before actually deciding the criteria for deleting empty images
#delete_empty_images("D:/AirSim/New/Images/Test_images_contour_detection")

test_check_object_present()