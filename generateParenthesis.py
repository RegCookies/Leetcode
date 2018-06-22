#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:39:06 2018

@author: z5044541
"""

def generateParenthesis(n):
        
    ans=["()"]
    if n==1:
        return ans
    for i in range(1,n):
        ans=list(set([i[0:k]+"()"+i[k:] for i in ans for k in range(len(i))]))
    return ans