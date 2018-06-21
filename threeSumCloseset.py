#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:10:49 2018

@author: z5044541
"""

def threeSumClosest(nums, target):
    nums = sorted(nums)
    result = []
    rel = []
    print(nums)
    for i in range(len(nums)-2):
  
        j, k = i+1, len(nums)-1
        print(i,j,k,nums[i], nums[j], nums[k],rel) 
            
        if nums[i] + nums[k-1] + nums[k] < target:
            result.append([nums[i],nums[k-1],nums[k]])
            rel.append(nums[i] + nums[k-1]+ nums[k])
        elif nums[i] + nums[j] + nums[j+1] > target:
            result.append([nums[i],nums[j],nums[j+1]])
            rel.append(nums[i] + nums[j]+ nums[j+1])
        else:
            while j < k:
                result.append([nums[i],nums[j],nums[k]])
                rel.append(nums[i] + nums[j]+ nums[k])
                if nums[i] + nums[j] + nums[k] < target:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > target:
                    k-=1
                else:
                    return target
    print(rel)
    rel.sort(key=lambda x:abs(x-target))
    print(rel)
    return rel[0]
a = [0,2,1,-3]
b = 1

c = threeSumClosest(a,b)