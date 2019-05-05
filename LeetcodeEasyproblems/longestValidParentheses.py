#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:03:37 2018

@author: z5044541
"""

def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = [0]
        longest = 0 
        
        for i in s:
            if i == "(":
                check.append(0)
            else:
                if len(check)>1:
                    val = check.pop()
                    check[-1] += val + 2
                    longest = max(longest,check[-1])
                else:
                    check = [0]
        return longest