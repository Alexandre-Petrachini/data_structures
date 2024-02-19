from typing import Optional, Dict


class Node:
    """
    Represents a node in a doubly linked list, typically used within an LRU cache implementation.
    
    Attributes:
        key (int): The key associated with the node's data.
        data (int): The data or value stored in the node.
        prev (Optional[Node]): A reference to the previous node in the list. None if this is the first node.
        next (Optional[Node]): A reference to the next node in the list. None if this is the last node.
    """
    def __init__(self, key: int, data: int):
        self.key: int = key
        self.data: int = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class LRUCache:
    """
    A simple implementation of a Least Recently Used (LRU) cache. The cache evicts the least recently accessed item
    when it exceeds its capacity.

    Attributes:
        capacity (int): The maximum number of items that can be stored in the cache.
    """
    def __init__(self, capacity: int):
        self.hmap: Dict[int, Node] = {}  # Maps keys to Node instances
        self.head: Node = Node(0, 0)  # Dummy head node
        self.tail: Node = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size: int = 0
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with a given key from the cache, and updates the item's position to reflect
        its recent access.
        
        Args:
            key (int): The key of the item to retrieve.
        
        Returns:
            int: The value associated with the key if found, -1 otherwise.
        """
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.__moveToHead(node)
        return node.data

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the value associated with a given key in the cache. If the cache exceeds its capacity,
        the least recently used item is removed.
        
        Args:
            key (int): The key of the item to insert or update.
            value (int): The value to associate with the key.
        """
        if key in self.hmap:
            node = self.hmap[key]
            node.data = value
            self.__moveToHead(node)
        else:
            new_node = Node(key, value)
            self.hmap[key] = new_node
            self.__addFirst(new_node)
            self.size += 1

            if self.size > self.capacity:
                self.__removeLRUEntry()

    def __removeLRUEntry(self) -> None:
        """
        Removes the least recently used (LRU) item from the cache.
        """
        tail_node = self.__popTail()
        del self.hmap[tail_node.key]
        self.size -= 1

    def __addFirst(self, node: Node) -> None:
        """
        Adds a node to the beginning of the doubly linked list (right after the dummy head node).
        
        Args:
            node (Node): The node to add.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __removeNode(self, node: Node) -> None:
        """
        Removes a node from the doubly linked list.
        
        Args:
            node (Node): The node to remove.
        """
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def __moveToHead(self, node: Node) -> None:
        """
        Moves a specific node to the beginning of the doubly linked list (making it the most recently used item).
        
        Args:
            node (Node): The node to move.
        """
        self.__removeNode(node)
        self.__addFirst(node)

    def __popTail(self) -> Node:
        """
        Removes and returns the node at the end of the doubly linked list (the least recently used item).
        
        Returns:
            Node: The node that was removed.
        """
        rem = self.tail.prev
        self.__removeNode(rem)
        return rem

    def display(self) -> None:
        """
        Prints the keys and values of the items in the cache in order from most to least recently used.
        """
        p = self.head.next
        while p != self.tail:
            print(f"[Key:{p.key}, Value:{p.data}]", end=" ")
            p = p.next
        print()