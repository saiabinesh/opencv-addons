# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
import json
import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np
import sys

global filename

i =1
virtual_coordinates = []
for z in np.linspace(-30,-100,10):
	for x in np.linspace(2.93,-37.37, 10):
		for y in np.linspace(-88.17, -192.27,10):
			virtual_coordinates.append("x: "+str(round(x,2))+", y: "+str(round(y,2))+", z: "+str(round(z,2)))

object_list = ["train", "truck", "gas_cylinder"]


for image_count in range(1,1000):
	list_of_fields = ["Height", "Width", "Gamma", "Autoexposure max brightness", "Virtual coorindates", "Labels", "Bounding boxes"]
	metadata_dictionary= {key: None for key in list_of_fields}
	metadata_dictionary["Height"] = 1024
	metadata_dictionary["Width"] = 1024
	metadata_dictionary["Gamma"] = 2.2
	metadata_dictionary["Autoexposure max brightness"] = 0.64
	metadata_dictionary["Virtual coorindates"] = virtual_coordinates[image_count-1]
	metadata_dictionary["Labels"] = []
	metadata_dictionary["Bounding boxes"]=[]

	for object in object_list:
		file_path = "D:/AirSim/New/Images/Images_master/"+object+"_bbox_coordinates_"+str(image_count)+".txt"
		if os.path.exists(file_path):
			metadata_dictionary["Labels"].append(object)
			metadata_dictionary["Bounding boxes"].append(open(file_path, 'r').read())
	# if len(metadata_dictionary["Labels"]) > 0:
	# 	metadata_dictionary["Labels"] = ','.join(map(repr, metadata_dictionary["Labels"]))
	# 	metadata_dictionary["Bounding boxes"]= ','.join(map(repr, metadata_dictionary["Bounding boxes"]))
	with open("D:/AirSim/New/Images/Images_master/"+"metadata_"+str(image_count)+".exif", 'w') as file:
		file.write(json.dumps(metadata_dictionary))	

# print(virtual_coordinates[1:10])







