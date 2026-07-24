# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we can make a helper function to get the minium
    # similar logic as going through a linkedlist
    def findMinimum(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left
        
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # we have two cases 
        # if we have 0 or 1 children (easy case)
        # 2 children (harder case)

        # delete the node base case
        if not root:
            return None

        # we need to find the target node first
        # if the current value is smaller than the target go to the right leaf
        if root.val < key:
            # search the right
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            # search the left
            root.left = self.deleteNode(root.left, key)
        
        # we found the node
        else:
            # then we have the cases with 0/1 or 2 nodes
            # check if we are missing the left node
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                # get a minimum node
                minNode = self.findMinimum(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root


    