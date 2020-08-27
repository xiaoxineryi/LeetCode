#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
    ## 基本思路：类似动态规划，从后往前遍历，如果是最后的几个特殊处理。
    ## 如果是最后一个就是0，然后如果是大于后面但是后面是0的话，那么就是0    
        length = len(T)
        ans = [0 for i in range(length)]
        for i in range(length-2,-1,-1):
            ans[i] = self.findBigger(T,i,ans)
        return ans

    def findBigger(self,T:List[int],index:int,ans:List[int]):
        next = index+1
        wait_day = 0
        while(ans[next] != 0 and T[index] >= T[next] ):
            next += ans[next]
        if(ans[next] == 0 and T[index] < T[next]):
            wait_day = next - index 
        elif(ans[next] ==0 and T[index] >= T[next]):
            wait_day = 0
        elif(ans[next] !=0 and T[index] < T[next]):
            wait_day = next - index
        return wait_day

# @lc code=end

