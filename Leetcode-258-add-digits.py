class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = int(sum(int(a) for a in str(num)))
            print(num)
        return num


    def addDigits(self,num: int) -> int:
        return 0 if num == 0 else 1+ (num-1)%9

# 为啥是 1+(num-1)%9
