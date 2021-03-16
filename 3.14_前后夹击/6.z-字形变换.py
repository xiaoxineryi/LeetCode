#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 先计算有多少列
        l = len(s)
        if numRows == 1:
            return s
        quotient = int(l / (numRows * 2 - 2))
        numCols = quotient * (numRows - 1)
        remainer = l % (numRows * 2 - 2)
        if remainer != 0:
            numCols += 1
        if remainer > numRows:
            numCols += remainer - numRows

        m = [['']* numRows for i in range(numCols)]

        col = 0
        row = 0

        for i in s:
            m[col][row] = i
            if col % (numRows-1) == 0:
                if row == numRows - 1:
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                row -=1
                col +=1
        ans = ''
        # print(m)
        for r in range(numRows):
            for c in range(numCols):
                if m[c][r] != '':
                    ans += m[c][r]
        return ans

# @lc code=end

