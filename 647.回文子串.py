#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 基本思路：分治法，判断左边有没有，右边有没有，中间连接左右的有没有
        length = len(s)
        return self.countSub(s,0,length-1)
    
    def countSub(self,s:str,st:int,end:int) ->int:
        # 如果只有一个就返回一，否则左右分治+自己中间
        count = 0
        if end - st == 0:
            return 1
        else:
            mid = (end+st)/2
            count = self.countSub(s,st,mid) + self.countSub(s,mid+1,end)
        mid = (end+st)/2
        
# @lc code=end

