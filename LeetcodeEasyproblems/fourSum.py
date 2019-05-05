#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:09:22 2018

@author: z5044541
"""


def fourSum(nums, target):
    nums = sorted(nums)
    result=set()
    
    for i in range(len(nums)-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            print(j)
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            l,r =j+1,len(nums)-1
            print(l,r)
            while l<r:
                s = nums[i] + nums[j]+nums[l] + nums[r]
                if s < target:
                    l+=1
                elif s> target:
                    r-=1
                else:
                    result.add((nums[i],nums[j],nums[l],nums[r]))
                    
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l< r and  nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
    return list(result)

nums = [0,0,0,0]
target = 0
a=fourSum(nums, target)
print(a)           
        
        