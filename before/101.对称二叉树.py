#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # def check(rootA,rootB):
        #     if rootA is None and rootB is None:
        #         return True
        #     if rootA is None or rootB is None:
        #         return False
        #     return rootA.val == rootB.val \
        #         and check(rootA.left,rootB.right)\
        #             and check(rootA.right,rootB.left)
        # if root is None:
        #     return True
        # return check(root.left,root.right)

        stack_left = []
        stack_right = []
        if root is None:
            return True
        stack_left.append(root.left)
        stack_right.append(root.right)

        while(stack_left and stack_right):
            left = stack_left.pop()
            right = stack_right.pop()

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack_left.append(left.left)
                stack_right.append(right.right)
                stack_left.append(left.right)
                stack_right.append(right.left)
            else:
                return False
        return True
# @lc code=end

