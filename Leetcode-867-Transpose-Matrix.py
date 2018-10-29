class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == [[]]:
            return [[]]
        row_len =  len(A)
        col_len =  len (A[0])
        
        result = [[0 for i in range(row_len)] for j in range(col_len)]
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                result[j][i] = A[i][j]
                
        return result 
