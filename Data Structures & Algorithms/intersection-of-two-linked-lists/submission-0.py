# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # goal is to return the node at which the two lists intersect
        # if the two linked lists have no intersection return null
        # we want to have two pointers at each linked list
        # iterate through the lists and check if the nodes are the same
        # once the value is the same we will return the nodes where they are the same
        i = headA
        j = headB

        while i is not j:
            i = i.next if i else headB
            j = j.next if j else headA
        
        return i

        