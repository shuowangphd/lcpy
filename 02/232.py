class MyQueue:

    def __init__(self):
        self.i, self.o = [], []

    def push(self, x: int) -> None:
        self.i.append(x)

    def pop(self) -> int:
        self.peek()
        return self.o.pop()

    def peek(self) -> int:
        if len(self.o) == 0:
            while self.i:
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self) -> bool:
        return not self.i and not self.o


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()