#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_total = 0
        for i in range(len(nums)):
            if nums[i] ==0:
                zero_total +=1
            else:
                nums[i-zero_total]  = nums[i]
        for i in range(zero_total):
            nums[-i-1] = 0
# @lc code=end

