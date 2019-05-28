#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
class Solution:
    def myAtoi(self, s: str) -> int:
        state = [{}, 
            {'blank': 1, 'sign': 2, 'digit':3}, 
            {'digit':3},
            {'digit':3, 'alphabet':4, 'blank':4, 'sign':4},
            {'alphabet':4, 'blank':4, 'digit':4, 'sign':4}]
        currentState = 1
        res = ''
        for c in s:
            if c == ' ':
                b = 'blank'
            elif c >= '0' and c <= '9':
                b = 'digit'
            elif c == ' ':
                b = 'blank'
            elif c in ['+', '-']:
                b = 'sign'
            elif c == '.':
                break
            else:
                b = 'alphabet'
            if b not in state[currentState].keys():
              return 0
            currentState = state[currentState][b]
            if currentState in [2,3]:
                res += c
        if currentState not in [3,4]:
            return 0
        res = int(res)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < - 2 ** 31:
            return - 2 ** 31
        else:
            return res

