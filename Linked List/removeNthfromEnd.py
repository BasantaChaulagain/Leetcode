# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __repr__(self):
#     	return "ListNode"+str({"val":self.val, "next":self.next})

# class LinkedList:
# 	def __init__(self, list=[]):
# 		head=None
# 		for i in range(len(list)):
# 			head=ListNode(list[i])
# 			print(head)
# 			head.next=ListNode(list[i+1])
# 			print(head)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        length=0
        first=dummy.next
        while(first!=None):
            first=first.next
            length+=1
        
        change_index=length-n
        ind=0
        first=dummy
        
        while(first!=None):
            if ind==change_index:
                first.next=first.next.next
                break
            first=first.next
            ind+=1
        
        print(head, dummy.next)
        return dummy.next
        
# def main():
# 	lnode=LinkedList([1,2,3])
# 	print(lnode)

# main()