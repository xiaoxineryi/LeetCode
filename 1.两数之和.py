#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

# @lc code=end

