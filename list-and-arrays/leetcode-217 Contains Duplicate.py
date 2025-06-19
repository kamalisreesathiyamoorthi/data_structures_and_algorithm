'''Given an integer array nums,
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
'''

def containsDuplicate(nums):
        # my_hash = {}
        # for i in nums :
        #     if i in my_hash : #if the element is already in the hash , then it is appearing for the send time thus the repeated element found
        #         return True
        #     my_hash[i] = 1

        # return False
        
        return len(nums)!= len(set(nums))

nums = [1,2,3,1]
print(containsDuplicate(nums))