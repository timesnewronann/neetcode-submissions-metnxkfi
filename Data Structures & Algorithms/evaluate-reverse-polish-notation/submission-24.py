class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to parse through each token
        # whenever we encounter an operator we'll pop the tokens off and perform the operations
        stack = []

        for token in tokens:
            # check if we encounter the operators
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif token == "-":
                first_item = int(stack.pop())
                second_item = int(stack.pop())

                stack.append(second_item - first_item)

            elif token == "/":
                first_item = stack.pop()
                second_item = stack.pop()

                stack.append(int(second_item / first_item))

            else:
                stack.append(int(token))

        return stack[-1]