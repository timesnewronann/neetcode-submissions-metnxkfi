class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can add up the profit at each index
        profit = 0

        for i in range(1, len(prices)):
            # check if the current price > previous day
            if prices[i] > prices[i - 1]:
                # we can make a profit
                profit += prices[i] - prices[i - 1]
            
        
        return profit