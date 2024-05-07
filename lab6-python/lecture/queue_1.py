# This file is named queue_1 to avoid shadowing queue from python stdlib.
class Queue:
    def __init__(self):
        self._q = []
        self._size = 0

    def empty(self) -> int:
        return self._size == 0
    
    def size(self) -> int:
        return self._size
    
    def front(self):
        return self._q[0]
    
    def push(self, item) -> None:
        self._size += 1
        self._q.append(item)
    
    def pop(self):
        self._size -= 1
        return self._q.pop(0)    
