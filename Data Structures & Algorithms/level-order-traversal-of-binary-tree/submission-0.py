# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we want to use a binary search
        #create a result array
        result = []

        #create a queue
        queue = deque()

        #we didn't check if we were on the root node
        if root:
            queue.append(root)

        #go through the queue while it's not empty
        while queue:
            #store the value in a list
            val = []
            #go through the level
            for i in range(len(queue)):
                #get the current level stored
                curr = queue.popleft()
                #store the nodes into the list 
                val.append(curr.val)
                #check if the left tree and right tree have nodes still
                if curr.left:
                    #add them into the queue
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            #add the values from each level into the result array
            result.append(val)

        return result
               
