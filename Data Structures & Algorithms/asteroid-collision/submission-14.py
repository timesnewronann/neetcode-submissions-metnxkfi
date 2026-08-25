class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # our goal is to return the list of asteroids which don't collide
        # we can use a stack to track which asteroids we currently have processed
        stack = []

        # go through the entire list
        for asteroid in asteroids:
            # we only have a collision 
            # if the asteroids going towards each other 
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the difference between the two asteroids
                diff = stack[-1] + asteroid

                # if the diff is neg
                if diff < 0:
                    # blow up the current stack's asteroid
                    stack.pop()

                elif diff > 0:
                    # blow up the current passing asteroid
                    asteroid = 0

                else:
                    # they both collide
                    asteroid = 0
                    stack.pop()

            # add the asteroid into our stack
            if asteroid:
                stack.append(asteroid)


        # return the asteroid
        return stack