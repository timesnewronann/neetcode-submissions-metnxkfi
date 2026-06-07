class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # I think this can be done with two pointers potentially
        # you would have left which is the value getting updated with the greatest element
        # then you would move the right pointer through each value in the list
        # to find the greatest in the list
        # then once you have the greatest replace the left value
        # and keep moving the pointers until left is at len(arr) - 1 then just put arr[left] = -1

        max_val = -1

        for right in range(len(arr) -1, -1, -1):
            temp = arr[right]
            arr[right] = max_val
            max_val = max(max_val, temp)
            

        return arr
            
