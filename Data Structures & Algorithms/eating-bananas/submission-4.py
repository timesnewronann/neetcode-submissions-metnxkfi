class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Our goal is to return minimum amount of bananas to eat to eat every banana in the piles within h hours
        # we can use a binary search to get the optimal banana eating count

        # The smallest amount of banana's we need to eat
        left = 1

        # highest amount of banana's we need to eat
        right = max(piles)

        result = right

        while left <= right:
            # This is K 
            mid = (left + right) // 2 
            hours = 0

            # go through each pile of bananas
            for pile in piles:
                # we will add the hours into this
                hours += math.ceil(float(pile) / mid)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1 

            else:
                left = mid + 1 
        
        return result
