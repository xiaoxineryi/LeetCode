# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while(len(stack)!=0):
                preIndex = stack[-1]
                if T[i] <= T[preIndex]:
                    break
                else:
                    stack.pop()
                    ans[preIndex] = i - preIndex
            stack.append(i)
        while(len(stack)!=0):
            index = stack.pop()
            ans[index] = 0
        return ans