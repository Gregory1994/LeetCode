#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        if not length:
            return 0

        water = 0
        left = height[0]
        i = 0
        water_local = 0

        while i < length:
            
            if left == 0:
                left = height[i]
                i += 1
                continue

            if height[i] < left:
                water_local += left - height[i] 
            else:
                water += water_local
                water_local = 0
                left = height[i]

            i += 1

        right = height[length - 1]
        j = length - 1 
        water_local = 0

        while j >= 0:
            
            if right == 0:
                right = height[j]
                j -= 1
                continue

            if height[j] > right:
                water += water_local
                water_local = 0
                right = height[j]
            else:
                water_local += right - height[j]

            j -= 1
        
        return water    


