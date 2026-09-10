class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to compare if the stack will blow up
        stack = []

        for asteroid in asteroids:
            # check if the two asteroids or on route to collide
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid

                if diff < 0:
                    stack.pop()

                elif diff > 0:
                    asteroid = 0

                else:
                    stack.pop()
                    asteroid = 0

            if asteroid:
                stack.append(asteroid)


        return stack