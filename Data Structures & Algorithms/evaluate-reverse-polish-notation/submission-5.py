class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif c == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif c == "-":
                val = - (stack.pop() - stack.pop())
                stack.append(val)
            elif c == "/":
                first = stack.pop()
                sec = stack.pop()
                print(first, sec)
                val = sec / first 
                stack.append(int(val))
            else:
                stack.append(int(c))
        
        print(stack)
        return round(stack[-1])