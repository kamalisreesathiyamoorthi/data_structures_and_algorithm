
print(hash("apple"))  # hash - a build-in method in python to generate hash values 

def hash_function ( key ) :
    hash_value = 0 
    prime = 19 
    for i in key :
        hash_value = ( hash_value + ord(i) ) * prime
    return hash_value

def hash_function2 (key) :
    hash_value = 0
    for index , char in enumerate(key , 1) :
        hash_value = hash_value + index * ord(char)   # ord(char) converts a character to its ASCII value.
    return hash_value

print(hash_function("apple"))
print(hash_function2("apple"))

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

class HashTable :
    
    def __init__ (self , size = 13) :
        self.data_table = [None] * size 
        
        
    def hash_function (self , key ) :
        hash_value = 0 
        prime = 19
        for char in key :
            hash_value = ( hash_value + ord(char) * prime ) % len(self.data_table)
        return hash_value 
        
        
    def insert_item (self , key , value ) :
        index = self.hash_function(key) 
        if self.data_table[index] is None : #If collision occurs , we use chaining
            self.data_table[index] = [[key , value ]]
        else : #check if the key already exists 
            for pair in self.data_table[index] :
                if pair[0] == key : # if the key already exists , change the new value of the key
                    pair[1] = value 
                    return
            self.data_table[index].append([key , value])  # key-value pair is stored as a list
    
    
    def get_item (self , key ) :
        index = self.hash_function(key) 
        if self.data_table[index] is None :  # No key-value pair is there in that index 
            return None 
        for pair in self.data_table[index] : #iterate over that list to find the given key and its value
            if pair[0] == key : # 0 for key , 1 for pair
                return pair[1]
        return None
            
    def get_all_keys (self) :
        keys = []
        for i in range(len(self.data_table)) :
            if self.data_table[i] is not None :
                for pair in self.data_table[i] :
                    keys.append(pair[0])
        return keys 
        
    def print_table (self) :
        for index , value in enumerate(self.data_table) :
            print(f"{index} -> {value}")
    
my_hash = HashTable()
my_hash.insert_item("apple" , 150)
my_hash.insert_item("orange" , 500)
my_hash.insert_item("melon" , 300)
my_hash.insert_item("lemon" , 250)
my_hash.insert_item("banana" , 600)
my_hash.insert_item("apple" , 250)  # this key already exists , so its value will be changed

print(my_hash.get_all_keys())       # ['banana', 'orange', 'apple', 'melon', 'lemon']

print(my_hash.get_item("apple"))    # 250

my_hash.print_table()   
'''
0 -> None
1 -> [['banana', 600]]
2 -> None
3 -> None
4 -> None
5 -> None
6 -> None
7 -> [['orange', 500]]
8 -> [['apple', 250]]
9 -> None
10 -> [['melon', 300], ['lemon', 250]]
11 -> None
12 -> None
'''

print(my_hash.get_item("lemon"))    # 250
print(my_hash.get_item("melon"))    # 300
        
        