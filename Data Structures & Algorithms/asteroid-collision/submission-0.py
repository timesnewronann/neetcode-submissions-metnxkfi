class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # go through the asteroids
        for asteroid in asteroids:
            alive = True
            # check the asteroid direction
            # so compare the two signs
            # while we have an asteroid to compare in our stack and our top of the stack is positive
            # collision can occur when top of stack is moving right and an assteroid is moving left
            while stack and stack[-1] > 0 and asteroid < 0:
                top = stack[-1]

                # if the signs are different find the smaller asteroid
                # if asteroid1 < asteroid2:
                    # pop asteroid1
                if abs(top) < abs(asteroid):
                    stack.pop()
                    continue 

                elif abs(top) == abs(asteroid):
                # blow both up 
                    stack.pop()
                    alive = False
                    break
                
                else:
                    # our current asteroid blows up
                    alive = False
                    break

            # if the signs are the same they will never meet just continue 
            if alive:
                stack.append(asteroid)

        # return the stack
        return stack