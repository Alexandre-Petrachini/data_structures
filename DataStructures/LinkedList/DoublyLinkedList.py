from typing import Optional, Generator

class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        data (int): The data stored in the node.
        prev (Optional[Node]): A reference to the previous node in the list.
        next (Optional[Node]): A reference to the next node in the list.
    """

    def __init__(self, data: int, prev: 'Optional[Node]' = None, next: 'Optional[Node]' = None) -> None:
        self.data: int = data
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next

class DoublyLinkedList:
    """
    Implements a doubly linked list with operations for insertion, removal, traversal,
    and size determination.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.counter: int = 0

    def __iter__(self) -> Generator[Node, None, None]:
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        nodes = [str(node.data) for node in self]
        return f"[{', '.join(nodes)}]"

    def traverse(self) -> str:
        return " <-> ".join([str(node.data) for node in self])

    def insert_start(self, value: int) -> None:
        node = Node(value, next=self.head)
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.counter += 1

    def insert_end(self, value: int) -> None:
        node = Node(value, prev=self.tail)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.counter += 1

    def remove(self, value: int) -> None:
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.counter -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list.")

    def size(self) -> int:
        return self.counter