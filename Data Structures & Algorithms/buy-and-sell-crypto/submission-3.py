class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can use a sliding window to adjust our profit
        profit = 0
        left =0
        maxProfit = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right

            profit = prices[right] - prices[left]
            
            if profit > maxProfit:
                maxProfit = max(maxProfit, profit)

        
        return maxProfit