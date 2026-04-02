# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #We can use a fast and slow pointer to detect if there's a cycle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True

        return False