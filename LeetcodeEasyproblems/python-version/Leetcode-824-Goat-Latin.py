class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels='aeiouAEIOU'
        words=[w if w[0] in vowels else w[1:]+w[0] for w in S.split()]
        return ' '.join(words[i]+'maa'+i*'a' for i in range(len(words)))


