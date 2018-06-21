#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:33:39 2018

@author: z5044541
"""

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    du = ListNode(0)
    dum = du
    while True:
        if l1 is None:
            dum.next = l2
            break
        if l2 is None:
            dum.next = l1
            break
        if l1.val<= l2.val: 
            dum.next = l1
            dum= dum.next
            l1 = l1.next
        else:
            dum.next = l2
            dum = dum.next  
            l2 = l2.next
    return du.next