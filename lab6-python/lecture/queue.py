class Queue:
    def __init__(self):
        self._q = []
        self._size = 0

    def empty(self) -> int:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def front(self) -> str:
        return self._q[0]
    
    def push(self, item : str) -> None:
        self._size += 1
        self._q.append(item)
    
    def pop(self) -> str:
        self._size -= 1
        return self._q.pop(0)    
