def create_hashtable(size): # returns tuple(list,list)
    return ([None]*size, [None]*size)

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    
    if increase == True:
        size = size*2
        size = next_prime(size)
        table = create_hashtable(size)
    elif increase == False:
        if size == 7:
            return (hashtable,size)
        else: 
            if size // 2 > 7:
                size = size // 2
            else:
                size = 7

            size = next_prime(size)
            table = create_hashtable(size)
    
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
        offset += abs(ord(character))
    
    offset = abs( offset // size)
    offset = (offset + oldAddress)% size
    return offset

def put(hashtable, key, data, size): #return hashtable,size
    address = hash_function(key,size)
    while hashtable[0][address] != None and hashtable[0][address] != "#":
        address = collision_resolver(key,address,size)
    hashtable[0][address] = key
    hashtable[1][address] = data

    loadfctr = loadFactor(hashtable, size)
    if loadfctr > 0.75:
       hashtable, size = resize_hashtable(hashtable,size,True)
    elif loadfctr < 0.3 and size > 7:
        hashtable, size = resize_hashtable(hashtable,size,False)

    return hashtable,size

def loadFactor(hashtable,size): # returns a float - Loadfactor of hashtable
    num_elements = 0
    for i in range(size):
        if hashtable[0][i] is not None and hashtable[0][i] != "#":
            num_elements += 1
    
    load_factor = num_elements / size
   

    return load_factor

def Update(hashtable,key, columnName, data ,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    address = hash_function(key, size)

    while hashtable[0][address] != key and hashtable[0][address] != None and hashtable[0][address] != "#":
        collision_path[opNumber].append(address)
        address = collision_resolver(key,address,size)
    
    collision_path[opNumber].append(address)
    hashtable[1][address][columnName] = data
    print('record Updated')
    return
     
def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    start = hash_function(key, size)
    collision_path[opNumber].append(start)
    if hashtable[0][start] == key:
        return hashtable[1][start]
    
    address = collision_resolver(key, start, size)
    while hashtable[0][address] != key and hashtable[0][address] != "#":
        collision_path[opNumber].append(address)
        if address == start:
            break
        address = collision_resolver(key,address,size)
    
    collision_path[opNumber].append(address)
    statement = None
    if  hashtable[0][address] == key:
        statement = hashtable[1][address]
        print ("Item found")
    elif statement == None:
        print ("Item not found")
    
    return statement 
        
        
def delete(hashtable, key, size,collision_path,opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
    address = hash_function(key, size)
    if key not in hashtable[0]:
        print ("Item not Deleted")
        return (hashtable, size)
    while hashtable[0][address] != key and hashtable[0][address] != None and hashtable[0][address] != "#":
        collision_path[opNumber].append(address)
        address = collision_resolver(key,address,size)
    hashtable[0][address] = "#"
    collision_path[opNumber].append(address)

    loadfctr = loadFactor(hashtable, size)
    if loadfctr > 0.75:
       hashtable, size = resize_hashtable(hashtable,size,True)
    elif loadfctr < 0.3 and size > 7:
        hashtable, size =  resize_hashtable(hashtable,size,False)

    print('Item Deleted')
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
