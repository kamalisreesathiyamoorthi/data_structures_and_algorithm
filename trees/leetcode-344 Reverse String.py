'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

from typing import List


class Solution:
    def recursive_reverse(self , s , start , end ) :
        if start >= end :
            return
        s[start] , s[end] = s[end] , s[start]  #swap the elements at start and end 
        self.recursive_reverse(s , start+1 , end-1)

    def reverseString(self, s: List[str]) -> None:
        # RECURSIVE APPROACH                          tc : O(n)     sc : O(n) due to call stack 
        # self.recursive_reverse(s , 0 , len(s)-1) 
        
        # TWO POINTERS                                tc : O(n)     sc : O(1)  
        start = 0 
        end = len(s) - 1
        while start < end :
            s[start] , s[end] = s[end] , s[start]
            start = start + 1
            end = end -1 