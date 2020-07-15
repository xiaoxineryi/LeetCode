/*
 * @lc app=leetcode.cn id=538 lang=c
 *
 * [538] 把二叉搜索树转换为累加树
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


struct TreeNode* convertBST(struct TreeNode* root){
    int sum = 0;
    covert(root,&sum);
    return root;
}

void covert(struct TreeNode* root,int* sum){
    if(root ==NULL){
        return ;
    }
    covert(root->right,sum);
    *sum +=root->val;
    root->val = *sum ;
    covert(root->left,sum);
}


// @lc code=end

