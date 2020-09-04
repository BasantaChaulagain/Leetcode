# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        items=[]
        temp=head
        while(temp):
            items.append(temp.val)
            temp=temp.next
        
        temp=res=ListNode(-1)
        items.reverse()
        for i in range(0,len(items),1):
            print(items[i])
            temp.next=ListNode(items[i])
            temp=temp.next
        print(res.next)
        return res.next

    #One pass solution
    # def reverseList(self, head):
    #     prev=None
    #     while head:
    #         curr=head
    #         head=head.next
    #         curr.next=prev
    #         prev=curr
    #     return prev