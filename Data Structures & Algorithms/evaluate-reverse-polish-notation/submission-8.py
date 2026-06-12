class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # this is similar to baseball game I think 
        # we use a stack to solve this 
        # we need to go through the tokens in the stack
        stack = []

        for token in tokens:
            if token == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) + int(val2))
            
            elif token == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            
            else:
                stack.append(int(token))
        
        return stack[0]