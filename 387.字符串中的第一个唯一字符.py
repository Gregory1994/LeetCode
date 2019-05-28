#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i in range(len(s)):

            if s[i] in d:
                d[s[i]] = -1
            else:
                d[s[i]] = i
        
        for i in d.keys():
            if d[i] >= 0:
                return d[i]
        
        return -1

