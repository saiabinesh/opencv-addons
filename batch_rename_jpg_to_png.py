import os,sys
folder = 'D:/AirSim/New/Images/Images_master'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       output = os.rename(infilename, newname)
       newname = infilename.replace('.jpg', '.png')