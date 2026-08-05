class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to push the operations and token
        stack = []

        for token in tokens:
            # check if we have the operators
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "-":
                token1 = stack.pop()
                token2 = stack.pop()

                stack.append(token2 - token1)
            
            elif token == "/":
                token1 = stack.pop()
                token2 = stack.pop()

                stack.append(int(token2 / token1))
            
            # otherwise push the token onto the stack
            else:
                stack.append(int(token))
        
        return stack[-1]