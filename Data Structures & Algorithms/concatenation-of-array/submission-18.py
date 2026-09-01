class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we can go through the list of nums twice
        result = []

        for i in range(2):
            # go through the list and add it in the result
            for num in nums:
                result.append(num)

        return result