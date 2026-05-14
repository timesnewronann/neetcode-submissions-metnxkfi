# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we can probably use a dfs or a bfs
        # check if the root is null
        current = root

        if current is None:
            new_node = TreeNode(val)
            return new_node
        
        # we can do a dfs which is recursive 
        if current.val > val:
            # value I am inserting is smaller than the current node
            # search the left side 
            current.left = self.insertIntoBST(current.left, val)
        elif current.val < val:
            # value I am inserting is greater than the current node
            # search right side
            current.right = self.insertIntoBST(current.right, val)
        else:
            # insert into that spot
            current.val = val

        return current