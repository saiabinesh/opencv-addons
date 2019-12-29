# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import setup_path 
import airsim
import os

import numpy as np

client = airsim.VehicleClient()
client.confirmConnection()

i =1 
# for z in np.linspace(-6,-50,2):
for z in [-6]:
	# for x in np.linspace(75,105,5):
	for x in [40]:
		# for y in np.linspace(0,60,5):
		for y in [170]:
			client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
			#print(client.simGetCameraInfo("0"))
			responses = client.simGetImages([
			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
			#    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
			# airsim.ImageRequest("0", airsim.ImageType.Scene, False, False),airsim.ImageRequest("1", airsim.ImageType.Scene, False, False),airsim.ImageRequest("2", airsim.ImageType.Scene, False, False), airsim.ImageRequest("4", airsim.ImageType.Scene, False, False),
			airsim.ImageRequest("3", airsim.ImageType.Scene, False, False)])
			# airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])
			#print('Retrieved images: %d', len(responses))
			#save segmentation images in various formats
			for idx, response in enumerate(responses):
			    filename = 'D:/AirSim/New/Images/Images_master_v6/image_' +str(i)+'_raw' 
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
			    if i%2 == 0:
			        print("Image count = ", i)
			        print(type(x),type(y), type(z))
			    i = i +1










