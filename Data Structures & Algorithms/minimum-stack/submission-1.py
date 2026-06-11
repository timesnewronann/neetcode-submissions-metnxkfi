class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        
        popped_element = self.stack[-1]
        del self.stack[-1]
        return popped_element
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        
        top_item = self.stack[-1]
        return top_item

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None

        minimum = float('inf')

        for value in self.stack:
            if value < minimum:
                minimum = value
        
        return minimum



        
        
