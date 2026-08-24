class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force we can place the numbers in a hashMap
        # and return the list of items that appear more than n/3
        # this is O(n) and O(1) solution
        # we can optimize this by
        # Taking out a count of the number everytime we iterate
        # and if we values left in the hashmap that would be majority elements

        # first we can create a counts hashMap
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

            # if the length of the hashMap > 2 
            if len(counts) <= 2:
                continue
            
            # create a new hashMap to track the counts 
            new_count = defaultdict(int)

            # go through the hashMap
            for num, count in counts.items():
                # we have to compare the majority elements
                if count > 1:
                    # place this number into our hashMap with the count - 1 
                    new_count[num] = count -1 

            # update the count with the values of our new hashMap
            counts = new_count

        result = []

        # go through the hashMap and add the values which appear more than a 3rd
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result