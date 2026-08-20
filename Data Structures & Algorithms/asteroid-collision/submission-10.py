class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # we can use a stack to track the asteroids 
        # and pop off of the stack to track collisions
        stack = []

        for asteroid in asteroids:
            # we'll only collide
            # when two asteroids meet
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