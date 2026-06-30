# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # handle edge cases where the list is null or 0
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            # keep reducing and cutting in half
            merge_list = []

            # go through each list
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                merge_list.append(self.mergeList(list1, list2))
            
            # update our lists variable
            lists = merge_list

        # return until there is 1 list left
        return lists[0]

     # we need to merge two sorted linked list
    def mergeList(self, list1, list2):
        temp = ListNode()

        tail = temp

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1

        elif list2:
            tail.next = list2
        

        return temp.next
