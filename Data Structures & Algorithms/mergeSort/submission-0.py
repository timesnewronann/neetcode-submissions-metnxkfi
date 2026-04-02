# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs[:]
        
        middle = len(pairs) // 2

        left = pairs[:middle]
        right = pairs[middle:]

        left_sort = self.mergeSort(left)
        right_sort = self.mergeSort(right)

        i = 0 
        j = 0

        merged = []

        while i < len(left_sort) and j < len(right_sort):
            if left_sort[i].key <= right_sort[j].key:
                merged.append(left_sort[i])
                i += 1
            else:
                merged.append(right_sort[j])
                j += 1 
        
        while i < len(left_sort):
            merged.append(left_sort[i])
            i += 1 
        
        while j < len(right_sort):
            merged.append(right_sort[j])
            j += 1 
        
        return merged
