class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to parse the tokens
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif token == "-":
                item1 = int(stack.pop())
                item2 = int(stack.pop())

                stack.append(item2 - item1)
            
            elif token == "/":
                item1 = int(stack.pop())
                item2 = int(stack.pop())

                stack.append(int(item2 / item1))
            
            else:
                stack.append(int(token))

        return stack[-1]