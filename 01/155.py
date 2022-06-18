class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        mn = self.getMin()
        if mn == None or val < mn:
            mn = val
        self.q.append((val,mn)) 

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if self.q:
            return self.q[-1][0]

    def getMin(self) -> int:
        if self.q:
            return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()