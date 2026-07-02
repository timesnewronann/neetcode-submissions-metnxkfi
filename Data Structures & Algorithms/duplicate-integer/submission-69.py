class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can use a hashSet to check if we have seen the current number before
        # if we have return true since logically we have a duplicate
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            
            hashSet.add(num)

        return False