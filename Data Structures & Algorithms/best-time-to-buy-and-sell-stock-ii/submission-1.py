class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can calculate the profit at every index
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i -1]:
                profit += prices[i] - prices[i-1]

        
        return profit