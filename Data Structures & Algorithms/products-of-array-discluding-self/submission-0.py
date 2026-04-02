class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I think we'll use a prefix sum
        # For each index we're on we multiply every other index and store it in our current index
        # on index 
        # 0 -> 2 * 4 * 6 = 48 
        # 1 -> 1 * 4 * 6 = 24 
        # 2 -> 1 * 2 * 6 = 12 
        # 3 -> 1 * 2 * 4 = 8

        #We want our product to be 1 because if we multiply it by 0 it's gonna break the code
        
        #We can use a prefix and post fix and output it 

        #intially get a result output array that we'll return
        result = [1] * (len(nums)) # default value of 1 

        #do the prefixes first
        prefix = 1
        #go through each position
        for i in range(len(nums)):
            #go through each postion and put it onto the array
            result[i] = prefix
            prefix *= nums[i]  #compute the prefixes this way   
        
        #do similar to postfix but backwards 
        postfix = 1 
        for i in range(len(nums) - 1, - 1, -1):
            result[i] *= postfix # multiply prefix and postfix together
            postfix *= nums[i] 

        return result


            

