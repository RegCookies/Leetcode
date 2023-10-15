class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        
        for i in prices:
            cash = max(cash, hold+i-fee)
            hold = max(hold, cash-i)
        
        return cash
