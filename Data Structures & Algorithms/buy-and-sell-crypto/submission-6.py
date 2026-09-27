class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to check if the current price < buy rate
        # then we update buy
        # Calculate our profit = price - buy

        profit = 0
        max_profit = 0

        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price

            else:
                profit = price - buy
                max_profit = max(profit, max_profit)

        return max_profit