# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we have to go through the input arrays and build the binary tree
        # so for preorder we would use a preorder dfs

        # go through inorder with an inorder dfs ?

        # base case if our roots are empty 
        if not preorder or not inorder:
            return None

        # we need to create a root node
        # by definition the first node in a preorder is the root
        root = TreeNode(preorder[0])

        # get the middle point
        mid = inorder.index(preorder[0])

        # get the left subtree
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root