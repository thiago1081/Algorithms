# Stack implementation using python built in list

class Stack:
    def __init__(self):
        self.data = []
        
    def size(self):
        return len(self.data)
    
    # Push data to the top of the stack
    def push(self, data):
        self.data.append(data)
        
    # Pop the top element of the stack   
    def pop(self):
        return None if self.size() == 0 else self.data.pop()
    
    # Get the value of the top element without popping it
    def peek(self):
        return None if self.size() == 0 else self.data[-1]
    def isEmpty(self):
        return (len(self.data) == 0)