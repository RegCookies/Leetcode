class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        cur = 1
        
        while num > 0:
            if num & 1 == 0:
                res += cur
            cur <<= 1
            num >>= 1
        return res
