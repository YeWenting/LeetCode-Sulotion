#include <iostream>

typedef struct ListNode{
	int data;
	ListNode *next;
} ListNode;

using namespace std;

int CheckLinkList(ListNode *head)
{
	ListNode *fast = head, *slow = head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow) break;
	}
	if (fast != slow)
		return -1;
	else 
	{
		fast = head;
		int pos;
		for (pos = 1; fast != slow; fast = fast->next, slow = slow->next, ++pos);
		return pos;
	}
}

int main(int argc, char const *argv[])
{
	/* Generate a LinkList has loop*/
	// ListNode *loopStart = NULL, *head = new ListNode;
	// head->data = 0;

	// {
	// 	ListNode* p = head;
	// 	for (int i = 1; i < 10; ++i, p = p->next)
	// 	{
	// 		if (i == 5) loopStart = p;
	// 		ListNode *tmp = new ListNode;
	// 		p->next = tmp;
	// 		tmp->data = i;
	// 	}
	// 	p->next = loopStart;
	// }

	/* Generate a no loop LinkList*/
	// ListNode *loopStart = NULL, *head = new ListNode;
	// head->data = 0;
	// ListNode* p = head;
	// for (int i = 1; i < 10; ++i, p = p->next)
	// {
	// 	if (i == 5) loopStart = p;
	// 	ListNode *tmp = new ListNode;
	// 	p->next = tmp;
	// 	tmp->data = i;
	// }

	/* Generate a single node with loop*/
	ListNode *head = new ListNode;
	head->data = 0;
	head->next = head;

	int ret;
	if ((ret = CheckLinkList(head)) < 0)
		cout << "This LinkList doesn't have loop" << endl;
	else 
		cout << "The loop starts at index " << ret << endl;
	return 0;
}