# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # This question is basically merge sorted linked lists with extra steps
        # handle the edge cases where the list is null or the list is 0 long
        if not lists or len(lists) == 0:
            return None

        
        while len(lists) > 1:
            # keep reducing and splitting into half
            merged_list = []

            # incrementer is 2 because we are looking at pairs of linkedlists
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                # merge the two lists together
                merged_list.append(self.merge(list1, list2))
            
            # update our lists variable
            lists = merged_list

        # keep doing that until there is one list left
        return lists[0]

    def merge(self, list1, list2):
        # return the output list 
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