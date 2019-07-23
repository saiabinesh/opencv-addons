import numpy as np
list_coordinates = []
for z in np.linspace(-10,-50,4):
	for x in np.linspace(-150,0, 10):
		for y in np.linspace(-60,-240,10):
			#print(x,y,z)
			temp_list =[]
			temp_list.append(x)
			temp_list.append(y)
			temp_list.append(z)
			list_coordinates.append(temp_list)

with open('coordinates.txt', 'w') as f:
    for item in list_coordinates:
        f.write("%s\n" % item)