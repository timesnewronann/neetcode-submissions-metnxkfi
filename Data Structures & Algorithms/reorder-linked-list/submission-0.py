# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to have a pointer at the head of the list
        # and need a pointer at the tail of the list
        # Then we need to start by moving the head to the front
        # then the tail
        # Then we move them towards each other
        # THese are singly linked lists so they don't have a pointer to
        # The previous which makes it inconvenient
        # We could find the midpoint of the linked list
        # Then reverse the second half
        # Then merge the halves 

        # we can use slow and fast to get the half of the list
        slow = head
        fast = head.next

        # while fast is not null and fast has not reached the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # beginning of the second half of the list
        second = slow.next

        # split the list into two different list
        slow.next = None

        prev = None

        # reverse the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the two list
        second = prev
        first = head

        while second:
            # merge the lists
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            
            # shift the pointers
            first = temp1
            second = temp2
