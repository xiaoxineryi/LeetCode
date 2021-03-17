#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isLargest = True
        length = len(nums)
        for l in range(length-1):
            if nums[l+1] > nums[l]:
                isLargest = False
                break
        if isLargest:
            # 如果是最大的话，就排列得到最小的
            nums.sort()
        else:
            # 如果不是最大的话，那么就倒着找递增的，递增则是最大的，一直到第一个下降的
            for st in range(length-1,-1,-1):
                # 如果出现下降的,将后面的排序得到最小
                if nums[st] > nums[st-1]:
                    ans = nums[:st-1]
                    # 找到后面比当前大的最小的元素提前
                    for l in range(length-1,st-1,-1):
                        if nums[l] > nums[st-1]:
                            ans.append(nums[l])
                            left = nums[st-1:l]
                            left2 = nums[l+1:]
                            for w in left2:
                                left.append(w)
                            left.sort()

                            for w in left:
                                ans.append(w)
                            nums.clear()
                            for w in ans:
                                nums.append(w)
                            break
                    break
            

# @lc code=end

