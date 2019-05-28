#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):

            if s[i] in d:
                if d[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]

        return True


