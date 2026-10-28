# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        # if the head.next pointer is empty or the list is empty
        if not head or not head.next:
            return head


        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return temp