#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = [[],[]]
        yuanyin = ['a','e','i','o','u','A','E','I','O','U']

        for i in range(len(s)):
            if s[i] in yuanyin:
                d[0].append(i)
                d[1].append(s[i])

        for i in range(len(d[0])):
            s = s[:d[0][i]] + d[1][len(d[0]) - i - 1] + s[d[0][i] + 1:]

        return s


