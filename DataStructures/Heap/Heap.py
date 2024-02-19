from typing import List, TypeVar, Generic

T = TypeVar('T')

class Heap(Generic[T]):
    """
    A generic heap class implementing the heap data structure for elements of any orderable type.
    
    This class provides methods to add an element, remove the minimum element, and find the minimum element,
    with operations ensuring the heap property is maintained.
    """

    def __init__(self) -> None:
        self.__arr: List[T] = []

    def __up(self, index: int) -> None:
        """
        Bubbles the value at arr[index] up to maintain the heap property.
        """
        while index > 0 and self.__arr[index] < self.__arr[(parent := (index - 1) // 2)]:
            self.__arr[index], self.__arr[parent] = self.__arr[parent], self.__arr[index]
            index = parent

    def __down(self, index: int) -> None:
        """
        Bubbles the value at arr[index] down to maintain the heap property.
        """
        n = len(self.__arr)
        while index < n:
            extreme = index
            left = index * 2 + 1
            right = index * 2 + 2

            if left < n and self.__arr[left] < self.__arr[extreme]:
                extreme = left
            if right < n and self.__arr[right] < self.__arr[extreme]:
                extreme = right

            if extreme == index:
                break

            self.__arr[index], self.__arr[extreme] = self.__arr[extreme], self.__arr[index]
            index = extreme

    def heapify(self) -> None:
        """
        Converts an arbitrary list into a heap by enforcing the heap invariant.
        """
        for i in range(len(self.__arr) - 1, -1, -1):
            self.__down(i)

    def findMin(self) -> T:
        """
        Returns the minimum element in the heap.
        """
        if len(self.__arr) == 0:
            raise IndexError("findMin on empty heap")
        return self.__arr[0]

    def push(self, value: T) -> None:
        """
        Adds a new element to the heap.
        """
        self.__arr.append(value)
        self.__up(len(self.__arr) - 1)

    def pop(self) -> T:
        """
        Removes and returns the minimum element from the heap.
        """
        if len(self.__arr) == 0:
            raise IndexError("pop from empty heap")
        if len(self.__arr) == 1:
            return self.__arr.pop()
        result = self.__arr[0]
        self.__arr[0] = self.__arr.pop()
        self.__down(0)
        return result

    def pushpop(self, value: T) -> T:
        """
        Pushes a new value onto the heap and then pops and returns the minimum element.
        """
        if len(self.__arr) == 0:
            raise IndexError("pop from empty heap")
        result = self.__arr[0]
        self.__arr[0] = value
        self.__down(0)
        return result