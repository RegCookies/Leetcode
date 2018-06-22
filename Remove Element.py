def removeElement(nums, val):
     index = 0
     for i in range(len(nums)):
         print(nums,index,nums[index],i,nums[i])
         if nums[i] != val:
             nums[index ] = nums[i]
             index +=1
     print(nums)
     return index

nums = [0,1,2,2,3,0,4,2]
val = 2
a = removeElement(nums,val)
print(a)