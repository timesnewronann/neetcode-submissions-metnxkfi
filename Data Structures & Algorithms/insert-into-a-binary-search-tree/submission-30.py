# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # this can be completed recursively

        # base case 
        if not root:
            return TreeNode(val)

        # check if our current root.val < val
        if root.val < val:
            # go to the right side of the tree
            root.right = self.insertIntoBST(root.right, val)
        
        elif root.val > val:
            # go to the right left side:
            root.left = self.insertIntoBST(root.left, val)
        
        return root