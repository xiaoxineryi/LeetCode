#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        number = len(height)
        ans = 0
        left,right = 0 , number -1
        for dis in range(number-1,0,-1):
            if height[left] < height[right]:
                ans,left = max(height[left]*dis,ans),left +1
            else:
                ans,right = max(height[right]*dis,ans),right-1
        return ans
# @lc code=end

