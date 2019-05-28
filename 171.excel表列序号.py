#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i in range(len(s)):
            n = n * 26 + (ord(s[i]) - 64)

        return n


