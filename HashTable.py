def create_hashtable(size): # returns tuple(list,list)
    return ([None]*size, [None]*size)

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    if increase == True:
        size = size*2
        size = next_prime(size)
        table = [None for i in range(size)]
    else:
        size = size//2
        size = is_prime(size)
        table = [None for i in range(size)]
    for i in range(len(hashtable[0])):
        if hashtable[0][i] != None:
            put(table,hashtable[0][i],hashtable[1][i],size)
    return (table,size)

       

def hash_function(key,size): #returns integer (Address)
    hash_value = 0
    for character in key:
        hash_value += ord(character)
    
    hash_value = abs( hash_value // 16 )
    return hash_value % size

def collision_resolver(key, oldAddress, size): #returns integer (Address)
    offset = 0
    for character in key:
        offset += ord(character)
    
    offset = abs( offset // size)
    return ((offset + oldAddress)% size)

def put(hashtable, key, data, size): #return hashtable,size
    if loadFactor > 75:
       resize_hashtable(hashtable,size,True)
    elif loadFactor < 30:
        resize_hashtable(hashtable,size,False)

    address = hash_function(key,size)
    while hashtable[0][address] != None or hashtable[0][address] != "#":
        address = collision_resolver(key,address,size)
    hashtable[0][address] = key
    hashtable[1][address] = data

    return (hashtable,size)

def loadFactor(hashtable,size): # returns a float - Loadfactor of hashtable
    num_elements = sum(1 for _ in filter(None, hashtable[0]))

    load_factor = num_elements / size

    return load_factor

def Update(hashtable,key, columnName, data,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    for index in range(len(hashtable[0])):
        if hashtable[0][index] == key:
            update_address = index
            break
    dictionary = hashtable[1][update_address]
    for keys in dictionary:
        if keys == columnName:
            dictionary[keys] = data 
            print('record Updated')
    return
     
def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    for index in range(len(hashtable[0])):
        if hashtable[0][index] == key:
            found_address = index
            return hashtable[1][found_address]
            
    
    return "Item not found"
        
def delete(hashtable, key, size,collision_path,opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
   for index in range(len(hashtable[0])):
        if hashtable[0][index] == key:
             hashtable[0][index] = "#"
             print('Item Deleted')
             break
   for number in collision_path:
       if number == opNumber:
           for i in range(len( collision_path[number])):
               if collision_path[number][i] == key:
                   del collision_path[number][i]
   return (hashtable, size)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
    while True:
        if is_prime(num):
            return num
        num += 1
