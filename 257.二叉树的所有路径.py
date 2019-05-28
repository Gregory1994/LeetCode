#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def binaryTreePaths(self, root):

        if not root:
            return []
        res = []
        self.core(root,'',res)
        return res

    def core(self, root, path, res):
        path += str(root.val)
        if not root.left and not root.right:
            res.append(path)

        if root.left:
            self.core(root.left, path + '->', res)

        if root.right:
            self.core(root.right, path + '->', res)




