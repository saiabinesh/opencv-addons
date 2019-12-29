#resize_image_camera_check_scale_invariance
import cv2
import os
#current_image_directory = "C:\\Projects\\mask_rcnn_retrain\\images"
current_image_directory = "D:\\AirSim\\New\\Images\\Images_master_v7"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1
for file in os.listdir(current_image_directory):
    #print(file)
    filename = os.path.join(current_image_directory,file)
    oriimg = cv2.imread(filename)
    print(oriimg.shape[:2])
    # exit()
    resized_image=oriimg[288:864,512:1536]
    #resized_image = cv2.resize(oriimg, (853,640)) #dimensions are width, height
    new_filename = "D:\\AirSim\\New\\Images\\Images_master_v7\\cropped_"+file
    cv2.imwrite(new_filename,resized_image)
    if counter%2==0:
        print(counter)
    counter = counter + 1