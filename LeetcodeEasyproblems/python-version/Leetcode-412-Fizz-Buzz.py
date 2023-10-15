class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for x in range(1, n+1):
            y = ''
            if not x % 3:
                y = 'Fizz'
            if not x % 5:
                y += 'Buzz'
            ret.append(y if y else str(x))
        return ret
