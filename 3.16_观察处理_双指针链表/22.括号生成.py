#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p,left,right,parens =[]):
            if left:
                generate(p + '(',left -1,right)
            if right > left:
                generate(p+ ')',left,right-1)
            if not right:
                parens.append(p)
            return parens
        return generate('',n,n)


    # @lc code=end

