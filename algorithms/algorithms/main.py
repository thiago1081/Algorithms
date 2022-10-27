#just an example

from linked_list import LinkedList
from double_linked_list import DoublyLinkedList
from circular_list import CircularList 
from bracket_matching import has_matching_brackets


# Linked list Example

print(' Linked list Example. Appending and printing 1 to 10')
ll = LinkedList()

for i in range(10):
    ll.append(i)

for i in ll:
    print(i)
print('After deleting 5')
ll.delete(5)

for i in ll:
    print(i)
    
# Doubled Linked list Example
print('Doubled Linked list Example. Appending and printing 1 to 10')
dll = DoublyLinkedList()

for i in range(10):
    dll.append(i)

for i in ll:
    print(i)
print('After deleting 5')
dll.delete(5)

for i in dll:
    print(i)
    
# Doubled Linked list Example
print('Circular Linked list Example. Appending and printing 1 to 10')
cll = CircularList()

for i in range(10):
    cll.append(i)

for i in cll:
    print(i)
print('After deleting 5')
cll.delete(5)

for i in dll:
    print(i)

print('Test with bracket matching')

sl = ( 
   "{(foo)(bar)}[hello](((this)is)a)test", 
   "{(foo)(bar)}[hello](((this)is)atest", 
   "{(foo)(bar)}[hello](((this)is)a)test))" 
) 
for s in sl: 
   m = has_matching_brackets(s) 
   print("{}: {}".format(s, m)) 