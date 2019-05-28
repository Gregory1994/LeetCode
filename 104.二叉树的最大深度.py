#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (67.60%)
# Total Accepted:    40.7K
# Total Submissions: 59.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# a = Solution()
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# a.maxDepth(root)        


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def maxDepthCore(left,right,MaxLen):
            MaxLenL = MaxLen
            MaxLenR = MaxLen
            if not left and not right:
                return MaxLen

            if left:
                MaxLenL += 1
                MaxLenL = maxDepthCore(left.left,left.right,MaxLenL)
            
            if right:
                MaxLenR += 1
                MaxLenR = maxDepthCore(right.left,right.right,MaxLenR)
            
            return max(MaxLenL,MaxLenR)

        if not root:
            return 0
        
        return maxDepthCore(root.left,root.right,1)
        

