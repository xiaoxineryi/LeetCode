#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack_left = []
        mapping = {'(':')','{':'}','[':']'}
        for c in s:
            if c in mapping:
                stack_left.append(c)
            else:
                if not stack_left:
                    return False 
                l = stack_left.pop()
                if mapping[l] != c:
                    return False
        if not stack_left:
            return True
        else:
            return False

# @lc code=end

