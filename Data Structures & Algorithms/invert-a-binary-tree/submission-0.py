# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we need to swap the values on the left tree with the values on the right
        # I think this is a dfs question
        # we would go through the left tree and then the right and swap them

        # dfs
        # what type of traversal maybe preorder 
        def dfs(root):
            # if the current node is null
            if not root:
                return []

            # swap the left and right children
            temp = root.left
            root.left = root.right
            root.right = temp

            # call dfs recursively on root.left and root.right
            dfs(root.left)
            dfs(root.right)
            
        
        dfs(root)

        return root

