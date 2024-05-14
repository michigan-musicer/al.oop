"""
For this lab, CircularLinkedList type objects can only contain objects of type int.
A better solution is to make the container generic, e.g. by following 
https://docs.python.org/3/library/typing.html#generics.
"""

"""
A circular linked list's last node points back to the head of the list.
For more on ordinary linked lists, see https://www.cs.cmu.edu/~15122-archive/n17/lec/10-linkedlist.pdf
or https://en.wikipedia.org/wiki/Linked_list.
"""
class CircularLinkedList:
    class Node:
        # I guess screw typing next here lol
        def __init__(self, next, val : int):
            self.next = next
            self.val = val

    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self) -> str:
        string = "["
        current_node = self._head
        for i in range(self.size()):
            string += f"{current_node.val}, "
            current_node = current_node.next
        string = string[:-2]
        string += ']'
        return string

    def empty(self) -> bool:
        # YOUR IMPLEMENTATION HERE
        pass

    def size(self) -> int:
        # YOUR IMPLEMENTATION HERE
        pass

    def head(self):
        # YOUR IMPLEMENTATION HERE
        pass

    """
    Insert item before index in the list. For example: 
    - On a CircularlLinkedList [1, 2, 3], call insert(1, 0) to insert 0 at index 1. New list is [1, 0, 2, 3].
    - On a CircularlLinkedList [], call insert(0, 5) to insert 5 at index 0. New list is [5].
    """
    def insert(self, index : int, item : int) -> None:
        # YOUR IMPLEMENTATION HERE
        pass        
        """
        Three cases: 
        - no items in list.
        - insert at 0 (need to change _begin).
        - insert elsewhere in non-empty list.
        """
        if self.size() == 0:
            # lst.insert(0, 5) where lst = [] 
            new_node = self.Node(None, item)
            self._head = new_node
        elif index == 0:
            # lst.insert(0, 5) where lst = [1, 2, 3]
            new_node = self.Node(self._head, item)
            self._head = new_node
            last_node, i = self._head, 0
            while i < self.size() - 1:
                last_node = last_node.next
                i += 1
            last_node.next = self._head
        else:
            # lst.insert(2, 5) where lst = [1, 2, 3]
            # lst after = [1, 2, 5, 3]
            new_node = self.Node(None, item)
            current_node, i = self._head, 0
            while i < index - 1:
                current_node = current_node.next
                i += 1
            new_node.next = current_node.next
            current_node.next = new_node            

        self._size += 1
    
    """
    Adds item to the end of the linked list.
    - On a CircularlLinkedList [1, 2, 3], call append(1) to get [1, 2, 3, 0].
    - On a CircularlLinkedList [], call append(5) to get [5].
    """
    def append(self, item: int) -> None:
        # YOUR IMPLEMENTATION HERE
        pass

    """
    remove item at index in the list. For example: 
    - On a CircularlLinkedList [1, 2, 3], call remove(1) to get [1, 3].
    - On a CircularlLinkedList [4, 5, 6], call remove(0) to get [5, 6].
    """
    def remove(self, index: int) -> int:
        # YOUR IMPLEMENTATION HERE
        pass

# run test cases if this is the main script file.
if __name__ == "__main__":
    # test cases here...
    lst = CircularLinkedList()
    print(f"lst should be empty, which is {lst.empty()}")
    for i in range(4):
        lst.append(i + 1)
    print(f"lst should be [1, 2, 3, 4], is {lst} with size {lst.size()} and head {lst.head().val}")
    lst.insert(2, 10)
    print(f"lst should be [1, 2, 10, 3, 4], is {lst} with size {lst.size()} and head {lst.head().val}")
    lst.remove(3)
    print(f"lst should be [1, 2, 10, 4], is {lst} with size {lst.size()} and head {lst.head()}")
    lst.remove(0)
    print(f"lst should be [2, 10, 4], is {lst} with size {lst.size()} and head {lst.head().val}")
