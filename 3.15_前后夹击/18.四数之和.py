#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)
        # 遍历第一个数据，从左到右
        for st in range(length-3):
            if st != 0 and nums[st] == nums[st-1]:
                continue
            # 遍历第二个数据
            for s in range(st+1,length-2):
                if s != st+1 and nums[s] == nums[s-1]:
                    continue
                # 左右找
                left,right = s+1,length-1
                while left < right:
                    add = nums[st] + nums[s] + nums[left] + nums[right]
                    if add < target:
                        left += 1
                    elif add > target:
                        right -= 1
                    else:
                        ans.append([nums[st],nums[s],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1
                        left +=1
                        right -=1
        return ans
# @lc code=end

