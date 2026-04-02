# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge case of inserting into an empty list
        dummy = ListNode()

        #set tail node to the dummy
        tail = dummy

        while list1 and list2:
            #check if 1 is less than 2
            if list1.val < list2.val:
                tail.next = list1
                #update pointer
                list1 = list1.next
            else:
                tail.next = list2
                #update pointer
                list2 = list2.next
            
            #update tail pointer regardless which gets updated
            tail = tail.next

        #check that every list is empty
        #find the non empty list and insert it
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
