from HashTable import *

def create_studentDatabase(studentRecords):
    hashtable = create_hashtable(7)
    for i in range(len(studentRecords)):
        hashtable[0][i] = studentRecords[i]["ID"]
        hashtable[1][i] = studentRecords[i]

def perform_Operations(H, operationFile):
     pass



            

def main(filename):
    with open (filename) as f:
        lines = f.readlines ()
    input = []
    for line in lines :
        line = line.strip () # remove leading and trailing spaces
        tokens = line.split () # split the line into tokens
        input.append ( tokens [0]) # add the first token to the input list
    print (input)
    print ()
    flst = []
    for i in range (1):
        dictionary = {}
        lst = input[i].split (',')
        for j in range(len(lst)):
            dictionary.update( {lst[j] : None})
    
    for i in range(1,8):
        x = dictionary.copy()
        temp = input[i].split (',')
        index = 0
        for key in dictionary:
            x[key] = temp[index]
            index += 1
        flst.append(x)

    print(flst)


    return flst





studentRecords=main('data.csv')
# H = create_studentDatabase(studentRecords)
# print(perform_Operations(H, 'Operations.txt'))
