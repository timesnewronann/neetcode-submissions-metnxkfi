# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # similar to max_depth but we need to add up the left and right depths
        best_diameter = 0 

        def height(root):
            nonlocal best_diameter

            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            # update the best_diameter
            best_diameter = max(best_diameter, left + right)

            return 1 + max(left, right)

        
        height(root)

        return best_diameter