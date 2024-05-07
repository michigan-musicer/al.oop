"""
For this lab, CircularLinkedList type objects can only contain objects of type int.
A better solution is to make the container generic, e.g. by following 
https://docs.python.org/3/library/typing.html#generics.
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
        return self._size == 0

    def size(self) -> int:
        return self._size

    def head(self):
        return self._head

    """
    Insert one before the index. For example: 
    - On a CircularlLinkedList [1, 2, 3], call insert(1, 0) to insert 0 at index 1. New list is [1, 0, 2, 3].
    - On a CircularlLinkedList [], call insert(0, 5) to insert 5 at index 0. New list is [5].
    """
    def insert(self, index : int, item : int) -> None:
        node_to_insert = self.Node(None, item)

        if self._size == 0:
            self._head = node_to_insert
            self._head.next = self._head
        elif index == 0:
            current_idx, last_node = 0, self._head 
            while current_idx < self._size - 1:
                last_node = last_node.next
                current_idx += 1
            node_to_insert.next = self._head 
            self._head = node_to_insert
            last_node.next = node_to_insert
        else:
            current_idx, current_node = 0, self._head 
            while current_idx < index - 1:
                current_node = current_node.next
                current_idx += 1
            node_to_insert.next = current_node.next
            current_node.next = node_to_insert

        self._size += 1
        

    def append(self, item: int) -> None:
        self.insert(self.size(), item)


    def remove(self, index: int) -> int:
        if self._size == 1:
            self._head = None
        elif index == 0:
            # step 1: remove self._head
            self._head = self._head.next
            # step 2: find last node and set its next ptr to the new begin
            i, current_node = 0, self._head
            while i < self._size - 1:
                current_node = current_node.next
                i += 1 
            current_node.next = self._head
        else:
            # step 1: find node one before target index
            current_idx, node_before = 0, self._head
            while current_idx < index - 1:
                node_before = node_before.next
                current_idx += 1
            # step 2: chop out node after node before
            node_before.next = node_before.next.next

        self._size -= 1
    

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
