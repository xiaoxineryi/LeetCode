#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        # ans = []
        # ans.append(nums[0])
        # ans.append(max(nums[1],nums[0]))
        # for i in range(2,len(nums)):
        #     ans.append(max(ans[i-1],ans[i-2]+nums[i]))
        # return ans[len(nums)-1]

        # 优化：上面的记录了所有的数值 空间复杂度是O(N) 但我们发现其实
        # 只要记录上一个房屋的最大钱数和上上个房屋最大钱数就可以了
        ll_money = nums[0]
        l_money = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            temp = max(ll_money+nums[i],l_money)
            ll_money = l_money
            l_money = temp
        return l_money

# @lc code=end

