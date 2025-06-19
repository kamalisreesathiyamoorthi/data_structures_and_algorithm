'''
Given a non-empty array of integers nums,
every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

xample 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
'''


class Solution(object):
    def singleNumber(self, nums):
        # my_hash = {}    tc : O(n)      sp :O(n)
        # for i in nums :
        #     my_hash[i]  = my_hash.get(i,0) + 1
        
        # for i in my_hash :
        #     if my_hash[i] == 1 :
        #         return i


        # USING XOR : tc : O(n)      sp :O(1)
        result = 0
        for i in nums :
            result = i ^ result   #XOR : same - false , different - true
        return result
        

obj = Solution()
nums = [4,1,2,1,2]
print(obj.singleNumber(nums))
