J = "aA"
S = "aAAbbb
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0 
        for i in S: 
            if i in J: 
                result +=1
        return result"
