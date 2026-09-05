# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # to avoid inserting into an empty list without a head node
        # create a temp node
        temp = ListNode()
        # we will insert into the temp by using tail
        tail = temp

        # go through the lists while they're not empty
        while list1 and list2:
            # check which value is smaller
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # we need to move our tail
            tail = tail.next

        if list1:
            tail.next = list1
            list1 = list1.next
        
        if list2:
            tail.next = list2
            list2 = list2.next

        # we want to return everything after the first dummy value
        return temp.next
        