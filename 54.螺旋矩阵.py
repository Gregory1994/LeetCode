#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = []
        while matrix:
            n += matrix[0]
            matrix = list(zip(*matrix[1:]))
            matrix = matrix[::-1]
        return n

