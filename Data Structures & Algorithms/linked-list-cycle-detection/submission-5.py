# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can use a slow and fast pointer to determine if there is a cycle
        # eventually the slow will catch up to fast if there is a cylce
        slow = head
        fast = head

        while fast and fast.next:
            # we need to move the pointers first
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False