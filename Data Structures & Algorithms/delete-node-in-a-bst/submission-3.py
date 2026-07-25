# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we can use a helper function to find the minimum node which will be helpful in our 2 child node cases
    def findMinimum(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left
        
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case 
        if not root:
            return None

        # we need to first find the target delete value
        if root.val < key:
            # go to the right side
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        # we found the target node
        else:
            # if we don't have a left node
            if not root.left:
                return root.right

            
            elif not root.right:
                return root.left

            else:
                minNode = self.findMinimum(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root

        