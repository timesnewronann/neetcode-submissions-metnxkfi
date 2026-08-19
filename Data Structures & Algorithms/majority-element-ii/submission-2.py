class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # create a hashMap
        count = defaultdict(int)

        # go through each number
        for num in nums:
            count[num] += 1 

            # if the length hashMap > 2 
            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)

            # go through each number and count
            for num, count in count.items():
                # check if the count > 1 
                if count > 1:
                    # put the number in the new hashMap
                    new_count[num] = count - 1 
            # update the count 
            count = new_count

        result = []

        # how do we verify they show up over a 3rd
        for num in count:
            if nums.count(num) > len(nums) // 3:
                # append to the result
                result.append(num)

        return result

            
            