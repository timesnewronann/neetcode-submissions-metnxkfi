class Solution:
    def climbStairs(self, n: int) -> int:
        # how would I solve this off of first glance
        # so our goal is to return the number of ways to climb to the top of the staircase
        # so we want permutations
        # dynamic programming question
        one = 1
        two = 1

        for i in range(n -1):
            temp = one
            one = one + two
            two = temp

        return one