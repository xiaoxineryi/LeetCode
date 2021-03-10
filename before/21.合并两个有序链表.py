#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归实现
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next,l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l2.next,l1)
        #     return l2

        # 迭代实现
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                pre = pre.next
                l1 = l1.next
            else:
                pre.next = l2
                pre = pre.next
                l2 = l2.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return prehead.next
        
# @lc code=end

