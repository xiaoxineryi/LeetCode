#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        ans = []
        if len(digits) == 0:
            return ans
        ans = dic[digits[0]]
        for index in range(1,len(digits)):
            w = digits[index]
            l = []
            for value in dic[w]:
                for a in ans:
                    l.append(a + value)
            ans = l
        return ans
# @lc code=end

