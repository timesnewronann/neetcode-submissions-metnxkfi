class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # go through the asteroids
        for asteroid in asteroids:
            # check the asteroid direction
            # so compare the two signs
            # while we have an asteroid to compare in our stack and our top of the stack is positive
            # collision can occur when top of stack is moving right and an assteroid is moving left
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = asteroid + stack[-1]

                # if the asteroid is negative blow up the asteroid on the stack
                if diff < 0:
                    stack.pop()

                # if the asteroid is positive blow up the current asteroid 
                elif diff > 0:
                    asteroid = 0

                else:
                    # both blow up
                    asteroid = 0
                    stack.pop()

            # if the signs are the same they will never meet just continue 
            if asteroid:
                stack.append(asteroid)

        # return the stack
        return stack