import os 
IMAGE_DIR = "C:/Projects/mask_rcnn_retrain/Converted_images"
for file in os.listdir(IMAGE_DIR):
    # temp_object_count = len(results_dict[file]["class_names"])
    # print(results_dict[file]["class_names"])
    # object_count = object_count + temp_object_count
	print(file)
