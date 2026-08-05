class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # our goal is to get the most optimal eating rate while getting as close to h hours as possible
        lowest = 1 
        highest = max(piles)

        result = highest 

        while lowest <= highest:
            eating_rate = (lowest + highest) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / eating_rate)

            # check if the hours < h we need to eat slower we ate too quickly
            if hours <= h:
                result = min(result, eating_rate)
                highest = eating_rate - 1 
            
            # we're eating too slowly
            else:
                lowest = eating_rate + 1 

        return result

