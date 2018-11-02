from random import randint
info_list =[]
for i in range(0,10):
    info_list.append(randint(0, 1))

    filename = "sample_mask_flags.txt"
# buffsize=1
# file = open(filename,"a+",buffsize)
# for item in info_list:
    # file.write("%s\n" % item) 

# Use this function to read the flags and later write into annotations
list = open(filename).read().splitlines()
print(list)