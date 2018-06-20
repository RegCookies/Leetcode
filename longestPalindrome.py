#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:33:39 2018

@author: z5044541
"""

def longestPalindrome(s):
    lenS = len(s)
    if lenS <= 1: return s
    minStart, maxLen, i = 0, 1, 0
    while i < lenS:
        if lenS - i <= maxLen / 2: break
        j, k = i, i
        print("first_line", j,k,i)
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1
        i = k + 1
        print("second_line", j,k,i)
        while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
        if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
    return s[minStart: minStart + maxLen]
    
    
s = "abcba"
b = longestPalindrome(s)
print(b)