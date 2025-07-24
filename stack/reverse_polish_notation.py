from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                to_subtract = stack.pop()
                target = stack.pop()
                stack.append(target - to_subtract)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(dividend / divisor))
            else:
                stack.append(int(token))

        return stack[0]
