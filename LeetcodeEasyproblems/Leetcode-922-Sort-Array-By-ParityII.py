class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        l,r = 0,n-1
        while l < n and r >= 0:
            while l < n and A[l] % 2 == 0: l += 2
            while r >=0 and A[r] % 2 == 1: r -= 2
            if l < n and r >= 0:
                A[l], A[r] = A[r], A[l]
        return A
