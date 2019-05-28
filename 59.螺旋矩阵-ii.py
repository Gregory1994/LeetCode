#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        lo = n*n + 1

        while lo > 1:
            lo, hi = lo - len(matrix), lo
            matrix = [list(range(lo, hi))] + list(zip(*matrix[::-1]))
        return matrix
