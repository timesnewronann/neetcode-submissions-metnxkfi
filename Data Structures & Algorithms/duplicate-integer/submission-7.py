class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # use a hashSet to check for duplicates
        hashSet = set()

         # go through each number in the list
        for num in nums:
        #check if the number is already in the set
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False