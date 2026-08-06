class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to compare our asteroidds 
        # whenever we need to blow up an asteroid we can just pop it off the stack

        stack = []

        # go through each asteroid
        for asteroid in asteroids:
            # we will loop through our stack if it has certain conditions
            # The stacks top asteroid is positive
            # The current asteroid is negative 
            # These will collide
            # Our stack is not empty
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the difference between the two asteroids
                diff = stack[-1] + asteroid

                # now we do the comparison logic on which asteroid blows up
                if diff < 0:
                    # we have a negative value that means our stack's asteroid gets blown up
                    stack.pop()
                elif diff > 0:
                    # we blow up the asteroid
                    asteroid = 0 # since this breaks the while loop condition
                
                # other wise they're the same value so they both blow up
                else:
                    stack.pop()
                    asteroid = 0

            # if we have an asteroid we should push it into our stack
            if asteroid:
                stack.append(asteroid)


        #return the stack after this is done
        return stack