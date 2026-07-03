class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you can't buy and sell on the same day
        # return the max profit
        # we can also choose to not make a transaction

        profit = 0
        max_profit = 0 

        left = 0 

        # can't buy and sell on the same day
        for right in range(1, len(prices)):
            # if the price at right < price at left buy
            if prices[right] < prices[left]:
                left = right
            
            profit = prices[right] - prices[left]

            if profit > max_profit:
                max_profit = max(profit, max_profit)
            

        return max_profit

