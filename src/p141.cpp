class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast = head, *slow = head;
        if (head == NULL)
            return false;
        while (fast->next != NULL && fast->next->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) break;
        }
        if (fast->next == NULL || fast->next->next == NULL)
            return false;
        else 
            return true;
    }
};