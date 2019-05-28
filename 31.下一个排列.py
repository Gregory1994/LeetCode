#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# class Solution:
#     def nextPermutation(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         minNum = nums[-1]
#         length = len(nums)
#         flag = 0

#         for i in range(1, length + 1):
#             if nums[-i] < minNum:
#                 d = nums[length-i:]
#                 a = max(d)
#                 d.remove(a)
#                 d.sort()
#                 nums = nums[0:length-i] + [a] + d
#                 flag = 1
#                 break
#             else:
#                 minNum = nums[-i]

#         if not flag:
#             nums.sort()
        
#         return

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trend
              j = i-1
              break
            i-=1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: # 
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return

