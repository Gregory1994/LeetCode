#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = n
        i = (a + b) // 2

        while guess(i) != 0:
            if guess(i) == -1:
                b = i - 1
            else:
                a = i + 1

            i = (a + b) // 2

        return i

        

