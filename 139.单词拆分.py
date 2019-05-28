#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#
class Solution(object):
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]


    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """
    #     if not s:
    #         return True
        
    #     for i in range(1, len(s) + 1):
    #         if s[:i] in wordDict:
    #             if self.wordBreak(s[i:], wordDict):
    #                 return True
        
    #     return False


