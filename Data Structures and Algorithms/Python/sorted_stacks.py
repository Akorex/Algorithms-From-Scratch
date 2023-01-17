from stack import ArrayStack

class SortedStack(ArrayStack):
    def __init__(self):
        super().__init__()
        self.temp_stack = ArrayStack()

    def push(self, item):
        if self.is_empty() or item < self.top():
            super().push(item)

        else: 
            while self.top() is not None and item > self.top():
                self.temp_stack.push(self.pop())
            super().push(item)

            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())        
