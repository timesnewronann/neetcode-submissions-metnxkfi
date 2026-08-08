class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        result = []

        for num in nums:
            counts[num] += 1 

            if len(counts) <= 2:
                continue
            
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

            
