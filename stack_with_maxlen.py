#6.16 stack with fixed length
class Stack_with_len:
    def __init__(self,max_len=None):
        if max_len is None:
            self._data = []
        else:
            self.MAX_LEN = max_len
            self._data = [None] * max_len
        self._size = 0
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return len(self._data)
    def push(self, data):
        if self.MAX_LEN is None:
            self._data.append(data)
            self._size += 1
            return True
        else:
            if self._size == self.MAX_LEN:
                return ("stack is full")
            else:
                self._data[self._size]=data
                self._size += 1
                return True
    def pop(self):
        if self.is_empty():
            return ("stack is empty")
        else:
            self._size -= 1
            return self._data.pop()
    def top(self):
        if self.is_empty():
            return ("Stack is empty")
        else:
            return self._data[-1]
        
        
