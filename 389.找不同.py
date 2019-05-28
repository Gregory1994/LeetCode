#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in d or d[t[i]] == 0:
                return t[i]
            else:
                d[t[i]] -= 1

