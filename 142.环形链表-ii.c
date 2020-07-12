/*
 * @lc app=leetcode.cn id=142 lang=c
 *
 * [142] 环形链表 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if(head ==NULL || head->next == NULL){
        return NULL;
    }
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    slow = slow->next;
    fast = fast->next->next;
    while(slow !=fast){
        if(fast ==NULL || fast->next ==NULL){
            return NULL;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* st = head;
    struct ListNode* st2 = slow;
    while(st != st2){
        st = st->next;
        st2 = st2->next;
    }
    return st;
}
// @lc code=end

