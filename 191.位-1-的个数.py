#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0

        while n:
            num += n & 1
            n >>= 1

        return num

