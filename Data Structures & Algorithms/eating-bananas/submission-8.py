class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We want to track the k and use a binary search to find the optimal bananna eating speed
        # Koko can only eat from 1 pile within the hour so if she eats a whole pile she can't start eating from another pile
        # lowest to highest banana eating speed
        # she must eat at least 1 banana
        low = 1
        high = max(piles) # the largest bannana eating speed
        result = high

        while low <= high:
            # we will calculate the middle point
            mid = (low + high) // 2 
            hours = 0 

            # go through each pile in the piles
            for pile in piles:
                # check if the number of hours is exceeding our h
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = min(result, mid)
                high = mid - 1 

            else:
                low = mid + 1 

        
        return result