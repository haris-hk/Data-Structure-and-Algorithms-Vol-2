def create_hashtable(size): # returns tuple(list,list)
    """
    Creates a new hashtable with a given size.
    The hashtable is represented as a tuple of two lists, one for keys and one for values.
    """
    return ([None]*size, [None]*size)

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    """
    Resizes the hashtable based on the 'increase' parameter.
    If 'increase' is True, the size of the hashtable is doubled and then rounded up to the next prime number.
    If 'increase' is False, the size of the hashtable is halved, but not less than 7, and then rounded up to the next prime number.
    Existing key-value pairs are rehashed and inserted into the new hashtable.
    """
    
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
    
    # Rehash and insert existing key-value pairs into the new hashtable
    for i in range(len(hashtable[0])):
        if hashtable[0][i] != None:
            put(table,hashtable[0][i],hashtable[1][i],size)
            
    
    return (table,size)



def hash_function(key,size): #returns integer (Address)
    """
    This function generates a hash value for a given key.
    It sums up the ASCII values of the characters in the key, right shifts by 4, and then takes the modulus with the size.
    """
    hash_value = 0
    for character in key:
        hash_value += ord(character)
    
    hash_value = hash_value >> 4
    return hash_value % size

def collision_resolver(key, oldAddress, size): #returns integer (Address)
    """
    This function resolves collisions using open addressing.
    It generates an offset based on the ASCII values of the characters in the key and the size,
    then adds this offset to the old address and takes the modulus with the size. This method is often called key-offset method.
    """
    offset = 0
    for character in key:
        offset += abs(ord(character))
    
    offset = abs( offset // size)
    offset = (offset + oldAddress)% size
    return offset



def put(hashtable, key, data, size): #return hashtable,size
    """
    This function inserts a key-value pair into the hashtable.
    It uses the hash function to generate an address for the key.
    If a collision occurs, it uses the collision resolver to find a new address.
    """
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
    """
    This function calculates the load factor of the hashtable.
    The load factor is the ratio of the number of elements in the hashtable to the size of the hashtable.
    """
    num_elements = 0
    for i in range(size):
        if hashtable[0][i] is not None and hashtable[0][i] != "#":
            num_elements += 1
    
    load_factor = num_elements / size
   
  
    return load_factor

def Update(hashtable,key, columnName, data ,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    """
    This function updates the value associated with a key in the hashtable.
    It uses the hash function to find the address of the key, and if a collision occurs, it uses the collision resolver to find the new address.
    The function then updates the value at the found address.
    """
    address = hash_function(key, size)

    while hashtable[0][address] != key and hashtable[0][address] != None and hashtable[0][address] != "#":
        collision_path[opNumber].append(address)
        address = collision_resolver(key,address,size)
    
    collision_path[opNumber].append(address)
    hashtable[1][address][columnName] = data
    print('record Updated')
    return
     




def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    """
    This function retrieves the value associated with a key in the hashtable.
    It uses the hash function to find the address of the key, and if a collision occurs, it uses the collision resolver to find the new address.
    The function then returns the value at the found address.
    """
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
    """
    This function deletes a key-value pair from the hashtable.
    It uses the hash function to find the address of the key, and if a collision occurs, it uses the collision resolver to find the new address.
    The function then marks the key at the found address as deleted by setting it to "#".
    If the load factor of the hashtable after the deletion is greater than 0.75, the hashtable is resized to more than double its size.
    If the load factor is less than 0.3 and the size of the hashtable is greater than 7, the hashtable is resized to less than half its size.
    """
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
    

def next_prime(num):
    """
    This function finds the next prime number after the input number and returns the first prime number it finds.
    """
    for i in range(2,num):
        if num % i == 0:
             num += 1
    return num

