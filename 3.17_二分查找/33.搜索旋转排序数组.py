#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] == target:
                return i
        return -1
# @lc code=end

