from HashTable import *

def create_studentDatabase(studentRecords):
    size = 7
    hashtable = create_hashtable(size)
    for student in studentRecords:
        hashtable, size = put(hashtable, student["ID"], student, size)
    return hashtable

def perform_Operations(H, operationFile):
    collision_path = {}
    size = len(H[0])
    with open (operationFile) as f:
        lines = f.readlines ()
    input = []
    for line in lines :
        line = line.strip () # remove leading and trailing spaces
        tokens = line.split () # split the line into tokens
        input.append ( tokens )
    
    for val in range (1, len(input)+1):
        collision_path[val] = []
    iteration = 1
    for lst in input:
        if lst[0] == 'Find':
            get(H, lst[1], size, collision_path, iteration )
            iteration += 1
        if lst[0] == 'Update':
            Update(H, lst[1], lst[2], lst[3], size,collision_path, iteration)
            iteration += 1
        if lst[0] == 'Delete':   
            H, size = delete(H, lst[1], size, collision_path, iteration)
            iteration += 1
    print(H)
    return collision_path



            

def main(filename):
    with open (filename) as f:
        lines = f.readlines ()
    input = []
    for line in lines :
        line = line.strip () # remove leading and trailing spaces
        tokens = line.split () # split the line into tokens
        input.append ( tokens [0]) # add the first token to the input list

    flst = []

    for i in range (1):
        dictionary = {}
        lst = input[i].split (',')
        for j in range(len(lst)):
            dictionary.update( {lst[j] : None})
    
    for i in range(1,len(input)):
        copy_of_dict = dictionary.copy()
        temp = input[i].split (',')
        index = 0
        for key in dictionary:
            copy_of_dict[key] = temp[index]
            index += 1
        flst.append(copy_of_dict)
    return flst





studentRecords=main('data.csv')
print(studentRecords)
H = create_studentDatabase(studentRecords)
print(perform_Operations(H, 'Operations.txt'))


