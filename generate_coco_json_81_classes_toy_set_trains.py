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
categories_list = [        
        {
            "supercategory": "person",
            "id": 1,
            "name": "person"
        },
        {
            "supercategory": "vehicle",
            "id": 2,
            "name": "bicycle"
        },
        {
            "supercategory": "vehicle",
            "id": 3,
            "name": "car"
        },
        {
            "supercategory": "vehicle",
            "id": 4,
            "name": "motorcycle"
        },
        {
            "supercategory": "vehicle",
            "id": 5,
            "name": "airplane"
        },
        {
            "supercategory": "vehicle",
            "id": 6,
            "name": "bus"
        },
        {
            "supercategory": "vehicle",
            "id": 7,
            "name": "train"
        },
        {
            "supercategory": "vehicle",
            "id": 8,
            "name": "truck"
        },
        {
            "supercategory": "vehicle",
            "id": 9,
            "name": "boat"
        },
        {
            "supercategory": "outdoor",
            "id": 10,
            "name": "traffic light"
        },
        {
            "supercategory": "outdoor",
            "id": 11,
            "name": "fire hydrant"
        },
        {
            "supercategory": "outdoor",
            "id": 13,
            "name": "stop sign"
        },
        {
            "supercategory": "outdoor",
            "id": 14,
            "name": "parking meter"
        },
        {
            "supercategory": "outdoor",
            "id": 15,
            "name": "bench"
        },
        {
            "supercategory": "animal",
            "id": 16,
            "name": "bird"
        },
        {
            "supercategory": "animal",
            "id": 17,
            "name": "cat"
        },
        {
            "supercategory": "animal",
            "id": 18,
            "name": "dog"
        },
        {
            "supercategory": "animal",
            "id": 19,
            "name": "horse"
        },
        {
            "supercategory": "animal",
            "id": 20,
            "name": "sheep"
        },
        {
            "supercategory": "animal",
            "id": 21,
            "name": "cow"
        },
        {
            "supercategory": "animal",
            "id": 22,
            "name": "elephant"
        },
        {
            "supercategory": "animal",
            "id": 23,
            "name": "bear"
        },
        {
            "supercategory": "animal",
            "id": 24,
            "name": "zebra"
        },
        {
            "supercategory": "animal",
            "id": 25,
            "name": "giraffe"
        },
        {
            "supercategory": "accessory",
            "id": 27,
            "name": "backpack"
        },
        {
            "supercategory": "accessory",
            "id": 28,
            "name": "umbrella"
        },
        {
            "supercategory": "accessory",
            "id": 31,
            "name": "handbag"
        },
        {
            "supercategory": "accessory",
            "id": 32,
            "name": "tie"
        },
        {
            "supercategory": "accessory",
            "id": 33,
            "name": "suitcase"
        },
        {
            "supercategory": "sports",
            "id": 34,
            "name": "frisbee"
        },
        {
            "supercategory": "sports",
            "id": 35,
            "name": "skis"
        },
        {
            "supercategory": "sports",
            "id": 36,
            "name": "snowboard"
        },
        {
            "supercategory": "sports",
            "id": 37,
            "name": "sports ball"
        },
        {
            "supercategory": "sports",
            "id": 38,
            "name": "kite"
        },
        {
            "supercategory": "sports",
            "id": 39,
            "name": "baseball bat"
        },
        {
            "supercategory": "sports",
            "id": 40,
            "name": "baseball glove"
        },
        {
            "supercategory": "sports",
            "id": 41,
            "name": "skateboard"
        },
        {
            "supercategory": "sports",
            "id": 42,
            "name": "surfboard"
        },
        {
            "supercategory": "sports",
            "id": 43,
            "name": "tennis racket"
        },
        {
            "supercategory": "kitchen",
            "id": 44,
            "name": "bottle"
        },
        {
            "supercategory": "kitchen",
            "id": 46,
            "name": "wine glass"
        },
        {
            "supercategory": "kitchen",
            "id": 47,
            "name": "cup"
        },
        {
            "supercategory": "kitchen",
            "id": 48,
            "name": "fork"
        },
        {
            "supercategory": "kitchen",
            "id": 49,
            "name": "knife"
        },
        {
            "supercategory": "kitchen",
            "id": 50,
            "name": "spoon"
        },
        {
            "supercategory": "kitchen",
            "id": 51,
            "name": "bowl"
        },
        {
            "supercategory": "food",
            "id": 52,
            "name": "banana"
        },
        {
            "supercategory": "food",
            "id": 53,
            "name": "apple"
        },
        {
            "supercategory": "food",
            "id": 54,
            "name": "sandwich"
        },
        {
            "supercategory": "food",
            "id": 55,
            "name": "orange"
        },
        {
            "supercategory": "food",
            "id": 56,
            "name": "broccoli"
        },
        {
            "supercategory": "food",
            "id": 57,
            "name": "carrot"
        },
        {
            "supercategory": "food",
            "id": 58,
            "name": "hot dog"
        },
        {
            "supercategory": "food",
            "id": 59,
            "name": "pizza"
        },
        {
            "supercategory": "food",
            "id": 60,
            "name": "donut"
        },
        {
            "supercategory": "food",
            "id": 61,
            "name": "cake"
        },
        {
            "supercategory": "furniture",
            "id": 62,
            "name": "chair"
        },
        {
            "supercategory": "furniture",
            "id": 63,
            "name": "couch"
        },
        {
            "supercategory": "furniture",
            "id": 64,
            "name": "potted plant"
        },
        {
            "supercategory": "furniture",
            "id": 65,
            "name": "bed"
        },
        {
            "supercategory": "furniture",
            "id": 67,
            "name": "dining table"
        },
        {
            "supercategory": "furniture",
            "id": 70,
            "name": "toilet"
        },
        {
            "supercategory": "electronic",
            "id": 72,
            "name": "tv"
        },
        {
            "supercategory": "electronic",
            "id": 73,
            "name": "laptop"
        },
        {
            "supercategory": "electronic",
            "id": 74,
            "name": "mouse"
        },
        {
            "supercategory": "electronic",
            "id": 75,
            "name": "remote"
        },
        {
            "supercategory": "electronic",
            "id": 76,
            "name": "keyboard"
        },
        {
            "supercategory": "electronic",
            "id": 77,
            "name": "cell phone"
        },
        {
            "supercategory": "appliance",
            "id": 78,
            "name": "microwave"
        },
        {
            "supercategory": "appliance",
            "id": 79,
            "name": "oven"
        },
        {
            "supercategory": "appliance",
            "id": 80,
            "name": "toaster"
        },
        {
            "supercategory": "appliance",
            "id": 81,
            "name": "sink"
        },
        {
            "supercategory": "appliance",
            "id": 82,
            "name": "refrigerator"
        },
        {
            "supercategory": "indoor",
            "id": 84,
            "name": "book"
        },
        {
            "supercategory": "indoor",
            "id": 85,
            "name": "clock"
        },
        {
            "supercategory": "indoor",
            "id": 86,
            "name": "vase"
        },
        {
            "supercategory": "indoor",
            "id": 87,
            "name": "scissors"
        },
        {
            "supercategory": "indoor",
            "id": 88,
            "name": "teddy bear"
        },
        {
            "supercategory": "indoor",
            "id": 89,
            "name": "hair drier"
        },
        {
            "supercategory": "indoor",
            "id": 90,
            "name": "toothbrush"
        }
]

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
#list containing lists of [[cat_id, class_name, num_instances],..] 10 - gas cylinder, 7- train, 8 - truck
category_id_list = [[7, "train", 1]]
path_binary_list_of_flags = "D:/AirSim/New/AirSim/PythonClient/computer_vision"
create_annotations(category_id_list, folder_path, master_json_dict, path_binary_list_of_flags)

file_path_for_json = "D:/AirSim/New/Images/coco/annotations/instances_val2014.json"
with open(file_path_for_json, 'w') as data_file:
	json.dump(master_json_dict,data_file)

print("Done")	