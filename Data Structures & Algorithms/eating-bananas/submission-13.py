class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we can use a binary search to go through the piles
        # define the smallest eating rate
        low = 1

        # highest eating rate
        high = max(piles)

        result = high

        # while low < right
        while low <= high:
            # calculate the eating rate
            k = (low + high) // 2 

            hours = 0
            # go through each pile
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                result = min(result, k)
                high = k - 1 
            
            else:
                low = k + 1


        return result 