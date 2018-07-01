class Red_blue_stack:
    def __init__(self):
        self._data = [None] * 100
        self._red_size = 0
        self._blue_size = 0
        self._red_top = -1
        self._blue_top = len(self._data)
    def __len__(self, color):
        if color == "red":
            return self._red_size
        else:
            return self._blue_size
    def is_empty(self, color):
        if color == "red":
            return self._red_size == 0
        else:
            return self._blue_size == 0
    def push(self, color, data):
        if color == "red":
            self._data[self._red_top + 1] = data
            self._red_top += 1
            self._red_size += 1
        else:
            self._data[self._blue_top - 1] = data
            self._blue_top -= 1
            self._blue_size += 1
    def pop(self, color):
        if color == "red":
            if not self.is_empty("red"):
                ans = self._data[self._red_top]
                self._data[self._red_top] = None
                self._red_top -= 1
                self._red_size -= 1
                return ans
            else:
                return ("stack is empty")
        else:
            if not self.is_empty("blue"):
                ans = self._data[self._blue_top]
                self._data[self._blue_top] = None
                self._red_top += 1
                self._red_size -+ 1
                return ans
            else:
                return ("Stack is empty")
    def top(self, color):
        if color == "red" and not self.is_empty("red"):
            return self._data[self._red_top]
        elif color == "blue" and not self.is_empty("blue"):
            return self._data[self._blue_top]


            
            
                
