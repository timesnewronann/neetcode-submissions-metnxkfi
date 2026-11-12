class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we can use a binary search to adjust our speed
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            # calculate our middle
            middle = (left + right) // 2 

            hours = 0

            # go through each pile
            for pile in piles:
                hours += math.ceil(pile / middle)

            if hours <= h:
                result = min(result, middle)
                right = middle - 1 
            
            else:
                left = middle + 1 

        return result

