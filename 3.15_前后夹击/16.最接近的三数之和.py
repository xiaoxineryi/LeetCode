#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 100000
        dis = 100000
        nums.sort()
        length = len(nums)
        for st in range(length - 2):
            l,r = st+1,length-1
            while l < r:
                s = nums[st] + nums[l] + nums[r]
                d = abs(s-target)
                # 如果是较优解
                if d < dis:
                    dis = d
                    ans = s
                if s - target > 0:
                    r -= 1
                elif s - target < 0:
                    l += 1
                else:
                    return ans
        return ans
# @lc code=end

