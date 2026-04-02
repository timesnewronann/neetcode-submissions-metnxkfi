class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #We can use a hashSet 
         # hashset's naturally cannot contain duplicates
         # We create a hashSet
        hashSet = set()

         # go through the list
        for num in nums:
            #Check if the num is in hashSet
            if num in hashSet:
                return True # there is a duplicate then
            #add the number in otherwise
            hashSet.add(num)
        return False 