from typing import Optional


class Node:
    """
    A node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: The next node in the list.
    """

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None