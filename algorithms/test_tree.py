from algorithms.bst import Tree

def test_insertion_root():
    tree = Tree()
    tree.insert(10)
    assert tree.root.data==10
    
def test_insertion_right():
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    
    assert tree.root.data==10
    assert tree.root.rightChild.data==12
    
def test_insertion_left():
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    
    assert tree.root.data==10
    assert tree.root.leftChild.data==5
    
def test_insertion_both():
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    
    assert tree.root.data==10
    assert tree.root.leftChild.data==5
    assert tree.root.rightChild.data==12
    
def test_deletion_left():
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.delete(5)
    
    assert tree.root.leftChild.data==4
    assert tree.root.leftChild.leftChild.data==3
    
def test_deletion_right():
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(13)
    tree.insert(14)
    tree.delete(12)
    
    assert tree.root.rightChild.data==13
    assert tree.root.rightChild.rightChild.data==14


def test_find():
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(13)
    
    find_1 = tree.find(12)
    find_2 = tree.find(800)
    
    assert find_1 == True
    assert find_2 == False