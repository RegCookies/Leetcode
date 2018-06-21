#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:09:39 2018

@author: z5044541
"""

def isValid(s): 
    
    dict1 = {"(":")",
            "[":"]",
            "{":"}"}
    
    temp=[""]
    
    for i in s:
        if i in dict1:
            print(i)
            temp.append(dict1[i])
            print(temp)
        elif i in dict1.values() and i != temp.pop():
            print(i)
            print(temp)
            print(i in dict1.values())
            print(i != temp.pop())
            return False
    print(temp)
    return True


s = "()"
b = isValid(s)
print(b)