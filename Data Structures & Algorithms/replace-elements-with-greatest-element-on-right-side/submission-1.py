class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # I think this is a two pointer question where we have to swap the values
        # We also should go through this question backwards since the last number is guranteed to be -1
        max_val = -1

        for right in range(len(arr) -1, -1, -1):
            temp = arr[right]
            arr[right] = max_val
            max_val = max(max_val, temp)

        return arr