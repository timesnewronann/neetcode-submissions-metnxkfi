class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to get all of the tokens 
        stack = []

        for token in tokens:
            # check if we have the operators
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            
            elif token == "-":
                first = int(stack.pop())
                second = int(stack.pop())

                stack.append(second - first)

            elif token == "/":
                first = stack.pop()
                second = stack.pop()

                stack.append(int(second / first))
            
            else:
                stack.append(int(token))

        return stack[-1]