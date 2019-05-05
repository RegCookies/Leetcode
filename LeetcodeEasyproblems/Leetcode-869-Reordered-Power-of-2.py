class Solution:
    
    def swap(self,n,i,j): 
        tmp = n[i]
        n[i] = n[j]
        n[j] = tmp
    
    def getPre(self,n,start,res):
        if n  is None or start < 0:
            return n
        if start == len(n):
            res.append("".join(n))
        else:
            i = start
            while i < len(n):
                self.swap(n,start,i)
                self.getPre(n,start+1,res)
                self.swap(n,start,i)
                i += 1
            
        
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        
        #first of all get all digits:
        res = []
        str1 = list(str(N))
        
        self.getPre(str1,0,res)
        for i in res:
            if int(i)&(int(i)-1) == 0 and int(i[0]) != 0:
                return True
        return False

