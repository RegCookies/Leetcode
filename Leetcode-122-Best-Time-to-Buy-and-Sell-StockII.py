class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        cash = 0
        hold = -prices[0]
        
        for i in prices:
            cash = max(cash,hold + i)
            hold = max(hold,cash-i)
        return cash
