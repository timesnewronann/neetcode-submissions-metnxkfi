class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to return the max profit we can achieve
        maxProfit = 0 

        profit = 0

        # we can use a sliding window to determine the best time to buy and sell stock
        left = 0

        # we can't buy and sell on the same day
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right

            profit = prices[right] - prices[left]

            if profit > maxProfit:
                maxProfit = max(profit, maxProfit)

        
        return maxProfit