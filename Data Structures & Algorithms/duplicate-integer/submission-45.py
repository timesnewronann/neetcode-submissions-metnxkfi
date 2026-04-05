class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set 
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False 