class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can buy and sell on the same day
        profit = 0 

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                # we have profit
                profit += (prices[i] - prices[i -1])

        
        return profit