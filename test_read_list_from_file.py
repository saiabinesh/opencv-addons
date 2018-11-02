# Having a list of binary flags in a text file, of gas cylinders being present 
base_filename = "list_gas_cylinder_"
list_of_lists = [ [] for i in range(0,5)] # creating 5 empty lists
print("list_of_lists: ",list_of_lists)
for i in range(1,6):
    list_of_lists[i-1] = (open(base_filename+str(i)+".txt").read().splitlines())
    print("List :"+str(i-1)+"\n"+str(list_of_lists[i-1][0:9]))  
    list_of_lists[i-1] =  [ int(item) for item in list_of_lists[i-1]]
    print("List :"+str(i-1)+"\n"+str(list_of_lists[i-1][0:9]))  