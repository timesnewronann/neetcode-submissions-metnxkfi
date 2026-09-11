# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we can keep track of our current pointer
        # and the prev pointer
        curr = head
        prev = None

        # we can loop through the list while curr exists
        while curr:
            # use a temp node to reverse the lists and not lose the pointer
            # save the curr pointer's next pointer
            temp = curr.next 
            # update the curr.next pointer to be prev so we reverse and break the list
            curr.next = prev
            # set the prev value which is now the head 
            prev = curr 
            # set the curr value to be the temp so
            curr = temp

        # prev is now the head 
        return prev