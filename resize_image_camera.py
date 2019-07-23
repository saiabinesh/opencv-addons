import cv2
import os
current_image_directory = "C:/Projects/mask_rcnn_retrain/images"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1
for file in os.listdir(current_image_directory):
    #print(file)
    filename = os.path.join(current_image_directory,file)
    oriimg = cv2.imread(filename)
    resized_image = cv2.resize(oriimg, (512, 512)) 
    new_filename = "C:/Projects/mask_rcnn_retrain/images/"+file
    cv2.imwrite(new_filename,resized_image)
    if counter%100==0:
        print(counter)
    counter = counter + 1