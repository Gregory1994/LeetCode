#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        d = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    d[i][j] = obstacleGrid[i][j] ^ 1
                elif i == 0:
                    d[i][j] = d[i][j-1] * (obstacleGrid[i][j-1] ^ 1)
                elif j == 0:
                    d[i][j] = d[i-1][j] * (obstacleGrid[i-1][j] ^ 1)
                else: 
                    d[i][j] = d[i-1][j] * (obstacleGrid[i-1][j] ^ 1) + d[i][j-1] * (obstacleGrid[i][j-1] ^ 1)
                    # 位运算优先级低于加减法运算

        return d[i][j] * (obstacleGrid[i][j] ^ 1)

