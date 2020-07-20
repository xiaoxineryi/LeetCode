#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ## 如果知道了两个的差值 那么直接取消差值一直往前走，就可以找到了
        # len_a =0
        # len_b =0
        # nodeA = headA
        # nodeB=headB
        # while nodeA:
        #     len_a+=1
        #     nodeA = nodeA.next
        # while nodeB:
        #     len_b +=1
        #     nodeB = nodeB.next
        # diff = len_a - len_b
        # if diff >0:
        #     temp = headA
        #     otherNode = headB
        #     for i in range(diff):
        #         temp = temp.next
        # elif diff <0:
        #     temp = headB
        #     otherNode = headA
        #     for i in range(-diff):
        #         temp = temp.next
        # elif diff ==0:
        #     temp = headA
        #     otherNode=headB

        # while temp != otherNode:
        #     if temp is None:
        #         return None
        #     else:
        #         temp = temp.next
        #         otherNode = otherNode.next
        # return temp

        # 上面那样写简直是笨比 写出来代码也太难看了
        # 这其实是两个循环 第一次到达None的时候 会做出来差
        # 这样下一次再循环就能找到相交的地方了 画图看看
        nodeA = headA
        nodeB = headB
        if nodeA is None or nodeB is None:
            return None
        while(nodeA != nodeB):
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next
        return nodeA
# @lc code=end

