class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # goal is to return the list of asteroids that don't blow up or exist after collisions
        # we can use a stack to handle the collisions
        # whenever a stack and asteroid collide we can pop it off our stack
        # to handle the logic of when to blow up we can track the difference
        
        stack = []


        # go through each asteroid 
        for asteroid in asteroids:
            # we only want to blow up the asteroid if the asteroids are on course for collision so if our top of our stack is positive and the asteroid is negative
            # also only while we have an asteroid on our stack#
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the difference
                diff = stack[-1] + asteroid
                # check if the diff is positive or negative
                if diff < 0:
                    # current asteroid wins blow up our stack's
                    stack.pop()

                elif diff > 0:
                    # blow up the asteroid
                    asteroid = 0 
                
                else:
                    # blow both up since they share the same value
                    stack.pop()
                    asteroid = 0

            # if we have an asteroid add it to our stack
            if asteroid:
                stack.append(asteroid)


        # after we process all the asteroids return our stack
        return stack
            