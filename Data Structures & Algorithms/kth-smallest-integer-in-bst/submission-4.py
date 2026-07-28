# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS traversal

        # iterative stack in order dfs
        n = 0

        stack = []

        # what node are we currently at ?
        curr = root 

        while curr or stack:
            while curr:
                # we need to go back up to the current after processing
                stack.append(curr)

                # keep going left and go through every node in the left subtree
                curr = curr.left

            # pop the last element off of the stack
            curr = stack.pop()

            n += 1 

            if n == k:
                # current node processed is the value we are looking for, we are looking for hte kth smallest element
                return curr.val

            # update root's subtree
            curr = curr.right 

        
        