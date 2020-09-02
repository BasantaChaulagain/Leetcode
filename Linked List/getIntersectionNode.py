# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
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