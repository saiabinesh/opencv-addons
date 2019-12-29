# skipped configdisplay() for debugging
# Changed MODEL_DIR and other dirs to sys.argv[]s 
# used matplotlib.agg as backend
# loading weights from scratch to start from 80 class original model to 5 class one
# changed path for load_mask from D:... to /ichec/home/users/saiabinesh/experiments/maskrcnn/images/Images_master/image_
global categories_list


import os
import sys
import random
import math
import re
import time
import numpy as np
import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import skimage.color
import skimage.io
import skimage.transform

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from pycocotools import mask as maskUtils

# Root directory of the project
# ROOT_DIR = os.path.abspath("../../")
ROOT_DIR = sys.argv[4]
print(ROOT_DIR)

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn.config import Config
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
from mrcnn.model import log

#%matplotlib inline 

# Directory to save logs and trained model
# MODEL_DIR = os.path.join("D:/Misc/Back up datasets and repositories/Mask RCNN model logs/3 classes models")
MODEL_DIR = sys.argv[1] # The first argument should be MODEL_DIR

# Local path to trained weights file
# COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_aerial_5_classes_0918.h5")
COCO_MODEL_PATH = sys.argv[2]
#################################################Load from previous checkpoint ##################

# COCO_MODEL_PATH = "D:/Misc/Back up datasets and repositories/Mask RCNN model logs/Renamed traffic light models/aerial_trains20181115T1114/mask_rcnn_aerial_trains_0015.h5"

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    print("coco model path not found. Downloading")
    utils.download_trained_weights(COCO_MODEL_PATH)

## Configurations

#Need to replace the following hard caoded category list with the appropriate attribute of coco class
categories_list =  [{"supercategory": "outdoor", "id": 1, "name": "wheelie bin"},{"supercategory": "accessory", "id": 2, "name": "suitcase"},{"supercategory": "accessory", "id": 3, "name": "backpack"},{"supercategory": "outdoor", "id": 4, "name": "radiation barrel"},{"supercategory": "outdoor", "id": 5, "name": "gas cylinder"},{"supercategory": "outdoor", "id": 6, "name": "hose"},{"supercategory": "outdoor", "id": 7, "name": "car battery"}]

class aerial_trains_Config(Config):
    """Configuration for training on the toy shapes dataset.
    Derives from the base Config class and overrides values specific
    to the toy shapes dataset.
    """
    # Give the configuration a recognizable name
    NAME = "Baldonnell_from_scratch_from5m"
    # Train on 1 GPU and 8 images per GPU. We can put multiple images on each
    # GPU because the images are small. Batch size is 8 (GPUs * images/GPU).
    GPU_COUNT = 1
    IMAGES_PER_GPU = 2

    # Number of classes (including background)
    NUM_CLASSES = 1 + 7  # background + 80 default classes

    # Use small images for faster training. Set the limits of the small side
    # the large side, and that determines the image shape.
    IMAGE_MIN_DIM = 256
    IMAGE_MAX_DIM = 2048

    # Use smaller anchors because our image and objects are small
    RPN_ANCHOR_SCALES = (64, 128, 256, 512, 1024)  # anchor side in pixels

    # Reduce training ROIs per image because the images are small and have
    # few objects. Aim to allow ROI sampling to pick 33% positive ROIs.
    TRAIN_ROIS_PER_IMAGE = 32

    # Use a small epoch since the data is simple
    STEPS_PER_EPOCH = 45

    # use small validation steps since the epoch is small
    VALIDATION_STEPS = 1
    
config = aerial_trains_Config()
# config.display()

# ## Notebook Preferences

# def get_ax(rows=1, cols=1, size=8):
    # """Return a Matplotlib Axes array to be used in
    # all visualizations in the notebook. Provide a
    # central point to control graph sizes.
    
    # Change the default size attribute to control the size
    # of rendered images
    # """
    # _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    # return ax



import cv2
class aerial_trains_Dataset(utils.Dataset):
    """Generates the shapes synthetic dataset. The dataset consists of simple
    shapes (triangles, squares, circles) placed randomly on a blank surface.
    The images are generated on the fly. No file access required.
    """
    def load_coco(self, dataset_dir, subset, year="2014", class_ids=None,
              class_map=None, return_coco=False, auto_download=False):
        """Load a subset of the COCO dataset.
        dataset_dir: The root directory of the COCO dataset.
        subset: What to load (train, val, minival, valminusminival)
        year: What dataset year to load (2014, 2017) as a string, not an integer
        class_ids: If provided, only loads images that have the given classes.
        class_map: TODO: Not implemented yet. Supports maping classes from
            different datasets to the same class ID.
        return_coco: If True, returns the COCO object.
        auto_download: Automatically download and unzip MS-COCO images and annotations
        """

        if auto_download is True:
            self.auto_download(dataset_dir, subset, year)

        coco = COCO("{}/annotations/instances_{}{}.json".format(dataset_dir, subset, year))
        if subset == "minival" or subset == "valminusminival":
            subset = "val"
        image_dir = "{}/{}{}".format(dataset_dir, subset, year)

        # Load all classes or a subset?
        if not class_ids:
            # All classes
            class_ids = sorted(coco.getCatIds())

        # All images or a subset?
        if class_ids:
            image_ids = []
            for id in class_ids:
                image_ids.extend(list(coco.getImgIds(catIds=[id])))
            # Remove duplicates
            image_ids = list(set(image_ids))
        else:
            # All images
            image_ids = list(coco.imgs.keys())

        # Add classes
        for i in class_ids:
            self.add_class("coco", i, coco.loadCats(i)[0]["name"])

        # Add images
        for i in image_ids:
            self.add_image(
                "coco", image_id=i,
                path=os.path.join(image_dir, coco.imgs[i]['file_name']),
                width=coco.imgs[i]["width"],
                height=coco.imgs[i]["height"],
                annotations=coco.loadAnns(coco.getAnnIds(
                    imgIds=[i], catIds=class_ids, iscrowd=None)))
        if return_coco:
            return coco
    
    #Using the default from the base class (utils.py) and pasting here for clarity 

    def load_image(self, image_id):
        """Load the specified image and return a [H,W,3] Numpy array.
        """
        # Load image
        print("loading image: "+str(image_id) +" @Time: "+ time.ctime(time.time()))
        image = skimage.io.imread(self.image_info[image_id]['path'])
        # If grayscale. Convert to RGB for consistency.
        if image.ndim != 3:
            image = skimage.color.gray2rgb(image)
        # If has an alpha channel, remove it for consistency
        if image.shape[-1] == 4:
            image = image[..., :3]
        return image
    
    def load_mask(self, image_id): #image_id here is just the serial number of the images in image_info, not their unique id in the json. 
        """Generate instance masks for shapes of the given image ID.
        """
        global categories_list
        # print("loading mask for image_id: ",image_id)
        # Replacing self with dataset_train
        # print("image_info  = ", dataset_train.image_info[image_id])
        ##############doing this only for train. Need to change 
        # extract all the unique objects from the annotation and create counters for them
        list_of_object_cat_ids = list(set([dict['category_id'] for dict in dataset_train.image_info[image_id]["annotations"]])) #this returns a unique list of all category_ids in the annotation 
        number_of_objects_in_image = len(list_of_object_cat_ids)
		#Extracting the corresponding object names based on the category ids
        list_object_names = [categories_list[i]["name"] for i in range(0,len(categories_list)) if categories_list[i]["id"] in list_of_object_cat_ids]
        # print("list_object_names: ",list_object_names)
        #creating a list of 1s that can be used as object counters for images with multiple objects
        # object_counter_dict = dict((key, value) for (key, value) in zip(list_object_names, [1]*number_of_objects_in_image))
        # for each unique object, create a counters. Increment them when one of them is being loaded. and use the counter number to extract the mask using the filename
		# Create counters for different objects 
        mask = np.ones(shape = (576,1024,len(dataset_train.image_info[image_id]["annotations"])))
        mask_counter = 0 
		#The actual unique image_id written in the json which can be used to call the correspoding original raw images of the format raw_image_1.png , where 1 is the image_id (image_number as called here)
        image_number = dataset_train.image_info[image_id]["id"]
        # print("image_number: ", image_number)
        temp_class_id = []
        for annotation in dataset_train.image_info[image_id]["annotations"]:
            # print("Current Annotation processed :", annotation)
            current_category_id = annotation["category_id"]
            # print("current_category_id = ", current_category_id)         
            current_object_name = [categories_list[i]["name"] for i in range(0,len(categories_list)) if categories_list[i]["id"] == current_category_id][0]
            # print("current_object_name: ",current_object_name)
            temp_class_id.append(self.class_names.index(current_object_name))

            # current_object_instance_number = object_counter_dict[current_object_name]
            current_object_instance_number = annotation["instance_number"]
            # object_counter_dict[current_object_name] = object_counter_dict[current_object_name]+1
            #access the mask from filename of the object mask for that image	
            # ex D:\AirSim\New\Images\Images_master
            
            # changed to double underscore here to check if filename path throws error.
            color_mask_filename = "/ichec/home/users/saiabinesh/experiments/maskrcnn/images/Images_master_v6/image_"+str(image_number)+"_"+str(current_object_name)+"_"+str(current_object_instance_number)+".png"
            if os.path.isfile(color_mask_filename):
                img = cv2.imread(color_mask_filename,0)   
                ret,current_mask  = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
                #print("Type of object: ",type(mask))
                mask[:,:,mask_counter] = current_mask
                mask_counter = mask_counter + 1
                #extracting class id from the coco dictionary of the json annotations
            else:
                print("Mask file for image_number "+str(image_number)+" is missing from path: "+str(color_mask_filename))
        # print("Temp class id from list unpacking: ",temp_class_id)               
        # #Commenting out all the old code for class ids to extract it from the list
        # class_id = [dict['category_id'] for dict in dataset_train.image_info[image_id]["annotations"]]
        # print(class_id)
        #class_id = self.image_info[image_id]["annotations"][0]["category_id"]
        class_id = np.asarray(temp_class_id)
        # print(np.shape(class_id))
        # class_id.shape = (1,)
        #print("class id: ",class_id)
        #print("class id shape ",np.shape(class_id))
        # _idx = np.sum(mask, axis=(0, 1)) > 0
        #print("_idx value = ",_idx)
        # mask = mask[:, :, _idx]
        mask = np.logical_not(mask).astype(int)

        return mask.astype(np.bool), class_id

    def random_shape(self, height, width):
        """Generates specifications of a random shape that lies within
        the given height and width boundaries.
        Returns a tuple of three valus:
        * The shape name (square, circle, ...)
        * Shape color: a tuple of 3 values, RGB.
        * Shape dimensions: A tuple of values that define the shape size
                            and location. Differs per shape type.
        """
        # Shape
        shape = random.choice(["square", "circle", "triangle"])
        # Color
        color = tuple([random.randint(0, 255) for _ in range(3)])
        # Center x, y
        buffer = 20
        y = random.randint(buffer, height - buffer - 1)
        x = random.randint(buffer, width - buffer - 1)
        # Size
        s = random.randint(buffer, height//4)
        return shape, color, (x, y, s)

    def random_image(self, height, width):
        """Creates random specifications of an image with multiple shapes.
        Returns the background color of the image and a list of shape
        specifications that can be used to draw the image.
        """
        # Pick random background color
        bg_color = np.array([random.randint(0, 255) for _ in range(3)])
        # Generate a few random shapes and record their
        # bounding boxes
        shapes = []
        boxes = []
        N = random.randint(1, 4)
        for _ in range(N):
            shape, color, dims = self.random_shape(height, width)
            shapes.append((shape, color, dims))
            x, y, s = dims
            boxes.append([y-s, x-s, y+s, x+s])
        # Apply non-max suppression wit 0.3 threshold to avoid
        # shapes covering each other
        keep_ixs = utils.non_max_suppression(np.array(boxes), np.arange(N), 0.3)
        shapes = [s for i, s in enumerate(shapes) if i in keep_ixs]
        return bg_color, shapes

###########################Change directory for dataset here#####################
# dataset_dir = "D:/AirSim/New/Images/coco"
dataset_dir = sys.argv[3]


# Training dataset
dataset_train = aerial_trains_Dataset()
dataset_train.load_coco(dataset_dir, "train", year = "2014",return_coco=True)
#dataset_train.load_shapes(500, config.IMAGE_SHAPE[0], config.IMAGE_SHAPE[1])
dataset_train.prepare()

#print(dataset_train.image_info)

# Validation dataset
dataset_val = aerial_trains_Dataset()
dataset_val.load_coco(dataset_dir, "val", year = "2014",return_coco=True)
#dataset_val.load_shapes(50, config.IMAGE_SHAPE[0], config.IMAGE_SHAPE[1])
dataset_val.prepare()

list_of_all_image_ids_train = [i["id"] for i in dataset_train.image_info]
# print(len(list_of_all_image_ids_train))
# print(list_of_all_image_ids_train)
# exit()
list_of_all_image_ids_val = [i["id"] for i in dataset_val.image_info]
total_number_of_images_train_plus_val = len(list_of_all_image_ids_train) + len(list_of_all_image_ids_val)

masks_4d_array = np.zeros((1261,576, 1024, 1),dtype = np.bool)
list_of_class_id_lists = [None] * 1261

list_of_all_mask_class_id_pairs = [None]*1261
counter = 1
for id in range(len(list_of_all_image_ids_train)):
    # print(id, end = " ")
    if counter%10 == 0:
        print(counter)
    # print(id)
    current_mask_class_id_pair = [None] * 2
    image_id = dataset_train.image_info[id]["id"]
    current_mask_class_id_pair[0], current_mask_class_id_pair[1] =dataset_train.load_mask(id)
    list_of_all_mask_class_id_pairs[image_id]=current_mask_class_id_pair
    counter = counter + 1 
# import psutil

counter = 1
for id in range(len(list_of_all_image_ids_val)):
    if counter%10 == 0:
        print(counter)
        # memory = psutil.virtual_memory().available/ (1000 ** 3)
        # print(memory)
    # print(id)
    current_mask_class_id_pair = [None] * 2
    image_id = dataset_val.image_info[id]["id"]
    current_mask_class_id_pair[0], current_mask_class_id_pair[1] =dataset_val.load_mask(id)
    list_of_all_mask_class_id_pairs[image_id]=current_mask_class_id_pair
    counter = counter + 1


from sklearn.externals import joblib
filename = '/ichec/work/ngcom012c/maskrcnn/numpy_images_and_masks/list_of_all_mask_class_id_pairs_v2.sav'
joblib.dump(list_of_all_mask_class_id_pairs, filename)
