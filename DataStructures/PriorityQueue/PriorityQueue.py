from typing import List, Optional


class Node:
    """
    A node in a priority queue, holding information and its priority.

    Attributes:
        info: The content stored in the node.
        priority: The priority of the node, used to determine its position in the priority queue.
    """

    def __init__(self, info: str, priority: int) -> None:
        self.info: str = info
        self.priority: int = priority


class PriorityQueue:
    """
    Implements a priority queue using a list, where nodes are inserted based on their priority.
    
    The queue is organized in increasing order of priority, meaning lower priority values are at the front.
    """

    def __init__(self) -> None:
        """
        Initializes an empty priority queue.
        """
        self.queue: List[Node] = []

    def insert(self, node: Node) -> bool:
        """
        Inserts a new node into the priority queue in its correct position based on priority.
        
        Args:
            node (Node): The node to be inserted into the queue.
        
        Returns:
            bool: True if the node was inserted, False otherwise.
        """
        # If queue is empty, add the new node directly.
        if self.size() == 0:
            self.queue.append(node)
            return True
        
        # Traverse the queue to find the right place for the new node.
        for x in range(self.size()):
            if node.priority < self.queue[x].priority:
                self.queue.insert(x, node)
                return True
            elif x == (self.size() - 1):
                # If we have traversed the complete queue, add new node at the end.
                self.queue.append(node)
                return True
        
        return False  # This line is theoretically unreachable.

    def delete(self) -> Optional[Node]:
        """
        Removes and returns the highest priority node from the queue.

        Returns:
            Optional[Node]: The node with the highest priority, or None if the queue is empty.
        """
        return self.queue.pop(0) if self.queue else None

    def show(self) -> None:
        """
        Prints each element of the priority queue along with its priority.
        """
        for x in self.queue:
            print(f"{x.info} - {x.priority}")

    def size(self) -> int:
        """
        Returns the number of nodes in the priority queue.

        Returns:
            int: The size of the queue.
        """
        return len(self.queue)