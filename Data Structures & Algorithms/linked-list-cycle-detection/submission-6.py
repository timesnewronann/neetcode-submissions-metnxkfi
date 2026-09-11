# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can use a slow and fast pointer
        # if the fast pointer == slow pointer value then we have a cycle
        slow = head
        fast = head

        # loop through the list while we have a fast node and a fast.next 
        while fast and fast.next:
            # move the pointers
            slow = slow.next

            fast = fast.next.next

            # check if the values are the same
            if slow == fast:
                return True

        return False 