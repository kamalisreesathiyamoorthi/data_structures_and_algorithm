'''
A path in a binary tree is a sequence of nodes 
where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    max_sum = -float("inf")

    def dfs(self , root) :
        if root is None :
            return 0
        
        left_gain = self.dfs(root.left)
        right_gain = self.dfs(root.right)

        left_gain = max(left_gain , 0)
        right_gain = max(right_gain , 0)

        self.max_sum = max (self.max_sum , root.val+left_gain+right_gain) 
        return root.val + max(left_gain , right_gain) # selecting either the leftsubtree or rightsubtree

    def maxPathSum(self, root):
        # Post-order Depth-First Search (DFS)                       tc : O(n)       sc : O(h) (h-height of the tree)
        self.dfs(root)
        return self.max_sum

        