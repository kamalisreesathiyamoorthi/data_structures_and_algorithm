"""

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to the original key 
plus the sum of all keys greater than the original key in BST.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum = 0  # holds the accumulated sum

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.reverse_inorder(root)
        return root

    def reverse_inorder(self, node: TreeNode):
        if node:
            self.reverse_inorder(node.right)
            self.sum += node.val
            node.val = self.sum
            self.reverse_inorder(node.left)
