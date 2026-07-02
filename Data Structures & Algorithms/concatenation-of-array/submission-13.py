class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we want to add the concatenation of two arrays
        result = []

        for i in range(2):
            for j in range(len(nums)):
                result.append(nums[j])

        return result