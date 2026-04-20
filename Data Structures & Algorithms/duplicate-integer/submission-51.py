class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we could solve this with a hashmap and check if the count > 1 return True
        # more optimal to use a hashSet
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            
            hashSet.add(num)

        return False