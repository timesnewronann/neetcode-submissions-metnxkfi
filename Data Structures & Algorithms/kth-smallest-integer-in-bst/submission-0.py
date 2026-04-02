# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Create a counter to track the elements
        self.count  = 0
        self.result = None
        #We'll use a dfs 
        #in order traversal
        def dfs(node):
            if not node:
                return None

            #go left child
            dfs(node.left)
            #in order add to a sorted list
            #increment the counter after visiting a node
            self.count += 1 

            #Check if this node is the kth smallest
            if self.count == k:
                self.result = node.val
                return

            dfs(node.right)

            #return list 
        dfs(root)

        return self.result