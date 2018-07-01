#6.35 leaky stack 
class LeakyStack:
    def __init__(self, max_len=5):
        self._data = [None] * max_len 
        self._size = 0
        self._top = -1
        self.MAX_LEN = max_len
    def _is_empty(self):
        return len(self._size) == 0
    def __len__(self):
        return self._size
    def top(self):
        return self._data[self._top]
    def push(self, data):
        avail = (self._top + 1) % self.MAX_LEN
        self._data[avail] = data
        self._top = avail
        self._size += 1
    def pop(self):
        ans = self._data[self._top]
        self._data[self._top] = None
        self._top = (self._top - 1 ) % self.MAX_LEN
        self._size -= 1
        return ans
        
        
