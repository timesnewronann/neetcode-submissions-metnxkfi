# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we can create a helper function to get the minimum node
    def findMinimum(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case 
        if not root:
            return None # delete the node

        # check if the roots value is < than the key
        if root.val < key:
            # go to the right side
            root.right = self.deleteNode(root.right, key)
        
        # Check the left side
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        # we found the target
        else:
            # we check the children node cases 0,1 or 2
            if not root.left:
                # search the right side
                return root.right

            elif not root.right:
                return root.left

            # we have the 2 child case
            else:
                minNode = self.findMinimum(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        
        return root
                


        