#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        def get_next(node):
            next = node.right
            while(next is not None and next.left is not None and next.left is not node):
                next = next.left
            return next
            # 找到node元素的下一个节点

        total = 0
        node = root
        while(node is not None):
            if node.right is None:
                # 如果没有右节点则说明已经遍历了所有比自己大的，直接加已经记录的所有元素和即可，
                total += node.val
                node.val = total
                node = node.left
            else:
                # 如果右节点有，那么就要找自己对应的下一个节点是哪个。
                next = get_next(node)
                if next.left is None:
                    # 因为next是找的对应node节点的下一个节点，因此一定没有左子树，如果记录中没有
                    # 左子树，则说明还没有记录自己的下一个节点，那么就把node赋值到左子树上
                    next.left = node
                    node = node.right
                else:
                    # 如果node的下一个节点已经赋值了左子树，那么说明它已经被找过一次了，那么说明
                    # 这是第二次经过节点node了，也就是比node大的所有元素都已经处理了，
                    # 这正好符合中序遍历的概念，直接加total即可。
                    next.left = None
                    total +=node.val
                    node.val = total
                    node = node.left
        return root
# @lc code=end

