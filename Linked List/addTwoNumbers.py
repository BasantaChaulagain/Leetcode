# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry=0
        res=l3=ListNode(-1)
        while(l1 or l2 or carry):
            fv=l1.val if l1 else 0
            sv=l2.val if l2 else 0
            val,carry=(fv+sv+carry)%10,(fv+sv+carry)//10
            l3.next=ListNode(val)
            
            l3=l3.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return(res.next)