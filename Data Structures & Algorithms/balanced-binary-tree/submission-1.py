# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return true or false if it is height-balanced 

        # left and right subtrees of every node are only differ by no more than 1 

        # This is a DFS question since we want to look at the heights I think

        # We can make this o(n)

        # Use DFS to compute the heights at each node
        # while calculating the heights of the left and right subtrees we also check if the tree rooted at the current node is balanced
        # LeftHeight - rightHeight > 1 update a global variable

        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        
        return dfs(root)[0]