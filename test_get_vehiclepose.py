# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import setup_path 
import airsim
import os

import numpy as np

client = airsim.VehicleClient()
client.confirmConnection()

for z in [-10,-30,-50,-100]:
	# for x in np.linspace(75,105,5):
	for x in [91]:
		# for y in np.linspace(0,60,5):
		for y in [32]:
			client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
			print(client.simGetVehiclePose())