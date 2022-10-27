from .list_node import ListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  
        
    def append(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        
    def delete(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = self.head.next
                    if current == self.tail:
                        self.tail = self.tail.next
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                self.size -= 1
                return 
            prev = current
            current = current.next
    
    # Search through the linked list to see if there exists a node with the given data 
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    # Clear all nodes
    def clear(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current = self.head
        while current is not None:
            data = current.data
            current = current.next
            yield data