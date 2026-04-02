class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        
        item = self.stack[-1]
        del self.stack[-1]
        return item
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        item = self.stack[-1]
        return item
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        
        min = float('inf')

        for num in self.stack:
            if num < min:
                min = num
        
        return min 
        
