'''
Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, 
return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

'''


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # FLOYD - CYCLE DETECTION METHOD            tc : O(n)       sc : O(1)
        # phase 1 : detect the cycle
        slow = nums[0]
        fast = nums[0]

        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast : #cycle found
                break 
        # phase 2 : find the entrance to the cycle
        # reset the slow 
        slow = nums[0]
        while slow != fast :
            slow = nums[slow]
            fast = nums[fast]
        
        return slow