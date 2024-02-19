from Node import Node
from typing import Generator, Optional


class CircularLinkedList:
    """
    Implements a singly circular linked list with operations for insertion, removal, traversal,
    and size determination.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.counter: int = 0

    def __iter__(self) -> Generator[Node, None, None]:
        if not self.head:
            return
        current = self.head
        while True:
            yield current
            current = current.next
            if current == self.head:
                break

    def __str__(self) -> str:
        if not self.head:
            return "[]"
        return " -> ".join([str(node.data) for node in self]) + " -> ..."

    def insert_start(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            # Find the last node to complete the circle
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        self.counter += 1

    def insert_end(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            # Find the last node to update its next to new node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.counter += 1

    def remove(self, value: int) -> None:
        if not self.head:
            return
        
        current = self.head
        prev = None
        while True:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:  # Removing the head
                    # If it's the only node in the list
                    if current.next == self.head:
                        self.head = None
                    else:
                        self.head = current.next
                        # Update the last node's next to new head
                        last_node = self.head
                        while last_node.next != current:
                            last_node = last_node.next
                        last_node.next = self.head
                self.counter -= 1
                return
            prev = current
            current = current.next
            if current == self.head:
                break  # Went around the list and didn't find the value
        raise ValueError("Value not found in the list.")

    def size(self) -> int:
        return self.counter