# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we want to create a helper function to find the minimum
    def findMinValue(self,root):
            curr = root

            while curr and curr.left:
                curr = curr.left

            return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # two scenarios where we need to delete a node that has 0 or 1 children
        # or delete a node that has 2 children or even 2 childrem that have children
        # base case
        if not root:
            return None

        # Search for the value to remove
        # check if the current val is less than the value we went to remove
        if root.val < key:
            # search the right side for the value
            root.right = self.deleteNode(root.right, key)


        elif root.val > key:
            # search the left side for the value
            root.left = self.deleteNode(root.left, key)

        # done searching we found the value
        else:
            # check if we are missing the left node
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                minNode = self.findMinValue(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

            
        return root

        


        
