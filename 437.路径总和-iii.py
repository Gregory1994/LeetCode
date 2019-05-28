#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        n = 0
        self.core(root, sum, n)
        return n
    
    def core(self, root, sum, n):

        if not root:
            return

        if root.val == sum:
            n += 1
        
        if root.left:
            self.core(root.left, sum, n)
            self.core(root.left, sum - root.val, n)
        
        if root.right:
            self.core(root.right, sum, n)
            self.core(root.right, sum - root.val, n)


