#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNum = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minNum:
            self.minNum.append(x)
        elif x < self.minNum[-1]:
            self.minNum.append(x)
        else:
            self.minNum.append(self.minNum[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        self.minNum.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.minNum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

