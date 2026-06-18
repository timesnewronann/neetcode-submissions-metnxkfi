# need a node class
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        # create two nodes left and right
        self.left = ListNode(0)
        self.right = ListNode(0)

        # connect the two nodes together
        # temp left and right nodes
        # helpful technique to deal with linkedlist problems
        # helps with edge cases
        # temp nodes deals with a node in the middle of the linked lists no edge cases at the beginning or end
        self.left.next = self.right
        self.right.prev = self.left
        

        # getting a value is O(n) if we have to iterate through the whole list 
    def get(self, index: int) -> int:
        curr = self.left.next 

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0: 
            return curr.val
        
        return -1

        

    def addAtHead(self, val: int) -> None:
        # create a new node
        node = ListNode(val)
        next = self.left.next
        prev = self.left
        
        # set the prev.next to the new node we created
        prev.next = node

        # set the next node's prev value to the new node
        next.prev = node
        
        # set the node's next and prev pointers
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.right
        prev = self.right.prev

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next

            index -= 1 
        
        if curr and index == 0:
            # create a new node
            node = ListNode(val)

            next = curr 
            prev = curr.prev

            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        # delete the node that are pointer is at
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0:
            next = curr.next
            prev = curr.prev

            next.prev = prev
            prev.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)