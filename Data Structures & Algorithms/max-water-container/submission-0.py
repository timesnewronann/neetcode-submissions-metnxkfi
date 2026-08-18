class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1 

        # track the max area we can have
        result = 0 

        # loop through until the pointers cross
        while left < right:
            # calculate our area
            area = min(heights[left], heights[right]) * (right - left)

            result = max(area, result)

            # move our pointers
            if heights[left] <= heights[right]:
                left += 1 

            else:
                right -= 1 

        
        return result