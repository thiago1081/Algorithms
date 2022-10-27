from list_node import ListNode

class CircularList:
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
        self.tail.next = self.head
        self.size += 1
    
    # Delete a node from list with given data
    def delete(self, data):
        current = self.head
        prev = None
        while current != self.tail:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        if current is not None and current.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                prev.next = self.head
                self.tail = prev
            self.size -= 1   
        
    def __iter__(self):
        current = self.head
        while current != self.tail:
            data = current.data 
            current = current.next
            yield data
        if self.tail is not None:
            yield self.tail.data