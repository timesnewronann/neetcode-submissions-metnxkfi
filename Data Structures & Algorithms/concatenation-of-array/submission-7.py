class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we want to double the length of the list
        # andd add the nums into it 
        # We can use enumerate 
        n = len(nums)
        result =[0] * (n * 2)

        for i, num in enumerate(nums):
            result[i] = result[i + n] = num

        return result