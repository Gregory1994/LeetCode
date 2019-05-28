#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = []

        while head:
            node.append(head.val)
            head = head.next

        while len(node) > 1:
            if node.pop(0) != node.pop():
                return False

        return True

