class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # bruteforce solution is to solve this with a hashmap
        # that solution would be O(n) time and space
        # we can optimize this by removing a count of each number 
        
        # get the counts
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

            # if the length of the hashMap <= 2 keep going
            if len(counts) <= 2:
                continue

            # we want to create a new hashmap which will sstore the values of the old hashmap and the decremented count
            new_count = defaultdict(int)

            for num, count in counts.items():
                # check if the count of the number is > 1
                if count > 1:
                    # we can store the value in the new map
                    new_count[num] = count - 1
            
            # update the count with the value of the new hashmap
            counts = new_count
                
        
        # then we want to store the values in the list
        result = []

        # go through the nums
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result