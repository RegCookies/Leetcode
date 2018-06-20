# This is the leetcode1 twoSum problem:
# The quickest way:

def twoSum(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            print(buff_dict)
            if nums[i] in buff_dict:
                print(nums[i])
                print(buff_dict[nums[i]])
                print(i) 
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

#my solution:
def twoSum1(self, nums, target):
    for i in nums:
        temp = target - i
        if temp in nums[nums.index(i)+1:]:
            return [nums.index(i), nums[nums.index(i)+1:].index(temp)+
                len(nums[:nums.index(i)+1])]                
                
nums = [2,7,11,15]
target = 9
b = twoSum(nums,target)
print(b)
