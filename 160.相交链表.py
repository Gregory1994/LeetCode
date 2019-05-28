#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        hA = []
        hB = []
        node = None

        while headA:
            hA.append(headA)
            headA = headA.next
        
        while headB:
            hB.append(headB)
            headB = headB.next

        while hA and hB:
            a = hA.pop()
            b = hB.pop()

            if a == b:
                node = a
            else:
                break
        
        return node

