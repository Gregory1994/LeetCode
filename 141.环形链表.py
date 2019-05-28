#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
            
        d = []

        while head.next:
            if head.next in d:
                return True
            else:
                d.append(head.next)
                head = head.next

        return False

