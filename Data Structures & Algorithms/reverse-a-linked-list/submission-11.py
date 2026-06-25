# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solve it iteratively first
        # curr = head
        # prev = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev

        # what is the base case -> we only have 1 node to flip
        # if list is empty
        if not head:
            # return null
            return None
        
        # recursively go to the end of the list the nthe last node becomes the new head
        tail = head
        if head.next:
            tail = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return tail
