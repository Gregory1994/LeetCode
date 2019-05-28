#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (51.01%)
# Total Accepted:    10.7K
# Total Submissions: 20.6K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def addNew(n,result):
            new_result = []
            for i in range(len(result)):
                num = result[i]
                for j in range(len(num)+1):
                    new = num[:]
                    new.insert(j,n)
                    if new not in new_result:
                        new_result.append(new)
            return new_result

        i = len(nums) - 1
        result = [[nums[0]]]

        while i != 0:
            result = addNew(nums[i],result)
            i -= 1
        
        return result
                        

