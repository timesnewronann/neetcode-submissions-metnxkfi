class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # we can go through the list of elements backwards so that we always start with -1
        # we can swap the values to the right with the max element

        curr_max = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = curr_max
            curr_max = max(arr[i], curr_max)
            arr[i] = temp
        
        return arr