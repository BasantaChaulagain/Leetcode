# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        if lists==[]:
            return None
        
        val_list=[]
        for i in range(len(lists)):
            pA=lists[i]
            if pA==None:
                continue
            while(pA!=None):
                val_list.append(pA.val)
                pA=pA.next
        
        val_list.sort()
        
        try:
            result=[ListNode(val_list[0])]
            for i in range(1,len(val_list)):
                result.append(ListNode(val_list[i]))
                result[i-1].next=result[i]

            return(result[0])
        
        except:
            return None