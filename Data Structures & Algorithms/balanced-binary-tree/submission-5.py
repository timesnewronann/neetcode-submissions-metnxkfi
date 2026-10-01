# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(root):
            if not root:
                return 0

            left = max_depth(root.left)
            right = max_depth(root.right)

            if left < 0 or right < 0:
                return -1 

            # the heights are valid but are differe > 1 
            if abs(left - right) > 1:
                return -1 
            
            return 1 + max(left, right)

        return max_depth(root) != -1