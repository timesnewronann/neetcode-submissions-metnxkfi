class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Goal return the minimum eating rate of bananas so we can eat all bananas within the hours
        # So we have to find the optimal banana eating raate within the constraint of 9

        # Somehow this is a binary search range question

        # I guess we would need a low range of banana eating rate
        # And a high range 

        # our middle point would be the optimal banana eating rate
        # the upper bound to eat bananas would have to be at hours == k
        # at the highest koko would need to eat 25 bananas in example 2
        # we need to have hours <= len(piles) since koko can only eat a full pile per and will stop
        # so if we have 5 piles but 4 hours it wouldn't be successful

        left = 1
        # the biggest pile we can eat
        right = max(piles)

        result = right # potentially the optimal rate

        while left <= right:
            # banana eating rate 
            k = (left + right) // 2 

            hours = 0 # how many hours it takes to eat the piles

            for pile in piles:
                hours += math.ceil(float(pile) / k)

            if hours <= h:
                result = min(result, k)

                right = k - 1 
            
            else:
                # rate was too small find a bigger eating rate
                left = k + 1 

        return result

