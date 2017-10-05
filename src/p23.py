# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [item for item in lists if item]
        if len(lists) == 0:
            return None
        head = tail = ListNode(0)
        while lists:
            min_val = 10000000000000
            for i, item in enumerate(lists):
                if item.val < min_val:
                    min_val = item.val
                    min_index = i
            tail.next = ListNode(min_val)
            tail = tail.next
            lists[min_index] = lists[min_index].next
            if lists[min_index] is None:
                del lists[min_index]
        return head.next


if __name__ == "__main__":

    ans = Solution().mergeKLists([[],[]])
    while ans:
        print ans.val
        ans = ans.next