class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # I think we can use a binary search to solve this question
        # We would adjust our eating rate based on the hours 

        # the smallest rate of bannana eating
        lowest = 1 

        # highest rate of bannana eating
        highest = max(piles)

        # track the result of our bannana eating rate
        result = highest

        while lowest <= highest:
            # track the amount of hours it takes to eat with our current rate
            hours = 0 
            k = (lowest + highest) // 2

            # we should go through each pile of bannana's now
            for pile in piles:
                # hours is our the amount in the pile / banana eating rate
                # add up our hours it takes to eat the piles
                hours += math.ceil(pile / k)

            # check if our current right is less than the hours
            # is this eating speed fast enough to finish within the allowed time?
            # if it is less than it is fast enough
            if hours <= h:
                result = min(result, k)
                highest = k - 1 
            
            # eating too slow
            else:
                # we need a larger speed to eat fast enough
                lowest = k + 1 


        return result