# We will come back to this some other day using iterators instead.
# Iterators allow us to solve Josephus more efficiently and really take advantage of the linked list structure.
# For iterators in C++, see https://eecs280staff.github.io/notes/17_Iterators.html

from circular_ll_solution import CircularLinkedList

"""
The Josephus problem, documented at https://en.wikipedia.org/wiki/Josephus_problem, is an extension of
"eeny-meeny-miny-moe". This function determines which item in the list is left over if we "count out" items 
until there is only one item left in the list. 
"""
def josephus(n : int, k : int) -> int:
    lst = CircularLinkedList()
    for i in range(n):
        lst.append(i + 1)
    # Complete the rest of the function.

# run test cases if this is the main script file.
if __name__ == "__main__":
    print(f"josephus(3, 2) should be 3, is {josephus(3, 2)}")
    print(f"josephus(41, 3) should be 31, is {josephus(41, 3)}")
    print(f"josephus(50, 20) should be 34, is {josephus(50, 20)}")
