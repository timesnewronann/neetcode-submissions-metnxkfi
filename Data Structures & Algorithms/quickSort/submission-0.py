# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # in place sorting algorithm
        # call the helper
        self.partition(pairs, 0, len(pairs) - 1)

        return pairs

    def partition(self, pairs, left, right):
        # base case when the subarray is length 1 already sorted
        # sort the array in place
        if (right - left + 1) <= 1:
            return 

        # set the pivot to the last value in the list
        pivot = pairs[right] # right most 
        leftPivot = left

        for i in range(left, right):
            # Partition
            if pairs[i].key < pivot.key:
                # swap the element at i with what's at left index
                pairs[i], pairs[leftPivot] = pairs[leftPivot], pairs[i]

                # move left pivot forward
                leftPivot += 1 
        
        pairs[right] = pairs[leftPivot]
        pairs[leftPivot] = pivot

        # call on the left half
        self.partition(pairs, left, leftPivot - 1)
        # call on the right half
        self.partition(pairs, leftPivot + 1, right)
