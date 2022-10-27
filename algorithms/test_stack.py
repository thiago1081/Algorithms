from algorithms.stack import Stack
def test_1():
    stack = Stack()
    stack.push(10)
    assert stack.size() == 1
    assert stack.peek() == 10
    stack.push(20)
    assert stack.size() == 2 
    assert stack.pop() == 20
