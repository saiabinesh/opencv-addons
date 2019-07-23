import sys
def generate_list_of_object_IDs(base_name, min_number, max_number):
	list_of_object_IDs = [str(x) for x in range(min_number,max_number)]+
	print(object_exists_list)


def write_list_of_object_IDs_to_file(list_of_object_IDs, file_name):
	buffsize=1
	file = open(filename,"a+",buffsize)
	for item in list_of_object_IDs:
		file.write("%s\n" % item)

base_name = sys.argv[1]
min_number = sys.argv[2]
max_number = sys.argv[3]
class_name = sys.argv[4]
filename = "list_"+class_name+"_"+base_name+".txt"

