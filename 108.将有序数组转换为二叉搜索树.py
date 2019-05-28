#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None 
        n = len(nums) // 2
        head = TreeNode(nums[n])
        head.left = self.sortedArrayToBST(nums[:n])
        head.right = self.sortedArrayToBST(nums[n + 1:])

        return head

