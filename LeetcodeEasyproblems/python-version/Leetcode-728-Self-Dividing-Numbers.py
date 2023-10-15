class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lis = []
        for i in range(left,right+1):
            flag = True
            if "0" in str(i):
                pass
            else:
                for j in list(str(i)):
                    if int(i)%int(j) != 0:
                        flag = False
                if flag == True:
                    lis.append(i)
        return lis
