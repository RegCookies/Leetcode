class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        c = sorted(costs, key = lambda x : x[0] - x[1])
        res = 0
        for i in range(len(c)):
            if i < len(c)/2:
                res += c[i][0]
            else:
                res += c[i][1]
        return res