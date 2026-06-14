class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we can loop through the array 2 times 
        ans = []

        for i in range(2):
            # go through the list of numbers
            for num in nums:
                ans.append(num)

        
        return ans