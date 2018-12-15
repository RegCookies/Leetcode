class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        a = len(nums)//2
        for i in nums:
            if i not in dic:
                dic[i] =1
            else:
                dic[i] +=1
            
        for i in dic:
            if dic[i] > a:
                return i
