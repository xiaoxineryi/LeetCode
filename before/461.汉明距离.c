/*
 * @lc app=leetcode.cn id=461 lang=c
 *
 * [461] 汉明距离
 */

// @lc code=start


int hammingDistance(int x, int y){
    int z = x ^ y;
    int ans = 0;
    while (z !=0)
    {
        if(z%2!=0){
            ans++;
        }
        z = z >>1;
    }
    return ans;
}


// @lc code=end

