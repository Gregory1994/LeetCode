#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        if not n:
            return res
        
        res = self.core(res, n, 0, 0, '')
        return res

    def core(self, res, n, left, right, string):
        if left == n and right == n:
            res.append(string)
        elif left == right:
            res = self.core(res, n, left+1, right, string + '(')
        elif left > right and left < n:
            res = self.core(res, n, left, right+1, string + ')')
            res = self.core(res, n, left+1, right, string + '(')
        elif left > right and left == n:
            res = self.core(res, n, left, right+1, string + ')')

        return res

