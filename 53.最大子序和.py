#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def merge(nums,left,right):
            mid = int((left+right)/2)
            leftmax,rightmax=-10000,-100000
            left_temp,right_temp = 0,0
            for i in range(mid,left-1,-1):
                left_temp += nums[i]
                if leftmax<left_temp:
                    leftmax = left_temp
            for i in range(mid+1,right+1):
                right_temp +=nums[i]
                if rightmax < right_temp:
                    rightmax = right_temp
            return leftmax + rightmax
            

        def search_subset(nums,left,right):
            if left==right:
                return nums[left]
            mid = int((left+right)/2)
            return max(max(search_subset(nums,left,mid),\
                search_subset(nums,mid+1,right)),merge(nums,left,right))
        length = len(nums)
        return search_subset(nums,0,length-1)
# @lc code=end

