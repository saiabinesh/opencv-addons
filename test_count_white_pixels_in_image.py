import cv2
import numpy as np
import os

#test file "image_7_suitcase_64.png"
directory = "D:/AirSim/New/Images/Images_master_v2"
# object_name = "suitcase"
class_names = ['dead animal', 'dead bird','gas cylinder','suitcase','backpack']  
exclude_list = list(range(1,301))             
for object_name in class_names:
    list_pixel_counts =[]
    counter = 0
    for file in os.listdir(directory):
        print(file)
        if (object_name in file) and not(any(str(i) in file for i in exclude_list)):
            filename = os.path.join(directory,file) 
            # img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            #Trying mode = 0 to see if that works
            img = cv2.imread(filename, 0)
            ret,current_mask  = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            n_white_pix = np.sum(current_mask == 0)
            # print('Number of white pixels:', n_white_pix)
            list_pixel_counts.append(n_white_pix)
            counter = counter + 1
            if counter%100 ==0:
                print(counter, end = " ", flush = True)
                print(file)
    average_white_pixels = sum(list_pixel_counts)/len(list_pixel_counts)
    print("Average pixel size of "+object_name+" is "+str(average_white_pixels))