#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:53:56 2018

@author: z5044541
"""
def letterCombinations(digits):
    d = {   "1":'',
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}
    temp = [""]
    for i in digits:
        print(i,type(i))
        current = []
        for j in d[i]:
            print(j)
            for k in temp:
                current.append(k+j)
        temp = current
    return temp
    
a = "23"
b =letterCombinations(a)
print(b)