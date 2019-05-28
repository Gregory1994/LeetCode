#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = maxlength = 0

        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
        
            d[s[i]] = i
        
        return maxlength

