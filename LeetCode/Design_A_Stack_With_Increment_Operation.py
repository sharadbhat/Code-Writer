# Leetcode
# https://leetcode.com/problems/design-a-stack-with-increment-operation/


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        self.stack = [i + val for i in self.stack[:k]] + self.stack[k:]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
