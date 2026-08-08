class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # maybe we can use a hashMap track the counts of each num
        result = 0

        count = 0 

        for num in nums:
            # when count reaches 0 the previous candidate has been canceled out by other values -> choose the current number as the new candidate
            if count == 0:
                result = num

            # if num matches the candidate, increase its count
            if num == result:
                count += 1 
            # Otherwise decrease the count because this cancels out the occurence
            else:
                count -= 1 

        return result


        
                