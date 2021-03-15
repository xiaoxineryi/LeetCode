#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans = ''
        for index in range(l):
            # if the length of str is odd
            res = self.check(s,index,index)
            if len(res) > len(ans):
                ans = res            
            # if the length is even
            r = self.check(s,index,index+1)

            if len(r) > len(ans):
                ans = r
        return ans


    def check(self,s,left,right):
        while(left >=0 and right < len(s) and s[left] == s[right] ):
            left -= 1
            right += 1
        return s[left+1:right]
# @lc code=end

