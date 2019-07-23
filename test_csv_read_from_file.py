import csv

def csv_to_list_of_strings(filename):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		# print("type(csv_reader) = ",type(csv_reader))
		list_of_object_IDs = []
		for line in csv_reader:
			# print(line)
			list_of_object_IDs.append(line[0])
	return(list_of_object_IDs)

filename= 'D:/List_of_object_IDs/master_csv.csv'
# list_of_object_IDs = csv_to_list_of_strings(filename)
# #unpacked_list = [line[0] for line in list_of_object_IDs]
# print(list_of_object_IDs)

with open(filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	# print("type(csv_reader) = ",type(csv_reader))
	master_csv = []
	for line in csv_reader:
		# print(line)
		master_csv.append(line)
for filename,label in master_csv:
	
	print(filename, label)
