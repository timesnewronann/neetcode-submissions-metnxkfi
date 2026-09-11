# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we want to reorder the list
        # we can use a slow and fast pointer to get the middle of the list
        # then reverse the second half 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # the second half of the list is slow
        second = slow.next

        # split the list into two different lists
        slow.next = None

        prev = None

        # reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge them back in
        second = prev
        first = head

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

