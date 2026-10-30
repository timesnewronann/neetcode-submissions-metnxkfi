class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a stack to process the tokens
        stack = []

        for token in tokens:
            if token == "+":
                item1 = stack.pop()
                item2 = stack.pop()
                stack.append(item1 + item2)

            elif token == "*":
                item1 =stack.pop()
                item2 =stack.pop()
                stack.append(item1 * item2)
            
            elif token == "-":
                item1 =stack.pop()
                item2 = stack.pop()
                stack.append(item2 - item1)
            
            elif token == "/":
                item1 = stack.pop()
                item2 = stack.pop()
                stack.append(int(item2 / item1))

            else:
                stack.append(int(token))

        return stack[-1]