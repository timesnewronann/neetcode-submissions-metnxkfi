class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Check if the list has a duplicate
         # return true or false
         # use a hashset's properties
        hashSet = set()

         #go through the list
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False 