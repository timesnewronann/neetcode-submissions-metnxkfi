# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # We have to unpack a list
        if len(pairs) <= 1:
            return pairs[:]

        middle = len(pairs) // 2

        left = pairs[:middle]
        right = pairs[middle:]

        left_sorted = self.mergeSort(left)
        right_sorted = self.mergeSort(right)

        merged = []

        i = 0
        j = 0

        while i < len(left_sorted) and j < len(right_sorted):
            # how do we unpack this do we need to do a for loop in the sorted
            if left_sorted[i].key <= right_sorted[j].key:
                merged.append(left_sorted[i])
                i += 1 
            else:
                merged.append(right_sorted[j])
                j += 1 


        while i < len(left_sorted):
            merged.append(left_sorted[i]) 
            i += 1 
        
        while j < len(right_sorted):
            merged.append(right_sorted[j])
            j += 1 
        
        return merged