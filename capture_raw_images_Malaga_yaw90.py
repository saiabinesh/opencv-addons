# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
# Working on the newer environement with new houses, cars and river (extended by Sean). 
# changed image folder in line 39. Commenting out 


import setup_path 
import airsim
import os

import numpy as np

client = airsim.VehicleClient()
client.confirmConnection()

# below code didn't work beacause currently in computerVision mode
# client.moveToPositionAsync(273, -7167, 1036, 10, 0).join() # , DrivetrainType.ForwardOnly, YawMode(False,0), 20, 1) 

#Change the code below to move the camera to desired position
i =1
# for z in np.linspace(-30,-100,10):
	# for x in np.linspace(2.93,-37.37, 10):
		# for y in np.linspace(-88.17, -192.27,10):
		
###############################Trying to change weather ###############################################
# client.simEnableWeather(True)

# airsim.wait_key('Press any key to enable rain at 25%')
# client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 0.25);

# exit()
		
#Trying different cameras with just 8 images 
# for camera_number in ["0","1","2","3","4"]:
	# for z in np.linspace(-30,-100,3):
		# for x in np.linspace(-150,-30, 3):
			# for y in np.linspace(-60,-240,3):
				# client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
				# #print(client.simGetCameraInfo("0"))
				# responses = client.simGetImages([
				# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
				# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
				# airsim.ImageRequest(camera_number, airsim.ImageType.Scene, False, False)])
				# # airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
				# #print('Retrieved images: %d', len(responses))
				# #save segmentation images in various formats
				# for idx, response in enumerate(responses):
					# filename = 'D:/AirSim/New/Images/Images_master_v2/image_' +str(i)+'_raw' 
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
						# airsim.write_png(os.path.normpath(filename + '.png'), img_rgba) #write to png 
					# if i%10 == 0:
						# print("Image count = ", i)
					# i = i +1
# #      exit()
import math
ninety_degrees_in_radians = (math.pi)/2
forty_five_degrees_in_radians = (math.pi)/4
client.simSetCameraOrientation(0, airsim.to_quaternion(0, 0, forty_five_degrees_in_radians)); #radians


#Changing coordinates for new environment images
for z in np.linspace(-10,-50,4):
	for x in np.linspace(-150,0, 10):
		for y in np.linspace(-60,-240,10):
			client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0, 0, forty_five_degrees_in_radians)), True)
			#print(client.simGetCameraInfo("0"))
			responses = client.simGetImages([
			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
			airsim.ImageRequest("3", airsim.ImageType.Scene, False, False)])
			# airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
			#print('Retrieved images: %d', len(responses))
			#save segmentation images in various formats
			for idx, response in enumerate(responses):
			    filename = 'D:/AirSim/New/Images/Images_master_v4_yaw_45/image_' +str(i)+'_raw' 
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
			    if i%10 == 0:
			        print("Image count = ", i)
			    i = i +1

# #        #find unique colors
# #        print(np.unique(img_rgba[:,:,0], return_counts=True)) #red
# #        print(np.unique(img_rgba[:,:,1], return_counts=True)) #green
# #        print(np.unique(img_rgba[:,:,2], return_counts=True)) #blue  
# #        print(np.unique(img_rgba[:,:,3], return_counts=True)) #blue


			# print(x,y,z)






