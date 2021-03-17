#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ahead = ListNode()
        ahead.val = 0
        ahead.next = head
        first = ahead
        while first != None:
            second = first.next
            if second != None:
                third = second.next
                if third != None:
                    second.next = third.next
                    third.next = second
                    first.next = third
                    first = second
                else:
                    break
            else:
                break
        return ahead.next

# @lc code=end

