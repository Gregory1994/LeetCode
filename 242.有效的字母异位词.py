#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(len(t)):
            if t[i] not in d or d[t[i]] == 0:
                return False
            else:
                d[t[i]] -= 1

        for i in d.keys():
            if d[i] != 0:
                return False

        return True


