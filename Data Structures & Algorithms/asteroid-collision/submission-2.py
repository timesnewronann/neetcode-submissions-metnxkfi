class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to hold our asteroids
        # have a variable that stores the difference between our asteroid and the asteroid on the sstack
        stack = []

        for asteroid in asteroids:

            # iterate while the stack is not empty and  top of stack is > 0 and asteroid is < 0 
            # only way for a collision to happen
            while stack and stack[-1] > 0 and asteroid < 0:
                # diff between our asteroids
                diff = stack[-1] + asteroid

                # we have three cases to check
                if diff < 0:
                    stack.pop()
                
                elif diff > 0:
                    asteroid = 0
                
                # we blow both up since the asteroid == stack[-1]
                else:
                    asteroid = 0 
                    stack.pop()
                    
            
            # if the signs are the same and we have an asteroid push it into the stack

            if asteroid:
                stack.append(asteroid)

        return stack
