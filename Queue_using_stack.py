class Queue_using_stack:
    def __init__(self):
        self.in_stack = ArrayStack()
        self.out_stack = ArrayStack()
        self.front = None
    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()
    def enqueue(self, d):
        self.in_stack.push(d)
    def dequeue(self):
        if self.out_stack.is_empty():
            print("inside out stack if")
            if not self.in_stack.is_empty():
                print("inside in stack if", self.in_stack.is_empty())
                while not self.in_stack.is_empty() > 0:
                    #print("inside while")
                    res = self.in_stack.pop()
                    self.out_stack.push(res)
                self.front = self.out_stack.top()
                return self.out_stack.pop()
            else:
                raise Empty("queue is empty")
        else:
            return self.out_stack.pop()
