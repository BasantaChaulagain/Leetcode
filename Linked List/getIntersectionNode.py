# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if(headA==None or headB==None):
            return None

        valA=[]
        while(headA!=None):
            valA.append(headA)
            headA=headA.next
        print(valA)
        print("--------------------")
        while(headB!=None):
            print(headB)
            if headB in valA:
                return headB
            headB=headB.next
            
        return None

        #optimized code
        l1 = headA
        l2 = headB
        while(l1 != l2):
            l1 = headB if l1==None else l1.next
            l2 = headA if l2==None else l2.next
        return l1