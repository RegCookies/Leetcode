class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if nums == []:
            return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i-1])
            else: 
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        #print(dp)
        return dp[-1]
        """
        cur = pre = 0
        
        for i in nums:
            pre,cur = cur,max(cur,pre+i)
            
        return cur 
