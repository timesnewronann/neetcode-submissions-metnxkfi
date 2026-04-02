#create a listnode class 
class ListNode:
    def __init__(self,val, next_node = None):
        self.val = val
        self.next = next_node 

class LinkedList:
    
    def __init__(self):
        #maintain head and tail
        self.head = ListNode(-1) #temp node 
        self.tail = self.head #assume list is none empty


    
    def get(self, index: int) -> int:
        #start at the beginning of list
        curr = self.head.next
        i = 0

        #go until
        while curr:
            if i == index:
                return curr.val
            #shift pointer
            #increment i
            i += 1
            curr = curr.next
        return -1 #index out of bound error
        

    def insertHead(self, val: int) -> None:
        #take value and convert it into a node
        new_node = ListNode(val)
        new_node.next = self.head.next 
        self.head.next = new_node

        #tail should always point to the last node
        if not new_node.next:
            #if list was empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        #move tail pointer to new node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0 
        curr = self.head
        while i < index and curr:
            #move curr to node before the target node
            i += 1
            curr = curr.next

        #check if curr and curr next exists
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False 
        
    def getValues(self) -> List[int]:
        #traversal over list
        curr = self.head.next 
        result = []

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
        
