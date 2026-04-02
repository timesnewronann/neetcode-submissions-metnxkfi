#First we should make a listNode which will be used to chain the list
class ListNode:
    def __init__(self,val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        #maintain the head and tail
        self.head = ListNode(-1) #default value of - 1, temp node
        self.tail = self.head 

    
    def get(self, index: int) -> int:
        #iterate through the linked list
        curr = self.head.next # ignore the node 

        #iterate i times
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next 
        
        #if pointer is null
        return -1 #index out of bounds 
            

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) #make a new node 
        #insert at head is easy with temp node
        new_node.next = self.head.next
        self.head.next = new_node

        #if tail is not pointing at the last pointer
        #Edge case if it was pointing at the dummy node
        if not new_node.next:
            #If list was empty before inserting 
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        #dummy node is at the tail of the list
        #if list is empty
        self.tail.next = ListNode(val) 
        #move tail pointer to the new node we inserted
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        #Remove the node at the index 
        i = 0
        curr = self.head #when we remove a node we need a reference to the pointer before to fix pointer
        while i < index and curr:
            #move curr to previous node before the target node 
            i += 1
            curr = curr.next
        
        #check if target node and previous node exists
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr 
            curr.next = curr.next.next # set's to the node after
            return True
        return False 


    def getValues(self) -> List[int]:
        curr = self.head.next 
        result = []

        while curr:
            result.append(curr.val)
            curr = curr.next 

        return result 
