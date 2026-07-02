class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # so we have to check two pointers can have the same value at different indices
        # and the abs(i - j) <= k

        left = 0

        hashSet = set()

        for right in range(len(nums)):
            # breaks the constraint
            if right - left > k:
                hashSet.remove(nums[left])
                left += 1 

            if nums[right] in hashSet:
                return True
            
            hashSet.add(nums[right])

        return False