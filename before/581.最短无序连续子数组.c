/*
 * @lc app=leetcode.cn id=581 lang=c
 *
 * [581] 最短无序连续子数组
 */

// @lc code=start


int findUnsortedSubarray(int* nums, int numsSize){
    int max_before = -10000,min=10000,less_last_pos = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if(nums[i]>max_before){
            max_before = nums[i];
        }else if(nums[i]<min && nums[i]<max_before){
            min = nums[i];
        }
        if(nums[i] <max_before){
            less_last_pos = i;
        }
    }
    int pos = 1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]>min){
            pos = i;
            break;
        }
    }
    return less_last_pos - pos + 1 ;
}


// @lc code=end

