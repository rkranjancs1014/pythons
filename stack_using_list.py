class ArrayStack:
    """LIFO stack implementation using Python list as underlying storage."""
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, d):
        self._data.append(d)
    def top(self):
        if self.is_empty():
            raise Empty("EmptySTack")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty("EmptyStack")
        return self._data.pop()
