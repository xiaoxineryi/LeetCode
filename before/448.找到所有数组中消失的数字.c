/*
 * @lc app=leetcode.cn id=448 lang=c
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize){
    int *res = (int *)malloc(sizeof(int)*numsSize);
	for (int i = 0; i < numsSize; i++) {
		int k = nums[i] - 1;//该元素应该出现的位置，比如1应该出现在数组下标为0的地方
		if (nums[i] == i + 1 || nums[i] == nums[k]) {
			;
		}
		else {
			int t = nums[i];
			nums[i] = nums[k];
			nums[k] = t;
			i--;
		}
	}
	int num = 0;
	for (int i = 0; i < numsSize; i++) {
		if (nums[i] != i + 1) {
			res[num] = i+1;
			num++;
		}
	}
	*returnSize = num;
	return res;
}


// @lc code=end

