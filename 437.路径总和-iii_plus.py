class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefixSumTree = {0:1}
        self.count = 0
        
        prefixSum = 0
        self.dfs(root, sum, prefixSum, prefixSumTree)
        
        return self.count
        
        
    def dfs(self, root, sum, prefixSum, prefixSumTree):
        if not root:
            return 0
        prefixSum += root.val
        oldSum = prefixSum - sum
        if oldSum in prefixSumTree:
            self.count += prefixSumTree[oldSum]
        prefixSumTree[prefixSum] = prefixSumTree.get(prefixSum, 0) + 1
        
        self.dfs(root.left, sum, prefixSum, prefixSumTree)
        self.dfs(root.right, sum, prefixSum, prefixSumTree)
        
        '''一定要注意在递归回到上一层的时候要把当前层的prefixSum的个数-1，类似回溯，要把条件重置'''
        prefixSumTree[prefixSum] -= 1