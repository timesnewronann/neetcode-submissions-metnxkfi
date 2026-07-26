# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Return the kth smallest value in the tree
        # The left subtree of every node contains only nodes with keys less than the node's key
        # kth smallest I think of a bucket sort since we want only certain grouping of values

        # we can use a depth search to search for the smallest elements
        # we want to use an inorder traversal
        # Track the visited node with a variable
        count = k
        result = root.val

        def dfs(root):
            nonlocal count, result

            if not root:
                return 

            dfs(root.left)
            if count == 0:
                return
                
            count -= 1
            if count == 0:
                result = root.val
                return

            dfs(root.right)

        dfs(root)

        return result