# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode
import sys
import setup_path 
import airsim
import os
import cv2 as cv 
import numpy as np

# client = airsim.VehicleClient()
# client.confirmConnection()

# ###################################################################################################################
# #Setting all object IDs to 0
# found = client.simSetSegmentationObjectID("[\w]*", 0, True);
# print("Set everything to 0 color code: %r" % (found))

#below code didn't work beacause currently in computerVision mode
#client.moveToPositionAsync(273, -7167, 1036, 10, 0).join() # , DrivetrainType.ForwardOnly, YawMode(False,0), 20, 1) 

# found = client.simSetSegmentationObjectID("FbxScene_PickupTruck[\w]*", 201, True);
# print("found FbxScene_PickupTruck? ",found)
# found = client.simSetSegmentationObjectID("KamazNov2[\w]*", 201, True);
# print("found KamazNov2? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_JCB2[\w]*", 201, True);
# print("found FbxScene_JCB2? ",found)

# #Set train alone to 1. Means setting the cars as well
# found = client.simSetSegmentationObjectID("cannopcart[\w]*", 2, True);
# print("found cannopcart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_GraveCart[\w]*", 2, True);
# print("found FbxScene_GraveCart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# print("found FbxScene_GraveCart? ",found)
# found = client.simSetSegmentationObjectID("FbxScene_train_model[\w]*", 2, True);
# print("found FbxScene_train_model? ",found)

# #Change the code below to move the camera to desired position
# x = -17
# y= -128
# z= -65
# i =0

# client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(x,y,z), airsim.to_quaternion(0,0,0)), True)
# #print(client.simGetCameraInfo("0"))
# responses = client.simGetImages([
# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, True), #depth in perspective projection
# #    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])  #scene vision image in uncompressed RGBA array
# airsim.ImageRequest("3", airsim.ImageType.Scene, False, False),
# airsim.ImageRequest("3", airsim.ImageType.Segmentation, False, False)])

# #print('Retrieved images: %d', len(responses))
# #save segmentation images in various formats
# for idx, response in enumerate(responses):
#     filename = 'D:/AirSim/New/Images/Images_batch2/py_seg_new_' +str(i)+' '+ str(idx) 
#     if response.pixels_as_float:
#         #print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#         airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
#     elif response.compress: #png format
# #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#     	airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
#     else: #uncompressed array - numpy demo
#        #print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
#         img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
#         img_rgba = np.flipud(img_rgba) #original image is flipped vertically
#         airsim.write_png(os.path.normpath(filename + '.numpy.png'), img_rgba) #write to png 
#     print("Image count = ", i)
#     i = i +1

#        #find unique colors
#        print(np.unique(img_rgba[:,:,0], return_counts=True)) #red
#        print(np.unique(img_rgba[:,:,1], return_counts=True)) #green
#        print(np.unique(img_rgba[:,:,2], return_counts=True)) #blue  
#        print(np.unique(img_rgba[:,:,3], return_counts=True)) #blue

img = cv.imread('D:/AirSim/New/Images/Images_batch2/py_seg_new_1 1.numpy.png',0)
color = [255, 255, 255] # 'cause purple!
# border widths; I set them all to 150
top, bottom, left, right = [1]*4
img_with_border = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_CONSTANT, value=color)
ret,thresh = cv.threshold(img_with_border,127,255,0)
im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
print(len(contours))
cv.imwrite("D:/AirSim/New/Images/Images_batch2/with_Border.jpg", im2)
#cnt = contours[len(contours)-1]
#M = cv.moments(cnt)
#print( M )

# x,y,w,h = cv.boundingRect(cnt)
# print(" x: "+str(x)+" y: "+str(y)+" w: "+str(w)+" h: "+str(h))
# rect = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect_lastcontour.jpg", rect)

# x,y,w,h = cv.boundingRect(cnt)
# print(" x: "+str(x)+" y: "+str(y)+" w: "+str(w)+" h: "+str(h))
# rect = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect.jpg", rect)

#Extracting the coorindates of the biggest enclosing rectangle
min_x, min_y, max_x, max_y = 1025,1025,0,0
for contour in contours[:-1]: #ignoring the last contour because it's the one around the whole picture
    # get rectangle bounding contour
    [x,y,w,h] = cv.boundingRect(contour)
    if x<min_x:
    	min_x=x
    	#print(x,min_x)
    if y<min_y:
    	min_y=y
    if x+w>max_x:
    	max_x=x+w
    	#print(max_x,x+w)
    if y+h>max_y:
    	max_y=y+h   	    	
    # draw rectangle around contour on original image

print(min_x, min_y, max_x, max_y)
cv.rectangle(im2,(min_x,min_y),(max_x, max_y),(0,255,0),2)

crop_img = im2[1:1025, 1:1025]
cv.imwrite("D:/AirSim/New/Images/Images_batch2/sample_rect_cropped.jpg", crop_img)





