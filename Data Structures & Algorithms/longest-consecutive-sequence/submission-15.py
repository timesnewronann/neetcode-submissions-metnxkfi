class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can put the nums in a hashSet
        hashSet = set(nums)
        longest = 0

        # 2, 20, 4, 3, 5

        for num in nums:
            if (num - 1) not in hashSet:
                length = 0

                while num + length in hashSet:
                    length += 1 


                    longest = max(longest, length)

            
        return longest
