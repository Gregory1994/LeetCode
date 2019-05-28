#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    length[i][j] = grid[i][j]
                elif i == 0:
                    length[i][j] = length[i][j-1] + grid[i][j]
                elif j == 0:
                    length[i][j] = length[i-1][j] + grid[i][j]
                else: 
                    length[i][j] = min(length[i-1][j], length[i][j-1]) + grid[i][j]

        return length[i][j]

