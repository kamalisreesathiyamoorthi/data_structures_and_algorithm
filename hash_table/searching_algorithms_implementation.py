def sequential_search_unordered(unordered_list , search_key ) :
    index = 0
    found = False
    
    while not found and index < len(unordered_list) :
        if unordered_list[index] == search_key :
            found = True 
        else :
            index = index + 1 

    return found
    
def sequential_search_ordered( ordered_list , search_key) :
    index = 0
    found = False
    too_big = False 
    
    while not found and index < len(ordered_list) and not too_big:
        if ordered_list[index] == search_key :
            found = True 
        elif ordered_list[index] > search_key :
                too_big = True 
        else :
            index = index + 1 
        
    return found
    
def binary_search_ordered( ordered_list , search_key ) :
    low = 0 
    high = len(ordered_list) - 1
    found = False
    while low <= high and not found :
        mid = (low+high) // 2 
        if ordered_list[mid] == search_key :
            found = True
        elif ordered_list[mid] > search_key :
            high = mid-1 
        else :
            low = mid +1
        
    return found
    
my_list1 = [1,9,7,0,5,8,2,23,42]
print(sequential_search_unordered(my_list1 , 19))   # False

my_list2 = [1,2,3,4,5,6,7,8,9,12,19,100,120,140]
print(sequential_search_ordered(my_list2 , 15))     # False
print(binary_search_ordered(my_list2 , 100))        # True
print(binary_search_ordered(my_list2 , 10))         # False