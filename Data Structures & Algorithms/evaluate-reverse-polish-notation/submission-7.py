class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to evaluate
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif token == "-":
                value1, value2 = stack.pop(), stack.pop()
                stack.append(value2 - value1)
            
            elif token == "/":
                value1, value2 = stack.pop(), stack.pop()
                stack.append(int(value2 / value1))
            
            else:
                stack.append(int(token))

        return stack[0]