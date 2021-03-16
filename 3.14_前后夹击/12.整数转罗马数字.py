#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        ans = ''
        key = sorted(dic.keys(),reverse=True)
        while num > 0:
            for i in key:
                while num >= i:
                    num -= i
                    ans += dic[i]
        return ans
        
# @lc code=end

