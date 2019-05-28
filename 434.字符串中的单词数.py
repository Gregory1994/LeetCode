#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
class Solution:
    def countSegments(self, s: str) -> int:
        flag = False
        n = 0

        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                if not flag:
                    flag = True
                    n += 1
            else:
                if flag:
                    flag = False

        return n


