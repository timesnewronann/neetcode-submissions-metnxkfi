# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we would do a dfs to get the height of left and right sides
        # and we would maintain a variable to check the condition
        # balanced if node's left and right subtree heights differ by 1 or 0
        # we do a dfs postorder
        
        # return [true/false, height]
        def dfs(root):
            if not root:
                # empty tree -> balanced
                return [True, 0]
            
            # is it balanced left and right
            left = dfs(root.left)
            right = dfs(root.right)

            # from the root is it balanced? Balanced means is the entire tree balanced at all
            balanced = (left[0] and right[0]
                     and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        # return True 

