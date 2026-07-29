class Solution:
    def trap(self, height: List[int]) -> int:
        # Goal -> Return the maximum area of water that can be trapepd between the bars
        # We need to calculate the area
        # So we need to find the space where water can be stored
        # So we need to calculate the area between the heights
        # Where it

        # start with defining our two pointers 
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        area = 0

        # formula for trapped water at index i: min(height[left], height[right]) - height[i]
        # we'll use the leftMax and rightMax of the heights to compare when to shift pointers and calculate the differences

        while left < right:
            if leftMax < rightMax:
                left += 1 
                # update leftMax with the bigger max
                leftMax = max(leftMax, height[left])

                # take the leftMax - height[left] and add into our area, this will never be negative due to the leftMax update before the area update
                area += leftMax - height[left]
            else:
                right -= 1 
                rightMax = max(rightMax, height[right])

                area += rightMax - height[right]


        return area