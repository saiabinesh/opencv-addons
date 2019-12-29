#resize_image_camera_check_scale_invariance
import cv2
import os
#current_image_directory = "C:\\Projects\\mask_rcnn_retrain\\images"
current_image_directory = "D:\\AirSim\\New\\Images\\Baldonnell test images\\Stadium screenshots"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1
for file in os.listdir(current_image_directory):
    #print(file)
    filename = os.path.join(current_image_directory,file)
    oriimg = cv2.imread(filename)
    # print(oriimg.shape[:2])
    # exit()
    resized_image=oriimg[0:1024,647:1671]
    #resized_image = cv2.resize(oriimg, (853,640)) #dimensions are width, height
    new_filename = "C:\\Projects\\mask_rcnn_retrain\\images\\"+file
    cv2.imwrite(new_filename,resized_image)
    if counter%2==0:
        print(counter)
    counter = counter + 1