class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__():
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans
    def enqueue(self, d):
        if self._size == len(self._data):
            self._resize(2 * self._size)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = d
        self._size += 1
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
        self._front = 0
        
        
