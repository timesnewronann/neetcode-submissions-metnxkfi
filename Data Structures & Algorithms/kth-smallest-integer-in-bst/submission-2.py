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
        visited = []

        def dfs(root):
            if not root:
                return 0

            dfs(root.left)
            visited.append(root.val)
            dfs(root.right)

        dfs(root)

        return visited[k -1]