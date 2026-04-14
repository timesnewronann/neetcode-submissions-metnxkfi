class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # multiple ways to solve this we can use two pointers and check if one value is a duplicate by moving pointers until we check all permutations
        # optimal way to solve this we can use a hashSet
        hashSet = set()

        # go through the list of numbers
        for num in nums:
            # check if the number is already in our set
            if num in hashSet:
                return True # cannot have duplicates in a set so we know if it's there already then we have a duplcate

            hashSet.add(num)
        
        # no duplicate if we exit out of the loop
        return False