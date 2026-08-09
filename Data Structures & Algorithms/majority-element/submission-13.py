class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we want to vote for the majority element
        # track the counts 
        count = 0

        # track our result
        result = 0

        # go through each num
        for num in nums:
            # check if the current count == 0 
            if count == 0:
                # update our current num
                result = num 

            # check if we have the same number that means cast the vote
            if num == result:
                count += 1 
            
            else:
                count -= 1 

        return result