class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 

        # go through each price after the firs day
        for i in range(1, len(prices)):
            # check if we can make a profit
            if prices[i] > prices[i -1]:
                profit += prices[i] - prices[i - 1]


        return profit