class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we want to use a stack to get the token values
        stack = []

        # go through each token
        for token in tokens:
            # check if the token is a plus
            if token == "+":
                # add up the two values
                stack.append(int(stack.pop()) + int(stack.pop()))

            # elif * similar logic to +
            elif token == "*":
                # multiply
                stack.append(int(stack.pop()) * int(stack.pop()))
            
            # logic for subtract and divide is a little more confusing
            elif token == "-":
                first_item = stack.pop()
                second_item = stack.pop()

                stack.append(int(second_item) - int(first_item))

            elif token == "/":
                first_item = stack.pop()
                second_item = stack.pop()

                stack.append(int(second_item /first_item))
            
            # otherwise push the token into the stack
            else:
                stack.append(int(token))

        # return the last item in the list which should be the value
        return stack[0]
