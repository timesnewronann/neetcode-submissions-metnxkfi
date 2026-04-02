# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Inorder traversal iterative approach with a stack
        stack = []
        curr = root

        while curr or stack:
            while curr:
                #we need to go back up to current after processing current
                stack.append(curr)
                #keep going left and go through every left subtree node
                curr = curr.left 

            #pop the most recently added value from stack
            curr = stack.pop()
            #update n cause we visited a node
            k -= 1 
            if k == 0:
                return curr.val

            #go through the right subtree
            curr = curr.right
        