#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False

            m = max(m, i + n)

        return True

