class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can use an array to calculate the profit
        profit = 0 
        
        # go through each price in the list
        for i in range(1,len(prices)):
            # check if our current price is greater than the previous price
            if prices[i] > prices[i - 1]:
                # we can get some profit if we sell
                profit += prices[i] - prices[i-1]

        return profit