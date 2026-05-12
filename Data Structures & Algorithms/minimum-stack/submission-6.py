import bisect


class MinStack:
    stack = []

    sorted_elements = []

    def __init__(self):
        self.stack = []
        self.sorted_elements = []
        return None

    def find_index(self, val: int):
        return bisect.bisect_left(self.sorted_elements, val)

    def sort_insert(self, val: int) -> int:
        index = self.find_index(val)
        self.sorted_elements.insert(index, val)
        return index

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sort_insert(val)

    def pop(self) -> None:
        self.sorted_elements.pop(self.find_index(self.stack[-1]))
        self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.sorted_elements[0]