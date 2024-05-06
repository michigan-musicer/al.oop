class Stack:
    def __init__(self):
        self._s = []
        self._size = 0

    def empty(self) -> int:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def front(self) -> str:
        return self._s[0]
    
    def push(self, item : str) -> None:
        self._size += 1
        self._s.append(item)
    
    def pop(self) -> str:
        self._size -= 1
        return self._s.pop()    
