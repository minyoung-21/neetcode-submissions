class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) > 0:
                    if c == ')' and '(' == stack[-1]:
                        stack.pop()
                    elif c == '}' and '{' == stack[-1]:
                        stack.pop()
                    elif c == ']' and '[' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True