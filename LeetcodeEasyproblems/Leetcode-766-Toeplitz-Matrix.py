class Solution:
    def isToeplitzMatrix(self, matrix):
        return all(matrix[i][:-1] == matrix[i+1][1:] for i in range(len(matrix)-1))
