# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue 
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(None) 
        q = PriorityQueue()
        
        for l in lists:
            #print(l.val,l)
            if l: 
                
                q.put((l.val,l))
        while not q.empty():
            point.next = q.get()[1] 
            point = point.next
            if point.next: q.put((point.next.val,point.next))
        return head.next