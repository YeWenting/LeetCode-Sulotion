class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast = head, *slow = head;
        if (fast == nullptr)
            return nullptr;
        while (fast->next != nullptr && fast->next->next != nullptr)
        {
            slow = slow ->next;
            fast = fast->next->next;
            if (slow == fast) break;
        }
        if (fast->next == nullptr || fast->next->next == nullptr)
            return nullptr;
        else
        {
            fast = head;
            for (;fast != slow; fast = fast->next, slow = slow->next);
            return slow;
        }
    }
};