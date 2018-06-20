#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:34:33 2018

@author: z5044541
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l = ListNode(0)
        cur = l
        add = 0
        
        while l1 or l2 or add:
            value = (l1.val if l1 else 0 ) + (l2.val if l2 else 0) + add
            add = value // 10 
            cur.next = ListNode(value % 10) 
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
             
        return l.next 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """