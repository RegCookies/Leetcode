#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:32:19 2018

@author: z5044541
"""

def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        point=dum= ListNode(None)
        point.next = head
        
        while point.next and point.next.next:
            temp = point.next
            temp1 = point.next.next  
            point.next,temp1.next,temp.next = temp1, temp, temp1.next
            point = temp
        return dum.next