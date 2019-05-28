#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) > 0 and len(p) == 0:
            return False
        # 如果模式第二个字符是*
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                # 如果第一个字符匹配，三种可能1、模式后移两位；2、字符串移1位
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.isMatch(s, p[2:])
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False

