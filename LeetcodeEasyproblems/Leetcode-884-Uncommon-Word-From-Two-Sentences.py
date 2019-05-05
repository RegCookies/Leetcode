class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dic = {}
        word_A = A.split(" ")
        word_B = B.split(" ")
        
        for i in word_A: 
            if i not in word_B:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] +=1
        for i in word_B:
            if i not in word_A:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] +=1
        
        return [i for i in dic if dic[i] == 1]
