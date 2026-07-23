# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we can do this recursivrly

        # check if we are on the root
        if not root:
            # not on the root so we need to insert a new node
            return TreeNode(val)
        
        # check if the current value we are on is less than the root's value
        if root.val < val:
            # we should insert into the right side
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        
        return root 