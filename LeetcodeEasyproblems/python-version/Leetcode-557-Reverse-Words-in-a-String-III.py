class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s[::-1].split(" ")
        res = ""
        for i in a[::-1]: 
            res += i + " "
        return res.strip(" ")
