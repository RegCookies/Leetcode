class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
       
        history = []
        for i in ops:
            if i == "C":
                history.pop()
            elif i == "D":
                history.append(history[-1] * 2)
            elif i == "+":
                history.append(history[-1] + history[-2])
            else:
                history.append(int(i))
        return sum(history)
