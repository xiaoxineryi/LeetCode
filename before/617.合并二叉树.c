/*
 * @lc app=leetcode.cn id=617 lang=c
 *
 * [617] 合并二叉树
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


struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2){
    if(t1 ==NULL || t2==NULL){
        return t1==NULL?t2:t1;
    }
    addLeft(t1,t2);
    return t1;
}

void addLeft(struct TreeNode* left1,struct TreeNode* left2){
    left1->val += left2->val;
    if(left1->left ==NULL){
        left1->left = left2->left;
    }else if(left2->left!=NULL){
        addLeft(left1->left,left2->left);
    }
    if(left1->right ==NULL){
        left1->right = left2->right;
    }else if(left2->right !=NULL){
        addLeft(left1->right,left2->right);
    }
}


// @lc code=end

