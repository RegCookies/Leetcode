#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:29:54 2018

@author: z5044541
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
def removeNthFromEnd(self, head, n):
    dummy = ListNode(0)
    dummy.next = head
        
    first = second = dummy
    
    for i in range(n):
        first = first.next
    print(first.val)
    while first.next is not None:
        first = first.next
        second = second.next
    second.next= second.next.next
    
    return dummy.next

a = ListNode(1)
a.val = 5 
print(a.val)