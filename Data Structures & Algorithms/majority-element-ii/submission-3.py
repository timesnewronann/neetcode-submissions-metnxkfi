class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force we can go through each number place it in a hashmap
        # and then check for the majority
        # O(n) time and O(n) space
        # but we can bring it down to O(1) -> if we remove the counts every time

        # use a hashMap to track the count of numbers
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

            # check if the hashMap is > 2
            if len(counts) <= 2:
                continue

            # we can create a new hashMap to track the new counts
            new_count = defaultdict(int)

            # then we want to go through the num, count in the hashMap
            for num, count in counts.items():
                # check if the count > 1
                if count > 1:
                    # put the number into the new hashmap
                    new_count[num] = count - 1 
                
            # update the count
            counts = new_count
        

        result = []

        # verify which numbers show up > 1/3
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result
                