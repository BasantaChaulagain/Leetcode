# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# classical method
    def hasCycle(self, head):
        lists=[]
        while(head):
            if head==None:
                return False
            if head in lists:
                return True
            lists.append(head)
            head=head.next

    # Optimized solution, two pointer method
    def hasCycle(self, head):
        fast=slow=head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                return True
        return False