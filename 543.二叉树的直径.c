/*
 * @lc app=leetcode.cn id=543 lang=c
 *
 * [543] 二叉树的直径
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int diameterOfBinaryTree(struct TreeNode* root){
    int maxD = 0;
    dig(root,&maxD);
    return maxD;
}

int max(int a,int b){
    return a>b?a:b;
}

int dig(struct TreeNode* root,int* maxD){
    if(root==NULL){
        return 0;
    }else{
        int left = dig(root->left,maxD);
        int right = dig(root->right,maxD);
        *maxD = max(*maxD,left+right);
        return max(left,right)+1;
    }
}


// @lc code=end

