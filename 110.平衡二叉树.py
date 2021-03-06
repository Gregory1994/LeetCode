#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        return self.check(root) != -1
    
    def check(self, root):

        if not root:
            return 0
        
        left = self.check(root.left)
        right = self.check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1 
        
        return 1 + max(left, right)



