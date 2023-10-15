def threeSum1(nums):

    nums = sorted(nums)
    result = []

    for first_tag in range(len(nums)-2):
        second_tag, third_tag = first_tag+1, len(nums)-1

        while second_tag < third_tag:
             check_sum =  nums[first_tag] + nums[second_tag] + nums[third_tag]

             if check_sum > 0:
                third_tag -=1
             elif check_sum < 0:
                second_tag += 1
             else:
                if [nums[first_tag],nums[second_tag],nums[third_tag]] not in result:
                    result.append([nums[first_tag],nums[second_tag],nums[third_tag]])

                while second_tag < third_tag and nums[second_tag] == nums[second_tag+1]:
                    second_tag += 1
                while second_tag < third_tag and nums[third_tag] == nums[third_tag-1]:
                    third_tag -= 1

                second_tag+=1
                third_tag-=1
    return  result

def threeSum(nums):
    if len(nums)< 3:
        nums =[]
    nums = sorted(nums)
    result = set()
    for i,v in enumerate(nums[:-2]):
        if i > 0 and v == nums[i-1]:
            continue
        d = {}
        for j in nums[i+1:]:
            if j not in d:
                d[-v-j] = 1
            else:
                result.add((v,-v-j,j))
        return list(result)
a=[0,0,0]
b= threeSum(a)
print(b)



