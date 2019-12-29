# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
# Working on the newer environement with new houses, cars and river (extended by Sean). 
# changed image folder in line 39. Commenting out 

from AirSimClient import *
import setup_path 
import airsim
import datetime
import time

import os
import numpy as np
import math

#client = airsim.VehicleClient()
client = MultirotorClient()
client.confirmConnection()
#Change the code below to move the camera to desired position
i =1 #starting from 400 as already 400 images captured
#Changing coordinates for new environment images
#for z in np.linspace(-10,-50,4):
start_time = datetime.datetime.now()

for z in [-10]:
	for x in np.linspace(-5,5,11):
		for y in np.linspace(-5,5,11):
	# for x in [9.600925314]:
		# for y in [-91.89895572]:
			# for roll in np.linspace(-30,30,3):
				# for pitch in np.linspace(45,0,2):
			for roll in [0]:
				for pitch in [0]:
					one_degree_in_radians = (math.pi)/180
					pitch_in_radians=pitch * one_degree_in_radians
					roll_in_radians=roll * one_degree_in_radians
					# The handy `airsim.to_quaternion()` function allows to convert pitch, roll, yaw to quaternion
					# client.simSetCameraOrientation(0, airsim.to_quaternion(0, radians, 0)); #radians
					client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(pitch_in_radians,roll_in_radians,0)), True)
					#print(client.simGetCameraInfo("0"))
					responses = client.simGetImages([
					airsim.ImageRequest("3", airsim.ImageType.Scene, False, False)])
					for idx, response in enumerate(responses):
						filename = 'D:/AirSim/New/Images/Images_master_v7/image_' +str(i)+'_raw' 
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
							airsim.write_png(os.path.normpath(filename + '.png'), img_rgba) #write to png 
						if i%100 == 0:
							print("Image count = ", i)
						# if i>= 45:
							# exit()

						i = i +1
print("--- %s minutes ---" % ((datetime.datetime.now() - start_time)/60))

# #        #find unique colors
# #        print(np.unique(img_rgba[:,:,0], return_counts=True)) #red
# #        print(np.unique(img_rgba[:,:,1], return_counts=True)) #green
# #        print(np.unique(img_rgba[:,:,2], return_counts=True)) #blue  
# #        print(np.unique(img_rgba[:,:,3], return_counts=True)) #blue