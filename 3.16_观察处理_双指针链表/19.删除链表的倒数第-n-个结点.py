#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #使用双指针，间隔n，然后一起移动，一直到结尾
        f = head
        remove = head
        tail = head
        for _ in range(n):
            tail = tail.next
        # 如果往后移动n以后是none，说明删除的就是头节点
        if tail == None:
            return f.next
        # 如果往后移动还有的话，就再往后移动一个，保证tail到None的时候，正好是要删除的前一个
        tail = tail.next

        while tail !=None:
            remove = remove.next
            tail = tail.next
        remove.next = remove.next.next
        return head
# @lc code=end

