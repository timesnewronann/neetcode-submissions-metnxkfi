class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # if the two asteroids will collide
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the diff between the two asteroids to determine the outcome
                diff = stack[-1] + asteroid 

                # that means the stack's asteroid blows up
                if diff < 0:
                    stack.pop()

                # our asteroid we're on blows up
                elif diff > 0: 
                    asteroid = 0 

                # otherwise both of them are the same size so they both blow up
                else:
                    asteroid = 0
                    stack.pop()

            
            # if we have an asteroid
            if asteroid:
                stack.append(asteroid)

        return stack