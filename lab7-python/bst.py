from typing import Optional

class BST:
    class Node:
        def __init__(self,  val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, initial_val=None) -> None:
        self._root = self.Node(initial_val) if initial_val else None
        self._size = 0    

    def empty(self) -> bool:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def root(self) -> Node:
        return self._root

    # Implement inorder traversal. See https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BinaryTreeTraversal.html
    # at section 12.5.1.3 for an example + Java implementation.
    # We will probably do this together in class.
    def __str__(self) -> str:
        # REPLACE pass WITH YOUR IMPLEMENTATION
        pass

    # Requires that val is not already in this BST.
    def insert(self, val=None) -> None:
        # REPLACE pass WITH YOUR IMPLEMENTATION
        pass
        
    # If target is in this BST, return the Node object with val=target.
    # Else, return None.
    def find(self, target=None) -> Optional[Node]:
        # REPLACE pass WITH YOUR IMPLEMENTATION
        pass

    # If you have extra time and want a challenge: try implementing delete.


if __name__ == "__main__":
    tree = BST(5)
    tree.insert(4)
    tree.insert(6)
    print(tree)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(9)
    print(tree)
    n = tree.find(4)
    print(f"n.val should be 4, is {n.val}")
    n = tree.find(20)
    print(f"n should be None, is {n}")
