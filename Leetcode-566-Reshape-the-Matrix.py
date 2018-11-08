class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        orgrows = len(nums)         #orgrows  original rows
        orgcols = len(nums[0])
        numofelem = orgrows * orgcols

        newnumofelem = r*c

        if numofelem != newnumofelem:
            return nums
        else:  
            res=[]
            nums = [item for row in nums for item in row]
            s=0
            for e in range(c,newnumofelem+1,c):
                res.append(nums[s:e])
                s=e

        return res
