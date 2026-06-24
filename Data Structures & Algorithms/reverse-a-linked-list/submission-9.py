# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solve iteratively
        # curr = head
        # prev = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev

        # what is the base case for this
        # we want to break this down into sub problems so maybe we break it down node by node
        # we know we are done reversing once prev is the head node since we want to reverse
        # since we have fully reversed

        if not head:
            return None
        
        # recursive call fuction on head.next
        tail = head

        if head.next:
            tail = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return tail