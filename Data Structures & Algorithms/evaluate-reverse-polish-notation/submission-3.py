class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif char == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif char == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            
            else:
                stack.append(int(char))
        
        return stack[0]
            