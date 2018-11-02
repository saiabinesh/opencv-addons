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


#Change the code below to move the camera to desired position
i =1
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
			airsim.ImageRequest("3", airsim.ImageType.DepthPlanner, False, False)])
			#print('Retrieved images: %d', len(responses))
			#save segmentation images in various formats
			for idx, response in enumerate(responses):
				global filename
				filename = 'D:/AirSim/New/Images/Images_master/depth_'+str(i)
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
					airsim.write_png(os.path.normpath(filename + '.jpg'), img_rgba) #write to jpg
			#draw_bounding_box(filename)
			if(i%10 ==0):
				print("Image count = ", i)
			i = i +1
			








