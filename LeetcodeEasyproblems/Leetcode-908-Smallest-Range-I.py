class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        a = max(A) - min(A)
        
        return 0 if a <= 2*K else a-2*K
