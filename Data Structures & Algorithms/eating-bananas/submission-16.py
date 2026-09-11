class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we can use a binary search to determine the optimal eating rate
        low = 1

        high = max(piles)

        result = high

        while low <= high:
            # determine the eating rate
            k = (low + high) // 2

            hours = 0
            for pile in piles:
                # take the amount in the pile and get the hours from the eating rate
                hours += math.ceil(pile / k)

            if hours <= h:
                # shift the high lower so we can eat slower
                result = min(result, k)
                high = k - 1 
            
            else:
                low = k + 1
                
           

        return result
