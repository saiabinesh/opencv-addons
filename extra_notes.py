import datetime
import json 
global date
date = str(datetime.datetime.now())
print(date)

#master_json_dict = {} #The final dictionary that will be dumped into the json
info__dict = {
"year": 2018,
"version": 1,
"description": "Coco style dataset with just train class generated from RCS Image dataset 10.5281/zenodo.1403708",
"contributor": "Sai Abinesh",
"url": "10.5281/zenodo.1403708",
"date_created": date,
}
#Changing id 10 from traffic light to gas cylinder
categories_list =  [{"supercategory": "vehicle", "id": 1, "name": "train"}, {"supercategory": "vehicle", "id": 2, "name": "truck"}, {"supercategory": "outdoor", "id": 3, "name": "gas cylinder"},{"supercategory": "outdoor", "id": 4, "name": "house"},{"supercategory": "person", "id": 5, "name": "person"}]

licenses_list = [{"url": "http:\/\/creativecommons.org\/licenses\/by-nc-sa\/2.0\/", "id": 1, "name": "Attribution-NonCommercial-ShareAlike License"}, {"url": "http:\/\/creativecommons.org\/licenses\/by-nc\/2.0\/", "id": 2, "name": "Attribution-NonCommercial License"}, {"url": "http:\/\/creativecommons.org\/licenses\/by-nc-nd\/2.0\/", "id": 3, "name": "Attribution-NonCommercial-NoDerivs License"}, {"url": "http:\/\/creativecommons.org\/licenses\/by\/2.0\/", "id": 4, "name": "Attribution License"}, {"url": "http:\/\/creativecommons.org\/licenses\/by-sa\/2.0\/", "id": 5, "name": "Attribution-ShareAlike License"}, {"url": "http:\/\/creativecommons.org\/licenses\/by-nd\/2.0\/", "id": 6, "name": "Attribution-NoDerivs License"}, {"url": "http:\/\/flickr.com\/commons\/usage\/", "id": 7, "name": "No known copyright restrictions"}, {"url": "http:\/\/www.usa.gov\/copyright.shtml", "id": 8, "name": "United States Government Work"}]

#Creating the master json dictionary using the prepopulated fields above
master_json_dict = {"info": info__dict, "images": [], "annotations": [], "licenses": licenses_list, "categories": categories_list  }

# print("categories list for id 10: ", categories_list[9])
# print(master_json_dict)

# The following function outputs a python dictionary that can be written into a file as a json. Right now bounding boxes are not written
def create_annotations(category_id_list, folder_path, master_json_dict, path_binary_list_of_flags):
	global date
	# Writing the basic image info for each image
	annotation_count =1 
	for image_number in range(100,200):

		image_temp = {
		"id": image_number,
		"width": 1024,
		"height": 1024,
		"file_name": folder_path+"/image_"+str(image_number)+"_raw.png",
		"license": 1,
		"flickr_url": "none",
		"coco_url": "none",
		"date_captured": date,
		}
		list_of_annotations_current_image = []
		for i in range(0,len(category_id_list)):
			current_category_id = category_id_list[i][0] #The first element in each list is the category id
			current_category_name = category_id_list[i][1] #The second element is the category name
			number_of_instances_in_category = category_id_list[i][2] #The third element is the number of instances in that category
			for instance_number in range(1,number_of_instances_in_category+1):
				#Reading the text file containing the binary flags of 1s and 0s and storing it into a list. The text file is of the format ex. "list_gas cylinder_5"
				binary_flags_object_present = open(path_binary_list_of_flags+"/list_"+current_category_name+"_"+str(instance_number)+".txt").read().splitlines()
				#Converting the elements of the list into int
				binary_flags_object_present =  [int(item) for item in binary_flags_object_present]
				if binary_flags_object_present[image_number-1]: # image_number-1 since image_number is indexed from 1, and binary flags are python indexed from 0
					annotations_temp = {
					"id": annotation_count,
					"image_id": image_number,
					"category_id": current_category_id, 
					"segmentation": [],
					"area": 0,
					"bbox": [], #For now ignoring this as bounding boxes will be automatically calculated from binary masks which are provided as numpy array from binary B/W style images
					"iscrowd": 0,
					"instance_number": instance_number,
					#"annotation_id":annotation_count,
					}
					annotation_count = annotation_count + 1
					list_of_annotations_current_image.append(annotations_temp)
		master_json_dict["images"].append(image_temp)
		master_json_dict["annotations"] = [*master_json_dict["annotations"], *list_of_annotations_current_image]

		# For each image writing annotations of objects so that the corresponding masks can be called during the finetuning process
		# The category id, category name, and the number of instances in each category are passed in as a list of lists as [[category_id, category name, number_of_instances],...] 


# print(master_json_dict["images"])
# print(master_json_dict["annotations"])
folder_path = "D:/AirSim/New/Images/Images_master"
#list containing lists of [[cat_id, num_instances],..] 10 - gas cylinder, 7- train, 8 - truck
category_id_list = [[3,"gas cylinder", 6],[1, "train", 1],[2,"truck",3],[4,"house",3],[5,"person",1]]
path_binary_list_of_flags = "D:/AirSim/New/AirSim/PythonClient/computer_vision"
create_annotations(category_id_list, folder_path, master_json_dict, path_binary_list_of_flags)

file_path_for_json = "D:/AirSim/New/Images/coco/annotations/instances_val2014.json"
with open(file_path_for_json, 'w') as data_file:
	json.dump(master_json_dict,data_file)

print("Done")	