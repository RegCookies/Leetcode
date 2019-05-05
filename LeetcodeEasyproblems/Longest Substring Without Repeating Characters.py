#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:34:00 2018

@author: z5044541
"""

def lengthOfLongestSubstring(s):
    start =maxl = 0
    check = {}
    for i in range(len(s)): 
        if s[i] in check and start <= check[s[i]]:
            start = check[s[i]] + 1
        else:
            maxl = max(maxl, i-start+1)
        check[s[i]] = i
    return maxl

s = "dvdf"
b = lengthOfLongestSubstring(s)
print(b)