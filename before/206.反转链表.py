#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代求解
        # pre = None
        # temp = head
        # while(temp):
        #     next_node = temp.next
        #     temp.next = pre
        #     pre = temp
        #     temp = next_node
        # return pre

        # 递归求解
        def reverse(pre,temp):
            if temp:
                reverse(temp,temp.next)
                temp.next = pre
        if head is None:
            return None
        new_root = head
        while new_root.next:
            new_root = new_root.next
        reverse(None,head)
        return new_root

# @lc code=end

