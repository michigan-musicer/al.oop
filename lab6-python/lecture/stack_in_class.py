class Stack:
    def __init__(self):
        # member variables, class variable...
        # if it starts with _, it is a private variable according to my style
        self._s = []
        self._size = 0

    def empty(self) -> int:
        return self._size == 0
    
    def size(self) -> int:
        return self._size

    def top(self):
        # return self._s[self._size - 1]
        return self._s[-1]        
    
    def push(self, item) -> None:
        self._size += 1
        self._s.append(item)
    
    def pop(self):
        self._size -= 1
        return self._s.pop(-1)

if __name__ == "__main__":
    s = Stack()
    print(s.empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.pop())
    print(s.top())

