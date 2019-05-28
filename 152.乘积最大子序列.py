#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子序列
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            curMax, curMin = max(curMax * nums[i], curMin * nums[i], nums[i]), min(curMax * nums[i], curMin * nums[i], nums[i])
            ans = max(curMax, ans)
        
        return ans

