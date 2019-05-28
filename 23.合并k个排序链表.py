#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        node = head

        nums = []

        for i in range(len(lists)):
            n = lists[i]
            while n:
                nums.append(n.val)
                n = n.next
        
        nums.sort()

        for i in range(len(nums)):
            head.next = ListNode(nums[i])
            head = head.next

        return node.next

