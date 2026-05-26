# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # This question can be solved iteratively and recursively
        # we'll do the recursive dfs version
        current = root

        while current is None:
            new_node = TreeNode(val)
            
            return new_node
        
        if current.val > val:
            # go on the left side
            current.left = self.insertIntoBST(current.left, val)
        
        elif current.val < val:
            # go on the right side
            current.right = self.insertIntoBST(current.right, val)
        
        else:
            # we can insert
            current.val = val
        
        return current

