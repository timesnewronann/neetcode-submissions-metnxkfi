# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # We want to do a dfs on this and swap the values in preorder 

        def dfs(root):
            if not root:
                return 

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
        