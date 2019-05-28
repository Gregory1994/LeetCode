#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums))

