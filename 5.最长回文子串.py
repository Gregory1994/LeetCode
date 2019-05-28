#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self,s,i,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1; j += 1
        return s[i+1:j]
        
