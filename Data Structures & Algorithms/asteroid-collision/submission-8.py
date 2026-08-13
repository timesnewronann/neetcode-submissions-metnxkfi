class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to compare if the top of the stack to the current asteroid to see which blows up

        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                # we are on course for collision
                diff = stack[-1] + asteroid

                if diff < 0:
                    # stack's asteroid explodes
                    stack.pop()

                elif diff > 0:
                    # asteroid blows up
                    asteroid = 0
                
                else:
                    # both blow up
                    stack.pop()
                    asteroid = 0

            # if we have an asteroid add it to the stack
            if asteroid:
                stack.append(asteroid)

        return stack