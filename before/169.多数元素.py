#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ans = {}
        # for num in nums:
        #     if num in ans:
        #         ans[num] +=1
        #     else:
        #         ans[num] = 1
        # length = len(nums)
        # for a in ans:
        #     if ans[a] >=length/2:
        #         return a
        # 上面是最基本的做法 就是一个哈希表然后查找
        # 下面我们使用投票法来进行解答 投票法之所以正确是因为多数元素超过n/2
        # 最坏的情况就是多数元素穿插在其他元素里面，导致每次非多数元素vote的减少
        # 都是因为多数元素造成的，如果这样最后透出来的结果还是多数元素 算法就正确
        ans = nums[0]
        vote = 0
        for num in nums:
            if ans == num:
                vote +=1
            else:
                vote -=1
            if vote<=0:
                ans = num
                vote = 1
        return ans
        
# @lc code=end

