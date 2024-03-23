def create_hashtable(size): # returns tuple(list,list)
    return ([None]*size, [None]*size)

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    if increase == True:
        size = size*2
        size = is_prime(size)
        hashtable[0].extend([None]*size)
        hashtable[1].extend([None]*size)
        return (hashtable,size)

    else:
        size = size//2
        size = is_prime(size)
        hashtable[0][:size]
        hashtable[1][:size]
        return (hashtable,size)

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


def put(hashtable,key, data,size): #return hashtable,size
    if loadFactor > 75:
       resize_hashtable(hashtable,size,True)
    elif loadFactor < 30:
        resize_hashtable(hashtable,size,False)

    address = hash_function(key,size)
    while hashtable[0][address] != None:
        address = collision_resolver(key,address,size)
    hashtable[0][address] = key
    hashtable[1][address] = data

    return (hashtable,size)

    




def loadFactor(hashtable,size): # returns a float - Loadfactor of hashtable
    num_elements = sum(1 for _ in filter(None, hashtable[0]))

    load_factor = num_elements / size

    return load_factor

def Update(hashtable,key, columnName, data,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    pass
        
    
def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    pass
        
def delete(hashtable, key, size,collision_path,opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
   pass

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
