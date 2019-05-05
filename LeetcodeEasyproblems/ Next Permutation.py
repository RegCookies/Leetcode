#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:35:00 2018

@author: z5044541
"""

def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = -1
        if len(nums) > 1:
            for j in range(len(nums)-1, 0 , -1):                
                if nums[j-1] < nums[j]:
                    index = j-1;
                    break
            if index == -1:
                nums = nums.reverse()
            else:
                up = 0
            
                for k in range(len(nums)-1, index, -1):
                    if nums[k] > nums[index]:
                        up = k
                        break 
                nums[up], nums[index] = nums[index],nums[up]
                print(index)
                print(nums[index+1:],nums)
                nums[index+1:] = nums[index+1:][::-1]
                print(nums[index+1:],nums)                   

nums = [1,1]

a = nextPermutation(nums)