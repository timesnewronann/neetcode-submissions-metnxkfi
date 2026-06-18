# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and hare problem
        # we move one pointer twice
        # and move another pointer once
        # if the fast pointer == slow then there is a cycle
        curr = head
        slow = curr
        fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
        
        