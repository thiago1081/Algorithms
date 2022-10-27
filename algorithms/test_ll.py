from algorithms.linked_list import LinkedList

def test_1():
    linked_list = LinkedList()
    linked_list.append('adam')
    linked_list.append('kadmon')
    linked_list.append('atlas')
    linked_list.append(453)
    assert linked_list.size == 4
    linked_list.delete('atlas')
    assert linked_list.size == 3
    assert not linked_list.search('atlas') 
    assert linked_list.search(453)
    lista = []
    for i in linked_list:
        lista.append(i)
    assert lista[0] == 'adam'
    assert lista[1] =='kadmon'
    assert lista[2]==453
    