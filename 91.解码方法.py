#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (19.90%)
# Total Accepted:    6.9K
# Total Submissions: 34K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#
class Solution:
    def numDecodings(self, s: str) -> int:
        
        num = s
        
        if len(num) in [0, 1]:
            return len(num)
        
        res = [0, 1]
        
        for i in range(1, len(num)):
            
            if int(num[i-1:i+1]) < 26 and int(num[i-1]) != 0:
                res.append(res[-1] + res[-2])
            else:
                res.append(res[-1])
                
        return res[-1]
