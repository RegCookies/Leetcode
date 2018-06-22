#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:52:59 2018

@author: z5044541
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        prev = None
        next1 = None
        count = 0
        #print(self.getCount(current))
        if head is None:
            return head
        elif self.getCount(current) < k:
            return head
        else:
            #print(self.getCount(current),count)
            if self.getCount(current) >= k:
                while current is not None and count<k: 
                    print("")
                    next1 = current.next
                    current.next = prev
                    prev= current 
                    current = next1
                    count += 1
                    print(self.getCount(current),count)
            #head = prev
            #print("current:",self.getCount(current),current.val,current.next.val)
           # print("head:",self.getCount(head),head.val,head.next.val )
            #print("prev", self.getCount(prev),prev.val,prev.next.val)
           # print("next", self.getCount(next1),next1.val)
            if next1 is not None:
                print(self.getCount(prev),self.getCount(current), self.getCount(next1))
                if self.getCount(current) >= k:
                    head.next = self.reverseKGroup(next1, k)
                else:
                    head.next = next1
        return prev
    def getCount(self,head):
        count = 0
        while head:
            count +=1
            head = head.next
        return count
            