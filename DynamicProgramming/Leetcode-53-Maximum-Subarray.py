class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]*len(nums)
        
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] +nums[i]
            else:
                dp[i] = nums[i]
        print(dp)
        return max(dp)
