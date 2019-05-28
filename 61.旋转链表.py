#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
            
        tail = head
        length = 1

        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if k == 0:
            return head

        breaknode = head
        while k != 1:
            breaknode = breaknode.next
            k -= 1

        newhead = breaknode.next
        breaknode.next = None
        tail.next = head

        return newhead


