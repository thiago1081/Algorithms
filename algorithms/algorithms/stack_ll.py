#Stacks with Linked_lists
from list_node import ListNode

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            
    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data
    
    def peek(self):
        return self.top.data if self.top is not None else None
            
    def __iter__(self):
        current = self.top
        while current is not None:
            yield current.data
            current = current.next