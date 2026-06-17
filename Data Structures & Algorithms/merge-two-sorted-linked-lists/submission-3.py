# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        linkedList = []
        # we need to maintain two pointers 1 at each list
        while list1 and list2:
            if list1.val < list2.val:
                linkedList.append(list1.val)
                list1 = list1.next
            else:
                linkedList.append(list2.val)
                list2 = list2.next
            
        while list1:
            linkedList.append(list1.val)
            list1 = list1.next
        
        while list2:
            linkedList.append(list2.val)
            list2 = list2.next
        
        # convert the list into a linked list
        if not linkedList:
            return None
        
        head = ListNode(linkedList[0])
        current = head
        
        for i in range(1, len(linkedList)):
            current.next = ListNode(linkedList[i])
            current = current.next


        return head

