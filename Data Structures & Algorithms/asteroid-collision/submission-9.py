class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to compare the asteroids when they will blow up
        stack = []

        for asteroid in asteroids:
            # check if our current stack's asteroid will collide with the asteroid
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the diff between the two 
                diff = stack[-1] + asteroid

                # if the diff < 0
                if diff < 0:
                    stack.pop()

                elif diff > 0:
                    asteroid = 0

                else:
                    # blow both up
                    stack.pop()
                    asteroid = 0

            
            # add the asteroids
            if asteroid:
                stack.append(asteroid)

        
        # return the stack
        return stack