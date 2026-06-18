class MinStack:

    def __init__(self):
        self.n = []
        self.minn = []

    def push(self, val: int) -> None:
        self.n.append(val)
        if self.minn:
            val = min(val, self.minn[-1])
        self.minn.append(val)

    def pop(self) -> None:
        self.n.pop()
        self.minn.pop()

    def top(self) -> int:
        return self.n[-1]

    def getMin(self) -> int:
        return self.minn[-1]
