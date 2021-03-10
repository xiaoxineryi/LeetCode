#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_number  = 0
        records = []
        for c in s:
            if c not in records:
                records.append(c)
                if len(records) > max_number:
                    max_number = len(set(records))
            else:
                while c in records:
                    records.pop(0)
                records.append(c)
        return max_number 
# @lc code=end

