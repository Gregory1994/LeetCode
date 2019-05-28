#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = ''

        while n != 0:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) // 26

        return res

