from math import floor

TABLE_CAPACITY = 128
WORD_SIZE = 2 ** 32

"""
If you are curious why this is a good hash function, read up on Donald Knuth's multiplicative hashing method,
which can be found on page 516 of Volume 3 of The Art of Computer Programming.
"""
def hash_int(x: int) -> int:
    hash = int(0x678DDE6F)
    M = TABLE_CAPACITY
    d = WORD_SIZE - 1
    return floor(M * ((hash / d * x) % 1))

"""DJB2 hash function, implementation taken from http://www.cse.yorku.ca/~oz/hash.html"""
def hash_string(s: str) -> int:
    hash = 5381
    M = TABLE_CAPACITY

    for c in s:
        hash = hash * 33 + ord(c)
    return hash % M

"""Define a custom exception for reaching hash table capacity"""
class HashTableCapacityError(Exception): ...
"""Define a custom exception for key not found in table"""
class HashTableKeyError(Exception): ...

class HashTable(dict):
    def __init__(self) -> None:
        self._size = 0
        self._table = [None for _ in range(TABLE_CAPACITY)]

    def size(self) -> int:
        return self._size

    def full(self) -> bool:
        return self._size == TABLE_CAPACITY

    def insert(self, key: type[int | str], value: type[int | str]) -> bool:
        # TODO: follow along with the instructor implementation of this function.
        ...

    """
    get should hash the key, then scan the table for matching values using linear probing.
    If you miss the explanation in class, see https://en.wikipedia.org/wiki/Linear_probing#Search
    """
    def get(self, key: type[int | str]) -> tuple[bool, type[int | str]]:
        ...

    """
    delete is a little tricky to implement correctly because linear probing needs to work even if
    a previously inserted key is removed. 
    At minimum, this function should search for a key and remove the corresponding entry from the table.
    For a challenge, implement the additional functionality to ensure that deletion maintains linear probing invariants.
    See https://en.wikipedia.org/wiki/Linear_probing#Deletion
    """
    def delete(self, key: type[int | str]) -> bool:
        ...

    """
    The following are operator overloads from Python's dict class (more on that in class).
    These are already completed and you don't need to worry about them.
    """
    def __getitem__(self, key: type[int | str]) -> type[int | str]:
        # return super().__getitem__(key)
        return self.get(key)
    
    def __setitem__(self, key: type[int | str], value: type[int | str]) -> None:
        # return super().__setitem__(key, value)
        return self.insert(key, value)

    def __delitem__(self, key: type[int | str]) -> None:
        # return super().__delitem__(key)
        return self.delete(key)

if __name__ == "__main__":
    table = HashTable()
    print(table.insert(5, 10))
    print(table.insert(6, 11))
    print(table.insert(7, 10))
    print(table.insert(7, 12))
    table["hello"] = "world"
    print(table.get(6))
    print(table["hello"])
    print(table.delete(5))
    print(table.delete(5))

