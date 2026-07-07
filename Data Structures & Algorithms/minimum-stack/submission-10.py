class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        self.minimum = min(val, self.minimum)
        self.min_stack.append(self.minimum)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.minimum = self.min_stack[len(self.min_stack) - 1]
        else:
            self.minimum = float("inf")

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        # print(self.stack, self.min_stack)
        return self.min_stack[len(self.stack) - 1]