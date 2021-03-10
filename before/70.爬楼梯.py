#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        methods = []
        methods.append(0)
        methods.append(1)
        methods.append(2)
        for i in range(3,n+1):
            methods.append(methods[i-1]+methods[i-2])
        return methods[n]
# @lc code=end

