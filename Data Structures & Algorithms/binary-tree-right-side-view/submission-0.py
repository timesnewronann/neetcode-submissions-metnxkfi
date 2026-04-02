# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #use a bfs to get the right values
        result = []

        queue = deque([root])

        while queue:
            rightSide = None
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                result.append(rightSide.val)

        return result