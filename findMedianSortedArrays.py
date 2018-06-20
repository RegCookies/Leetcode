#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:06:57 2018

@author: z5044541
"""

def findMedianSortedArrays(nums1, nums2):
    a = len(nums1)
    b = len(nums2)
    
    if a>b:
      nums1,nums2,a,b = nums2,nums1,b,a
    
    imin = 0 
    imax = a
    half = (a+b+1) // 2 
    while imin <= imax:
        i = (imin + imax) // 2
        j = half - i
        
        print(i,j,nums1,nums2)
        if i < a and nums2[j-1] > nums1[i]:
             imin = i+ 1
        elif i > 0 and nums1[i-1] > nums2[j]:
             imax = i - 1
        else:
            
            if i == 0 :
                max_left = nums2[j-1]
            elif j == 0 :
                max_left = nums1[i-1]
            else:
                max_left = max(nums2[j-1],nums1[i-1])
                
            
            if(a + b) % 2 ==1: 
                return max_left
            
            if i == a :
                min_right = nums2[j]
            elif j == b:
                min_right = nums1[i]
            else:
                min_right = min(nums2[j],nums1[i])
                
            return (max_left + min_right) / 2 
        
a = [1,3]
b = [2]
c = findMedianSortedArrays(a,b)
print(c)