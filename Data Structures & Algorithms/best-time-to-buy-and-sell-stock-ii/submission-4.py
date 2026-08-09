class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we keep track of our profits
        # and add up our profits everytime we encounter a price > previous 

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i -1]

        
        return profit