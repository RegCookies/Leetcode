class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return len([1 for i in range(L,R+1) if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19]])
