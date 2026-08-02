class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we can use the votes algorithm
        # what is the brute force
        # we could put all of the values in a hashMap count the elemnts
        # then sort the values and return the value with the greatest element
        result = 0

        count = 0

        for num in nums:
            if count == 0:
                result = num

            if num == result:
                count += 1 

            else:
                count -= 1

        return result