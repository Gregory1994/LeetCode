#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
class Solution:
    def findNthDigit(self, n: int) -> int:

        a = [9]
        b = [0]
        for i in range(1,10):
            a.append((i+1) * 9 * 10 ** i + a[-1])
            b.append((i + 1) * 10 ** i - a[-2] - 1)
        
        for i in range(10):
            if n <= a[i]:
                num = str((n + b[i]) // (i+1))
                j = (n + b[i]) % (i+1)
                return int(num[j])


