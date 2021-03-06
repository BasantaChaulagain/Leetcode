# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if(l1==None):
            return l2
        elif(l2==None):
            return l1
        
        pA=l1
        while(pA.next!=None):
            pA=pA.next
        pA.next=l2
        
        pA=l1
        vals=[]
        while(pA!=None):
            vals.append(pA.val)
            pA=pA.next
        vals.sort()
        
        l1=[ListNode(vals[0])]
        for i in range(1,len(vals)):
            l1.append(ListNode(vals[i]))
            l1[i-1].next=l1[i]
        
        return(l1[0])


# Alternative easier code
# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = cur = ListNode(0)
        
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
            
#         cur.next = l1 or l2
#         return head.next
