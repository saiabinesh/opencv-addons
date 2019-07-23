import cv2
import os
current_image_directory = "D:/AirSim/New/Images/Misc_test/Rotate_equalize/Original"
# current_image_directory = "D:/AirSim/New/Images/Images_master"
counter = 1
for file in os.listdir(current_image_directory):
    #print(file)
    filename = os.path.join(current_image_directory,file)
    oriimg = cv2.imread(filename)
    img_yuv = cv2.cvtColor(oriimg, cv2.COLOR_BGR2YUV)
	# equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
	# convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    new_filename = "D:/AirSim/New/Images/Misc_test/Rotate_equalize/Output/"+file
    cv2.imwrite(new_filename,img_output)
    if counter%2==0:
        print(counter)
    counter = counter + 1