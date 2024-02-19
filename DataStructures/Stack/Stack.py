from typing import Any, List, Optional


class Stack:
    """
    A simple implementation of a stack data structure.

    Attributes:
        items (List[Any]): The items in the stack.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Stack class.
        """
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self.items

    def push(self, item: Any) -> None:
        """
        Adds an item to the top of the stack.

        Args:
            item (Any): The item to add to the stack.
        """
        self.items.append(item)

    def pop(self) -> Optional[Any]:
        """
        Removes and returns the item at the top of the stack.

        Returns:
            The item at the top of the stack if the stack is not empty.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> Optional[Any]:
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack if the stack is not empty.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def display(self) -> List[Any]:
        """
        Returns a list of all items in the stack.

        Returns:
            List[Any]: The items in the stack.
        """
        return self.items