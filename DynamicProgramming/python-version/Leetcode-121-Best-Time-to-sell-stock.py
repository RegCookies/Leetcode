class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        sell = -float("inf")
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
                sell = -float("inf")
            if i > sell:
                sell = i
                profit = max(profit,sell-buy)
        return profit
