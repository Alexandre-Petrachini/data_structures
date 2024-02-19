from typing import List, Tuple


class UnweightedGraph:
    """
    Represents an unweighted graph using adjacency lists.

    Attributes:
        vertices (int): The number of vertices in the graph.
        directed (bool): Indicates if the graph is directed. Defaults to True.
        edges (List[List[int]]): Adjacency list representing the graph's edges.
    """

    def __init__(self, vertices: int, directed: bool = True) -> None:
        self.vertices: int = vertices
        self.directed: bool = directed
        self.edges: List[List[int]] = [[] for _ in range(vertices)]

    def __str__(self) -> str:
        output: str = ""
        for i in range(self.vertices):
            output += f"{i}: " + " ".join(str(dest) for dest in self.edges[i]) + "\n"
        return output

    def has_vertex(self, vertex: int) -> bool:
        """Checks if a vertex exists in the graph."""
        return 0 <= vertex < self.vertices

    def has_edge(self, start: int, dest: int) -> bool:
        """Checks if an edge exists between two vertices."""
        return self.has_vertex(start) and self.has_vertex(dest) and dest in self.edges[start]

    def add_edge(self, start: int, dest: int) -> bool:
        """Adds an edge between two vertices."""
        if not self.has_edge(start, dest):
            self.edges[start].append(dest)
            if not self.directed:
                self.edges[dest].append(start)
            return True
        return False


class WeightedGraph:
    """
    Represents a weighted graph using adjacency lists, where edges are stored as tuples of (destination, weight).

    Attributes:
        vertices (int): The number of vertices in the graph.
        directed (bool): Indicates if the graph is directed. Defaults to True.
        edges (List[List[Tuple[int, int]]]): Adjacency list representing the graph's edges.
    """

    def __init__(self, vertices: int, directed: bool = True) -> None:
        self.vertices: int = vertices
        self.directed: bool = directed
        self.edges: List[List[Tuple[int, int]]] = [[] for _ in range(vertices)]

    def __str__(self) -> str:
        output: str = ""
        for i in range(self.vertices):
            edge_strs = [f"{dest} (weight: {weight})" for dest, weight in self.edges[i]]
            output += f"{i}: " + " ".join(edge_strs) + "\n"
        return output

    def has_vertex(self, vertex: int) -> bool:
        """Checks if a vertex exists in the graph."""
        return 0 <= vertex < self.vertices

    def has_edge(self, start: int, dest: int, weight: int) -> bool:
        """Checks if a weighted edge exists between two vertices."""
        return self.has_vertex(start) and self.has_vertex(dest) and (dest, weight) in self.edges[start]

    def add_edge(self, start: int, dest: int, weight: int) -> bool:
        """Adds a weighted edge between two vertices."""
        if not self.has_edge(start, dest, weight):
            self.edges[start].append((dest, weight))
            if not self.directed:
                self.edges[dest].append((start, weight))
            return True
        return False


def main():
    """
    Basic driver code to demonstrate the functionality of UnweightedGraph and WeightedGraph classes.
    """

    # Demonstrate UnweightedGraph
    ugraph = UnweightedGraph(5)
    ugraph.add_edge(0, 1)
    ugraph.add_edge(0, 2)
    ugraph.add_edge(0, 3)
    ugraph.add_edge(2, 4)
    ugraph.add_edge(1, 2)
    print(ugraph)

    # Demonstrate WeightedGraph
    wgraph = WeightedGraph(5)
    wgraph.add_edge(0, 2, weight=3)
    wgraph.add_edge(0, 3, weight=2)
    wgraph.add_edge(1, 3, weight=4)
    wgraph.add_edge(2, 1, weight=1)
    wgraph.add_edge(4, 3, weight=6)
    print(wgraph)

if __name__ == "__main__":
    main()