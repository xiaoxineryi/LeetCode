#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归实现
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root is not None:
    #         temp = root.left
    #         root.left = root.right
    #         root.right = temp
    #         left = self.invertTree(root.left)
    #         right = self.invertTree(root.right)
    #         return root
    #     else:
    #          return None

    # 迭代实现
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            temp = q.pop()
            if not temp:
                continue
            temp.left,temp.right = temp.right,temp.left
            q.append(temp.left)
            q.append(temp.right)
        return root
# @lc code=end

