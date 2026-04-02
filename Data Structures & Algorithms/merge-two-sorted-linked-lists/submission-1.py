# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Use a dummy node to avoid the edge case of inserting into an empty list
        dummy = ListNode()

        #set the tail as the dummy node 
        tail = dummy 

        #go through the lists while they're not empty
        while list1 and list2:
            #Check which value is lower
            if list1.val < list2.val:
                tail.next = list1
                #update to the next pointer
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            #update the tail pointer 
            tail = tail.next

        #exhaust all the lists
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
        