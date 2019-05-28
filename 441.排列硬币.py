#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#
class Solution:
    def arrangeCoins(self, n: int) -> int:
        corns = 0
        i = 0

        while n >= corns:
            i += 1
            corns += i
        i -= 1
        return i

