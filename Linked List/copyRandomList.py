"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def get_node(self, head, ind):
        while(head):
            if head.val==ind:
                return head
            head=head.next
        return None
        
    def copyRandomList(self, head):
        res=temp=Node(-1)
        rand_ind,i=[],0
        while(head):
            temp.next=Node(head.val)
            rand_ind.append(head.random.val if head.random else None)
            head=head.next
            temp=temp.next
            i+=1
        print(rand_ind)
        temp=res.next
        for i in range(len(rand_ind)):
            if rand_ind[i]==None:
                temp=temp.next
                continue
            nd=self.get_node(res.next,rand_ind[i])
            temp.random=nd
            temp=temp.next
        
        return(res.next)


# Making use of python copy module
# import copy
# class Solution:
#     def copyRandomList(self, head):
#         return(copy.deepcopy(head))