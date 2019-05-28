#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    d[i][j] = 1
                elif i == 0:
                    d[i][j] = d[i][j-1]
                elif j == 0:
                    d[i][j] = d[i-1][j]
                else: 
                    d[i][j] = d[i-1][j] + d[i][j-1]

        return d[i][j]

