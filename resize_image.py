import cv2
import os
current_image_directory = "C:/tmp/masks_person"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1
for file in os.listdir(current_image_directory):
    #print(file)
    filename = os.path.join(current_image_directory,file)
    oriimg = cv2.imread(filename)
    resized_image = cv2.resize(oriimg, (1024, 1024)) 
    new_filename = "D:/AirSim/New/Images/Images_master/"+file
    cv2.imwrite(new_filename,resized_image)
    if counter%100==0:
        print(counter)
    counter = counter + 1