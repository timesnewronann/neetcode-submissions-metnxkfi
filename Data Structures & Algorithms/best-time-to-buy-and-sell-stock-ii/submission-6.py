class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Goal is to maximize profits
        # we can use a pointer to track when we get profits


        profits = 0

        # go through the prices
        for i in range(1,len(prices)):
            # check if we can make a profit
            if prices[i] > prices[i-1]:
                profits += prices[i] - prices[i -1]

        
        return profits