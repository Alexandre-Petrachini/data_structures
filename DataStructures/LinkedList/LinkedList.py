from typing import Generator, Optional
from Node import Node


class LinkedList:
    """
    Implements a singly linked list with operations for insertion, removal, traversal,
    and size determination.

    Attributes:
        head (Optional[Node]): The first node in the list, or None if the list is empty.
        counter (int): The number of nodes in the list.
        tail (Optional[Node]): The last node in the list, or None if the list is empty.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.counter: int = 0
        self.tail: Optional[Node] = None

    def __iter__(self) -> Generator[Node, None, None]:
        """
        Allows iteration over the linked list nodes.
        """
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.
        """
        if self.head is None:
            return "[]"
        nodes = [str(node.data) for node in self]
        return f"[{', '.join(nodes)}]"

    def traverse(self) -> str:
        """
        Traverses the linked list and returns a string representation of node data.
        """
        nodes = [str(node.data) for node in self]
        return " -> ".join(nodes)

    def insert_start(self, value: int) -> None:
        """
        Inserts a new node at the start of the linked list.
        """
        self.counter += 1
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def size(self) -> int:
        """
        Returns the number of nodes in the linked list.
        """
        return self.counter

    def insert_end(self, value: int) -> None:
        """
        Inserts a new node at the end of the linked list.
        """
        self.counter += 1
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, value: int) -> None:
        """
        Removes a node with the specified value from the linked list.
        """
        if self.head is None:
            raise ValueError("LinkedList.remove(value): value not in LinkedList")
        
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = prev
                self.counter -= 1
                return
            prev, current = current, current.next

        raise ValueError("LinkedList.remove(value): value not in LinkedList")