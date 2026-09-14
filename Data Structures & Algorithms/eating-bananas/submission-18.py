class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we would use a binary search to determine what the optimal eating rate is 
        low = 1
        highest = max(piles)

        result = highest

        # binary search first
        while low <= highest:
            k = (low + highest) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                result = min(result, k)
                highest = k - 1 
            
            else:
                low = k + 1


        return result
