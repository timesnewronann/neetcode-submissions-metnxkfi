class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to compare the collisions
        stack = []

        # go through each asteroid
        for asteroid in asteroids:
            # if the stack isn't empty and the stacks value is positve and the current asteroid is negative we'll check the collision
            while stack and stack[-1] > 0 and asteroid < 0:
                # calculate the diff
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