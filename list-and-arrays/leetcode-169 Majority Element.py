'''
Given an array nums of size n, 
return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
class Solution(object):
    def majorityElement(self, nums):
        # HASH MAP  sc = O(n)    tc = O(n)
        # my_hash = {}
        # result = 0
        # max_num = 0
        # for i in nums :
        #     my_hash[i] = my_hash.get(i,0) + 1
        #     if my_hash[i] > max_num :
        #         max_num = my_hash[i]
        #         result = i
        # return result

        #BOYER MOORE sc = O(1)    tc = O(n)
        # if current element == result , increase count 
        # else decrease count ( if count = 0 , change the result)
        count = 0
        result = 0
        for current_element in nums :
            if current_element == result :
                count = count + 1
            else :
                if count == 0 :
                    result = current_element
                else :
                    count = count - 1 

        return result
        

obj = Solution()
nums = [3,2,3]
print(obj.majorityElement(nums))