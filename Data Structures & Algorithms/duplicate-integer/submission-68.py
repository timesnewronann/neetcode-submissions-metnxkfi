class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hashSet to check if the number is already there which means we have a duplicate
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            
            hashSet.add(num)
        
        return False