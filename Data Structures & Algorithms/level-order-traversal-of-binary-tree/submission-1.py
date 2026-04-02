# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs and go through each node in the tree
        #For each level we'll add each node into a queue 
        #We'll store the node's values inside of a list
        
        result = []

        queue = deque()

        #check if we're on the root
        if root:
            queue.append(root)

        #while len(queue) > 0
        while queue:
            val = []
            for i in range(len(queue)):
                curr = queue.popleft()
                val.append(curr.val)

                #check if there's a left subtree or subtree 
                if curr.left:
                    #add into the queue
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(val)

        return result

        
