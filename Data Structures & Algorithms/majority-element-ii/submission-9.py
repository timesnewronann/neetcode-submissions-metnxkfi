class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # we can brute force this with hashMap but it would not be O(1)
        # so we can use 2 hashMaps -> everytime the num + 1 in hashMap

        # start by counting the nums
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

            # check if the lenght of the counts <= 2 
            if len(counts) <= 2:
                continue
            
            

            # define a second hashMap
            new_count = defaultdict(int)

            for num, count in counts.items():
                if count > 1:
                    new_count[num] = count - 1 

            counts = new_count

        result = []

        for num in counts:
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result

