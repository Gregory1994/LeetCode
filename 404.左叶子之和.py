#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        num = 0
        num = self.sumCore(root, num, 0)
        return num
    
    def sumCore(self, root, num, flag):

        if not root.left and not root.right:
            num += root.val * flag
            
        
        if root.left:
            num = self.sumCore(root.left, num, 1)
        if root.right:
            num = self.sumCore(root.right, num, 0)

        return num

