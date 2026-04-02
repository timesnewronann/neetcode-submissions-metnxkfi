class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for number in nums:
            #check if the number is already in the set
            if number in hashSet:
                return True 
            hashSet.add(number)

        return False 