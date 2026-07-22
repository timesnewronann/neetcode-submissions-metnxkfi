class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we can solve this question with a binary search 
        # we can update the pointers based on if our banana eating variable affects our hours comparison
        left = 1

        right = max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2 
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                result = min(result, k)
                right = k - 1 

            else:
                left = k + 1 

        
        return result